# datos en formato json
import json
#creacionde la clase API
class API:
    def __init__(self):
        self.nombre_api = 'ProductosAPI'
        self.recursos = {}
        self.etapas = {}
        self.claves_api = {}
        self.politicas_iam = {}
        self.user_pools_cognito = {}

    # Ejercicio 1 y 2: Crear la API REST
    def crear_api_rest(self):
        print(f"Creando la API: {self.nombre_api}")
        return {'id': 'id-de-api'}

    def crear_recurso(self, id_p, p_ruta):
        id_recurso = f'id-recurso-{p_ruta}'
        self.recursos[p_ruta] = {
            'id_padre': id_p,
            'id_recurso': id_recurso,
            'ruta': f'/{p_ruta}'
        }
        print(f"Recurso creado: {p_ruta} con ID: {id_recurso}")
        return {'id': id_recurso}

    def agregar_metodo(self, id_recurso, metodo_http):
        print(f"Creando método {metodo_http} en el recurso ID: {id_recurso}")

    def integrar_con_lambda_y_dynamodb(self, id_recurso, metodo_http, uri_lambda):
        self.agregar_metodo(id_recurso, metodo_http)
        print(f"Integrando método {metodo_http} con URI: {uri_lambda} en el recurso ID: {id_recurso}")

    # Ejercicio 4: Despliegue de la API
    def crear_despliegue(self, nombre_etapa):
        self.etapas[nombre_etapa] = 'id-de-despliegue'
        print(f"Despliegue creado en la etapa: {nombre_etapa}")

    # Ejercicio 5: Control de acceso a la API REST
    def crear_clave_api(self, nombre_clave):
        self.claves_api[nombre_clave] = 'clave-api'
        print(f"Clave API '{nombre_clave}' creada con valor '{self.claves_api[nombre_clave]}'")
        return {'apiKey': self.claves_api[nombre_clave]}
    # crear la politica iam
    def crear_politica_iam(self, nombre_politica):
        self.politicas_iam[nombre_politica] = ['execute-api:Invoke', 'execute-api:ManageConnections']
        print(f"Política IAM '{nombre_politica}' creada con permisos: {self.politicas_iam[nombre_politica]}")
        return {'policyName': nombre_politica}
    #agregar autenticacion y  autorizacion
    def crear_user_pool_cognito(self, nombre_user_pool):
        self.user_pools_cognito[nombre_user_pool] = {
            'UserPoolId': 'id-de-user-pool',
            'ClientId': 'id-de-cliente'
        }
        print(f"User Pool '{nombre_user_pool}' creado con ID '{self.user_pools_cognito[nombre_user_pool]['UserPoolId']}'")
        return self.user_pools_cognito[nombre_user_pool]

    def configurar_control_acceso(self):
        clave_api = self.crear_clave_api('ProductsAPIKey')
        politica_iam = self.crear_politica_iam('ProductsAPIPolicy')
        user_pool_cognito = self.crear_user_pool_cognito('ProductsAPIUserPool')
        return {
            'Clave API': clave_api,
            'Política IAM': politica_iam,
            'User Pool Cognito': user_pool_cognito
        }

    # Ejercicio 6: Configuración de monitoreo de la API REST
    def configurar_cloudwatch(self):
        print("Configurando CloudWatch para monitoreo de métricas")
        # Simulación de configuración de CloudWatch

    # Ejercicio 7: Optimización de API Gateway
    def configurar_caching(self):
        print("Configurando caching para mejorar latencia de respuestas")
        # Simulación de configuración de caching

# Función para simular configuración de control de acceso
def simular_control_acceso(api_simulada):
    configuracion_control_acceso = api_simulada.configurar_control_acceso()
    print("\nConfiguración final de control de acceso:")
    print(json.dumps(configuracion_control_acceso, indent=4))

# Simulación del proceso de creación y despliegue de la API
if __name__ == '__main__':
    simulacion_api = API()
    
    # Crear la API
    api_creada = simulacion_api.crear_api_rest()
    
    # Crear recursos y métodos
    id_raiz = 'id-raiz-simulado'
    recurso_productos = simulacion_api.crear_recurso(id_raiz, 'productos')
    simulacion_api.integrar_con_lambda_y_dynamodb(recurso_productos['id'], 'GET', 'uri-lambda-get-all')
    simulacion_api.integrar_con_lambda_y_dynamodb(recurso_productos['id'], 'POST', 'uri-lambda-crear')

    recurso_id_producto = simulacion_api.crear_recurso(recurso_productos['id'], '{id}')
    simulacion_api.integrar_con_lambda_y_dynamodb(recurso_id_producto['id'], 'GET', 'uri-lambda-get-por-id')
    simulacion_api.integrar_con_lambda_y_dynamodb(recurso_id_producto['id'], 'PUT', 'uri-lambda-actualizar')
    simulacion_api.integrar_con_lambda_y_dynamodb(recurso_id_producto['id'], 'DELETE', 'uri-lambda-eliminar')
    
    # Desplegar la API
    simulacion_api.crear_despliegue('dev')
    
    # Configurar control de acceso
    simular_control_acceso(simulacion_api)
    
    # Configurar monitoreo
    simulacion_api.configurar_cloudwatch()
    
    # Configurar caching
    simulacion_api.configurar_caching()