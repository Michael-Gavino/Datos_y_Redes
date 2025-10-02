# ============================================================
# Simulación completa de la creación, despliegue y configuración
# de una API REST utilizando conceptos de Amazon API Gateway.
#
# Incluye:
#  - Creación de API y recursos
#  - Integración con Lambda y DynamoDB
#  - Despliegue en entornos
#  - Control de acceso (API Key, IAM, Cognito)
#  - Monitoreo con CloudWatch
#  - Optimización con caching
# ============================================================

import time
import json

# ------------------------------------------------------------
# Clase: API
# Descripción:
#   Representa una simulación de la creación y configuración de
#   una API REST en Amazon API Gateway. Contiene métodos para 
#   crear recursos, agregar métodos HTTP, integrar servicios, 
#   gestionar el acceso, monitorear y optimizar el rendimiento.
# ------------------------------------------------------------
class API:
    def __init__(self):
        # Atributos principales de la API
        self.nombre_api = 'ProductosAPI'
        self.recursos = {}              # Recursos y rutas de la API
        self.etapas = {}                # Etapas de despliegue (stages)
        self.claves_api = {}            # Claves API creadas
        self.politicas_iam = {}         # Políticas IAM creadas
        self.user_pools_cognito = {}    # User Pools de Cognito creados

    # --------------------------------------------------------
    # Ejercicio 1 y 2: Crear la API REST
    # --------------------------------------------------------
    def crear_api_rest(self):
        """
        Simula la creación de una API REST en Amazon API Gateway.
        Retorna:
            dict: ID simulado de la API creada.
        """
        print(f"Creando la API: {self.nombre_api}")
        return {'id': 'id-de-api'}

    def crear_recurso(self, id_p, p_ruta):
        """
        Crea un nuevo recurso dentro de la API (por ejemplo, /productos o /productos/{id}).
        Parámetros:
            id_p (str): ID del recurso padre (por ejemplo, raíz).
            p_ruta (str): Nombre del recurso (ruta).
        Retorna:
            dict: ID simulado del recurso creado.
        """
        id_recurso = f'id-recurso-{p_ruta}'
        self.recursos[p_ruta] = {
            'id_padre': id_p,
            'id_recurso': id_recurso,
            'ruta': f'/{p_ruta}'
        }
        print(f"Recurso creado: {p_ruta} con ID: {id_recurso}")
        return {'id': id_recurso}

    def agregar_metodo(self, id_recurso, metodo_http):
        """
        Agrega un método HTTP (GET, POST, PUT, DELETE) a un recurso.
        Parámetros:
            id_recurso (str): ID del recurso al cual se agrega el método.
            metodo_http (str): Verbo HTTP a agregar.
        """
        print(f"Creando método {metodo_http} en el recurso ID: {id_recurso}")

    def integrar_con_lambda_y_dynamodb(self, id_recurso, metodo_http, uri_lambda):
        """
        Simula la integración de un método HTTP con una función Lambda
        y una tabla DynamoDB.
        Parámetros:
            id_recurso (str): ID del recurso.
            metodo_http (str): Método HTTP (GET, POST, etc.).
            uri_lambda (str): URI de la función Lambda.
        """
        self.agregar_metodo(id_recurso, metodo_http)
        print(f"Integrando método {metodo_http} con URI: {uri_lambda} en el recurso ID: {id_recurso}")

    # --------------------------------------------------------
    # Ejercicio 4: Despliegue de la API
    # --------------------------------------------------------
    def crear_despliegue(self, nombre_etapa):
        """
        Simula el despliegue de la API en un 'stage' o entorno (por ejemplo: dev, prod).
        Parámetros:
            nombre_etapa (str): Nombre del entorno.
        """
        self.etapas[nombre_etapa] = 'id-de-despliegue'
        print(f"Despliegue creado en la etapa: {nombre_etapa}")

    # --------------------------------------------------------
    # Ejercicio 5: Control de acceso a la API REST
    # --------------------------------------------------------
    def crear_clave_api(self, nombre_clave):
        """
        Crea una API Key para autenticar solicitudes.
        Parámetros:
            nombre_clave (str): Nombre de la clave.
        Retorna:
            dict: Clave API creada.
        """
        self.claves_api[nombre_clave] = 'clave-api'
        print(f"Clave API '{nombre_clave}' creada con valor '{self.claves_api[nombre_clave]}'")
        return {'apiKey': self.claves_api[nombre_clave]}

    def crear_politica_iam(self, nombre_politica):
        """
        Crea una política IAM con permisos específicos para la API.
        Parámetros:
            nombre_politica (str): Nombre de la política IAM.
        Retorna:
            dict: Nombre de la política creada.
        """
        self.politicas_iam[nombre_politica] = ['execute-api:Invoke', 'execute-api:ManageConnections']
        print(f"Política IAM '{nombre_politica}' creada con permisos: {self.politicas_iam[nombre_politica]}")
        return {'policyName': nombre_politica}

    def crear_user_pool_cognito(self, nombre_user_pool):
        """
        Crea un User Pool en Amazon Cognito para la autenticación de usuarios.
        Parámetros:
            nombre_user_pool (str): Nombre del user pool.
        Retorna:
            dict: Información del user pool creado.
        """
        self.user_pools_cognito[nombre_user_pool] = {
            'UserPoolId': 'id-de-user-pool',
            'ClientId': 'id-de-cliente'
        }
        print(f"User Pool '{nombre_user_pool}' creado con ID '{self.user_pools_cognito[nombre_user_pool]['UserPoolId']}'")
        return self.user_pools_cognito[nombre_user_pool]

    def configurar_control_acceso(self):
        """
        Configura los tres métodos principales de control de acceso:
        - API Key
        - IAM Policy
        - Cognito User Pool
        Retorna:
            dict: Configuración completa de acceso.
        """
        clave_api = self.crear_clave_api('ProductsAPIKey')
        politica_iam = self.crear_politica_iam('ProductsAPIPolicy')
        user_pool_cognito = self.crear_user_pool_cognito('ProductsAPIUserPool')
        return {
            'Clave API': clave_api,
            'Política IAM': politica_iam,
            'User Pool Cognito': user_pool_cognito
        }

    # --------------------------------------------------------
    # Ejercicio 6: Configuración de monitoreo
    # --------------------------------------------------------
    def configurar_cloudwatch(self):
        """
        Simula la configuración del servicio Amazon CloudWatch 
        para monitorear métricas de la API.
        """
        print("Configurando CloudWatch para monitoreo de métricas")

    # --------------------------------------------------------
    # Ejercicio 7: Optimización con Caching
    # --------------------------------------------------------
    def configurar_caching(self):
        """
        Simula la configuración del sistema de caching para mejorar
        la latencia de las respuestas de la API.
        """
        print("Configurando caching para mejorar latencia de respuestas")

# ------------------------------------------------------------
# Función auxiliar: simular_control_acceso
# Descripción:
#   Ejecuta la configuración de control de acceso y muestra el 
#   resultado en formato JSON legible.
# ------------------------------------------------------------
def simular_control_acceso(api_simulada):
    configuracion_control_acceso = api_simulada.configurar_control_acceso()
    print("\nConfiguración final de control de acceso:")
    print(json.dumps(configuracion_control_acceso, indent=4))

# ------------------------------------------------------------
# BLOQUE PRINCIPAL
# Simula el flujo completo de creación, despliegue y configuración
# de una API REST llamada "ProductosAPI".
# ------------------------------------------------------------
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
