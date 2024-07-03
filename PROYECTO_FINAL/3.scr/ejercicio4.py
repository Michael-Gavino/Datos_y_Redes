import time

# Configuración base de la API Gateway
url_base_api = 'https://api.ejemplo.com'
nombre_stage = 'dev'

# Configuración de recursos y métodos simulados
endpoints = {
    '/productos': ['GET', 'POST'],
    '/productos/{id}': ['GET', 'PUT', 'DELETE']
}
# Función para simular el despliegue de la API en un stage
def desplegar_api(url_base_api, nombre_stage, endpoints):
    print(f"Simulando configuración y despliegue de la API en Amazon API Gateway '{nombre_stage}'...")
    for ruta, metodos in endpoints.items():
        for metodo in metodos:
            print(f"Configurando {metodo} {ruta}")
            if metodo in ['POST', 'PUT', 'DELETE']:
                time.sleep(1)  # Simulación de tiempo de respuesta
            print(f"Respuesta: 20 - Successfully {metodo} {ruta}")
    print("Simulación de API desplegada exitosamente.")
# Simulación de despliegue de la API
if __name__ == '__main__':
    desplegar_api(url_base_api, nombre_stage, endpoints)


