"""
sim_serverless.py

Proyecto de simulación local (Python) de una API REST construida con:
- Simulación de Amazon API Gateway (Flask + routing + auth middleware)
- Simulación de AWS Lambda functions (métodos CRUD)
- Simulación de DynamoDB (tabla en memoria con persistencia JSON opcional)
- Simulación de mecanismos de acceso: API Key, IAM-role, Cognito token
- Simulación de CloudWatch (métricas, dashboard, alarmas)
- Optimización: caching (TTL), throttling (rate-limit), compresión (simulada)

Instrucciones:
    pip install flask cachetools
    python sim_serverless.py
"""

from flask import Flask, request, jsonify, make_response
import time, json, threading
from functools import wraps
from cachetools import TTLCache, cached

# -------------------------------
# Simulación DynamoDB (in-memory)
# -------------------------------
class DynamoDBSim:
    """
    Tabla simulada en memoria. Soporta CRUD básico y persistencia opcional a un archivo JSON.
    """
    def __init__(self, table_name='ProductsTable', persist_file=None):
        self.table_name = table_name
        self.persist_file = persist_file
        self._items = []
        self._load()

    def _load(self):
        if self.persist_file:
            try:
                with open(self.persist_file, 'r', encoding='utf-8') as f:
                    self._items = json.load(f)
            except Exception:
                self._items = []
        else:
            # Datos iniciales
            self._items = [
                {'id': 1, 'name': 'Product 1', 'price': 100},
                {'id': 2, 'name': 'Product 2', 'price': 150},
            ]

    def _save(self):
        if self.persist_file:
            with open(self.persist_file, 'w', encoding='utf-8') as f:
                json.dump(self._items, f, ensure_ascii=False, indent=2)

    def scan(self):
        return list(self._items)

    def get(self, product_id):
        return next((p for p in self._items if p['id'] == product_id), None)

    def put(self, item):
        # assign id if missing
        if 'id' not in item or item['id'] is None:
            item['id'] = (max([p['id'] for p in self._items]) + 1) if self._items else 1
        self._items.append(item)
        self._save()
        return item

    def update(self, product_id, updates):
        p = self.get(product_id)
        if p:
            p.update(updates)
            self._save()
        return p

    def delete(self, product_id):
        original_len = len(self._items)
        self._items = [p for p in self._items if p['id'] != product_id]
        self._save()
        return len(self._items) < original_len

# --------------------------------
# Simulación Lambda (funciones)
# --------------------------------
class LambdaHandlers:
    """
    Conjunto de 'funciones lambda' que ejecutan la lógica de negocio.
    Todas reciben (event, context) para simular AWS Lambda signature.
    """
    def __init__(self, db: DynamoDBSim):
        self.db = db

    def create_product(self, event, context):
        body = event.get('body') or {}
        item = {
            'name': body.get('name'),
            'price': body.get('price')
        }
        created = self.db.put(item)
        return {'statusCode': 201, 'body': created}

    def get_all_products(self, event, context):
        items = self.db.scan()
        return {'statusCode': 200, 'body': items}

    def get_product_by_id(self, event, context):
        pid = int(event['pathParameters'].get('id'))
        product = self.db.get(pid)
        if not product:
            return {'statusCode': 404, 'body': {'message': 'Product not found'}}
        return {'statusCode': 200, 'body': product}

    def update_product(self, event, context):
        pid = int(event['pathParameters'].get('id'))
        updates = event.get('body') or {}
        updated = self.db.update(pid, updates)
        if not updated:
            return {'statusCode': 404, 'body': {'message': 'Product not found'}}
        return {'statusCode': 200, 'body': updated}

    def delete_product(self, event, context):
        pid = int(event['pathParameters'].get('id'))
        deleted = self.db.delete(pid)
        if not deleted:
            return {'statusCode': 404, 'body': {'message': 'Product not found'}}
        return {'statusCode': 200, 'body': {'message': 'Product deleted'}}

# --------------------------------------------
# Simulación de Autenticación y Autorización
# --------------------------------------------
class AuthSim:
    """
    - API Keys stored in-memory
    - IAM roles simulated by checking a header 'X-IAM-Role'
    - Cognito-like token simulated by checking 'Authorization: Bearer <token>'
    """
    VALID_API_KEYS = {'ProductsAPIKey': 'mi_api_key_123'}
    VALID_IAM_ROLES = {'admin', 'developer'}
    VALID_TOKENS = {'token_valido_abc'}

    @staticmethod
    def check_api_key(api_key):
        return api_key in AuthSim.VALID_API_KEYS.values()

    @staticmethod
    def check_iam_role(role):
        return role in AuthSim.VALID_IAM_ROLES

    @staticmethod
    def check_cognito_token(token):
        return token in AuthSim.VALID_TOKENS

# ---------------------------------------
# Simulación CloudWatch (métricas sencilla)
# ---------------------------------------
class CloudWatchSim:
    """
    Recolecta métricas por ruta/método: count, errors, total_latency_ms
    Ofrece funciones para imprimir un 'dashboard' y comprobar alarmas.
    """
    def __init__(self):
        self.metrics = {}  # key = (method, path)

    def record(self, method, path, latency_ms, error=False):
        key = (method, path)
        m = self.metrics.setdefault(key, {'count': 0, 'errors': 0, 'total_latency_ms': 0})
        m['count'] += 1
        m['total_latency_ms'] += latency_ms
        if error:
            m['errors'] += 1

    def get_snapshot(self):
        snap = {}
        for (method, path), data in self.metrics.items():
            avg_lat = data['total_latency_ms'] / data['count'] if data['count'] else 0
            snap[f"{method} {path}"] = {
                'Requests': data['count'],
                'Errors': data['errors'],
                'AvgLatencyMs': round(avg_lat, 2)
            }
        return snap

    def print_dashboard(self):
        print("\n=== CloudWatch Simulated Dashboard ===")
        snap = self.get_snapshot()
        for k, v in snap.items():
            print(f"{k}: reqs={v['Requests']}, errors={v['Errors']}, avg_lat={v['AvgLatencyMs']}ms")
        print("======================================\n")

    def check_alarms(self, error_threshold=5, latency_threshold_ms=1000):
        alarms = []
        for (m, p), d in self.metrics.items():
            avg_lat = d['total_latency_ms'] / d['count'] if d['count'] else 0
            if d['errors'] > error_threshold:
                alarms.append((m, p, 'HighErrorRate', d['errors']))
            if avg_lat > latency_threshold_ms:
                alarms.append((m, p, 'HighLatency', round(avg_lat,2)))
        return alarms

# ---------------------------------------
# Optimizations: caching, throttling, compression
# ---------------------------------------
# simple per-route TTL cache using cachetools
route_cache = TTLCache(maxsize=100, ttl=60)  # default TTL 60s

# Basic in-memory throttling: map (client_ip, method_path) -> [timestamps]
class SimpleThrottler:
    def __init__(self, max_per_sec=5):
        self.max_per_sec = max_per_sec
        self.calls = {}  # key -> list of timestamps

    def allow(self, key):
        now = time.time()
        window_start = now - 1.0
        arr = self.calls.setdefault(key, [])
        # remove old
        while arr and arr[0] < window_start:
            arr.pop(0)
        if len(arr) >= self.max_per_sec:
            return False
        arr.append(now)
        return True

throttler = SimpleThrottler(max_per_sec=10)  # default 10 req/s per client+route

# ---------------------------------------
# API Gateway simulation: Flask app + middleware
# ---------------------------------------
app = Flask(__name__)

# instantiate simulations
db = DynamoDBSim(persist_file=None)
lambdas = LambdaHandlers(db)
cw = CloudWatchSim()
auth = AuthSim()

def api_gateway_route(method):
    """
    Decorator factory that wraps a Flask route handler to simulate:
    - API Gateway authorization selection (API Key / IAM / Cognito)
    - Throttling
    - Caching for GETs
    - Metrics collection
    - Invoking the lambda handler and formatting responses
    """
    def decorator(lambda_func, require_auth=True, allowed_auth_methods=('api_key','iam','cognito')):
        @wraps(lambda_func)
        def wrapper(*args, **kwargs):
            start = time.time()
            path = request.path
            client_ip = request.remote_addr or 'local'
            method_name = request.method

            # --- Authorization (choose any of allowed methods) ---
            # Check API Key (header X-API-Key)
            api_key = request.headers.get('X-API-Key')
            iam_role = request.headers.get('X-IAM-Role')
            auth_header = request.headers.get('Authorization')
            token = None
            if auth_header and auth_header.startswith('Bearer '):
                token = auth_header.split(' ',1)[1]

            authorized = False
            if not require_auth:
                authorized = True
            else:
                for m in allowed_auth_methods:
                    if m == 'api_key' and api_key and auth.check_api_key(api_key):
                        authorized = True; break
                    if m == 'iam' and iam_role and auth.check_iam_role(iam_role):
                        authorized = True; break
                    if m == 'cognito' and token and auth.check_cognito_token(token):
                        authorized = True; break

            if not authorized:
                latency = (time.time() - start)*1000
                cw.record(method_name, path, latency, error=True)
                return make_response(jsonify({'message':'Unauthorized'}), 401)

            # --- Throttling ---
            throttle_key = f"{client_ip}:{method_name}:{path}"
            if not throttler.allow(throttle_key):
                latency = (time.time() - start)*1000
                cw.record(method_name, path, latency, error=True)
                return make_response(jsonify({'message':'Too Many Requests'}), 429)

            # --- Caching (only for safe GET caching) ---
            cache_key = None
            if method_name == 'GET':
                cache_key = f"{method_name}:{path}:{json.dumps(request.args, sort_keys=True)}"
                cached_resp = route_cache.get(cache_key)
                if cached_resp:
                    latency = (time.time() - start)*1000
                    cw.record(method_name, path, latency, error=False)
                    # indicate cache hit in header
                    resp = make_response(jsonify(cached_resp['body']), cached_resp.get('statusCode',200))
                    resp.headers['X-Cache'] = 'HIT'
                    return resp

            # --- Prepare event for lambda ---
            event = {
                'pathParameters': kwargs,
                'queryStringParameters': request.args.to_dict(),
                'body': request.get_json(silent=True) or {},
                'headers': dict(request.headers),
                'requestContext': {'identity': {'sourceIp': client_ip}}
            }

            # --- Invoke lambda-like function ---
            try:
                result = lambda_func(event, {})  # context empty
                status = result.get('statusCode', 200)
                body = result.get('body')
                latency = (time.time() - start)*1000
                cw.record(method_name, path, latency, error=(status>=400))
                # caching store
                if cache_key and status < 300:
                    route_cache[cache_key] = {'statusCode': status, 'body': body}
                # compression simulated by header if client asks 'Accept-Encoding: gzip'
                resp = make_response(jsonify(body), status)
                if 'gzip' in (request.headers.get('Accept-Encoding','') or ''):
                    resp.headers['Content-Encoding'] = 'gzip-simulated'
                resp.headers['X-Cache'] = 'MISS'
                return resp
            except Exception as e:
                latency = (time.time() - start)*1000
                cw.record(method_name, path, latency, error=True)
                return make_response(jsonify({'message': 'Internal Server Error', 'detail': str(e)}), 500)

        return wrapper
    return decorator

# ----------------------------
# Route bindings (API surface)
# ----------------------------
# GET /products
@app.route('/products', methods=['GET'])
@api_gateway_route('GET')(lambdas.get_all_products)
def get_products():
    # wrapper target is not used directly since decorator invokes lambda handler
    pass

# POST /products
@app.route('/products', methods=['POST'])
@api_gateway_route('POST')(lambdas.create_product)
def post_product():
    pass

# GET /products/<id>
@app.route('/products/<int:id>', methods=['GET'])
@api_gateway_route('GET')(lambdas.get_product_by_id)
def get_product(id):
    pass

# PUT /products/<id>
@app.route('/products/<int:id>', methods=['PUT'])
@api_gateway_route('PUT')(lambdas.update_product)
def put_product(id):
    pass

# DELETE /products/<id>
@app.route('/products/<int:id>', methods=['DELETE'])
@api_gateway_route('DELETE')(lambdas.delete_product)
def delete_product(id):
    pass

# ----------------------------------------
# Utility endpoints for observability
# ----------------------------------------
@app.route('/__cloudwatch__/dashboard', methods=['GET'])
def cloudwatch_dashboard():
    """
    Endpoint to view the simulated CloudWatch dashboard (JSON).
    """
    return jsonify(cw.get_snapshot())

@app.route('/__cloudwatch__/alarms', methods=['GET'])
def cloudwatch_alarms():
    alarms = cw.check_alarms(error_threshold=2, latency_threshold_ms=1000)
    return jsonify({'alarms': alarms})

# ----------------------------------------
# Self-test runner: runs a few requests programmatically
# ----------------------------------------
def run_self_tests():
    import requests
    base = 'http://127.0.0.1:5000'
    headers_ok = {'X-API-Key': AuthSim.VALID_API_KEYS['ProductsAPIKey'], 'Accept-Encoding': 'gzip'}
    headers_bad = {'X-API-Key': 'wrong'}
    print("\n-- Running self-tests (these appear in console as requests) --")
    # create
    r = requests.post(f"{base}/products", json={'name':'New Product','price':120}, headers=headers_ok)
    print("POST /products ->", r.status_code, r.json())
    # get all
    r = requests.get(f"{base}/products", headers=headers_ok)
    print("GET /products ->", r.status_code, r.json())
    # get by id (2)
    r = requests.get(f"{base}/products/2", headers=headers_ok)
    print("GET /products/2 ->", r.status_code, r.json())
    # update
    r = requests.put(f"{base}/products/2", json={'price':175}, headers=headers_ok)
    print("PUT /products/2 ->", r.status_code, r.json())
    # delete
    r = requests.delete(f"{base}/products/2", headers=headers_ok)
    print("DELETE /products/2 ->", r.status_code, r.json())
    # unauthorized
    r = requests.get(f"{base}/products", headers=headers_bad)
    print("GET /products (bad key) ->", r.status_code, r.json())
    # dashboard
    r = requests.get(f"{base}/__cloudwatch__/dashboard")
    print("CLOUDWATCH DASHBOARD ->", r.status_code, json.dumps(r.json(), indent=2))

# ----------------------------------------
# Main entrypoint
# ----------------------------------------
if __name__ == '__main__':
    # start Flask in a thread and then run self-tests so the user sees the whole flow
    from threading import Thread
    def run_app():
        app.run(debug=False, use_reloader=False)

    server_thread = Thread(target=run_app, daemon=True)
    server_thread.start()

    # wait server ready
    time.sleep(1.0)
    print("Server started at http://127.0.0.1:5000")
    # Run a sequence of example calls to demonstrate integration
    try:
        run_self_tests()
        # print dashboard and alarms in console
        cw.print_dashboard()
        alarms = cw.check_alarms(error_threshold=1, latency_threshold_ms=500)
        if alarms:
            print("=== ALARMAS DETECTADAS ===")
            for a in alarms:
                print(a)
        else:
            print("No hay alarmas críticas.")
    except Exception as e:
        print("Error en pruebas automáticas:", e)

    # keep running the Flask server (so you can test with Postman)
    server_thread.join()
