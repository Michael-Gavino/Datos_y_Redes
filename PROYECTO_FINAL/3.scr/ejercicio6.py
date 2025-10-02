import time

# =====================================================
# 📊 SIMULACIÓN DE CLOUDWATCH PARA API GATEWAY
# =====================================================
# Este script simula cómo se configuraría el monitoreo de una API
# en Amazon CloudWatch, incluyendo métricas, dashboards y alarmas.
# CloudWatch permite observar el rendimiento de las APIs y detectar
# posibles errores o anomalías en su funcionamiento.

# =====================================================
# FUNCIÓN: simular_metricas_cloudwatch
# =====================================================
def simular_metricas_cloudwatch(api_name):
    """
    Simula la recolección de métricas básicas de una API en CloudWatch.

    Args:
        api_name (str): Nombre de la API a monitorear.

    Returns:
        dict: Diccionario con las métricas simuladas (solicitudes, latencia, errores).
    """
    print(f"📈 Configurando métricas de CloudWatch para la API: {api_name}")
    
    # Métricas simuladas (en un entorno real provienen de CloudWatch automáticamente)
    metricas = {
        'Número de Solicitudes': 100,  # Total de peticiones recibidas
        'Latencia': 200,               # Tiempo promedio de respuesta (ms)
        'Errores': 5                   # Número de solicitudes fallidas
    }
    
    # Mostrar métricas recolectadas
    for metrica, valor in metricas.items():
        print(f"\t✅ {metrica}: {valor}")
    
    return metricas


# =====================================================
# FUNCIÓN: crear_dashboard_cloudwatch
# =====================================================
def crear_dashboard_cloudwatch(api_name, metricas):
    """
    Simula la creación de un dashboard en CloudWatch para visualizar métricas de la API.

    Args:
        api_name (str): Nombre de la API.
        metricas (dict): Métricas recopiladas para la API.

    Returns:
        dict: Estructura simulada del dashboard con widgets por cada métrica.
    """
    print(f"📊 Creando dashboard de CloudWatch para la API: {api_name}")
    
    # Estructura simulada del dashboard
    dashboard = {
        'Nombre de la API': api_name,
        'Widgets': []
    }
    
    # Crear un widget por cada métrica
    for metrica, valor in metricas.items():
        widget = {
            'Nombre de la Métrica': metrica,
            'Valor': valor,
            'Gráfico': f"Gráfico de {metrica}"
        }
        dashboard['Widgets'].append(widget)
    
    # Mostrar widgets creados
    for widget in dashboard['Widgets']:
        print(f"\t📌 Widget: {widget['Nombre de la Métrica']} - {widget['Gráfico']}")
    
    return dashboard


# =====================================================
# FUNCIÓN: configurar_alarmas_cloudwatch
# =====================================================
def configurar_alarmas_cloudwatch(api_name, metricas, umbral_errores):
    """
    Simula la configuración de alarmas en CloudWatch para detectar anomalías.

    Args:
        api_name (str): Nombre de la API.
        metricas (dict): Métricas recopiladas.
        umbral_errores (int): Valor máximo de errores permitido antes de activar la alarma.

    Returns:
        list: Lista de alarmas configuradas, con su estado (OK o ALARMA).
    """
    print(f"🚨 Configurando alarmas de CloudWatch para la API: {api_name}")
    alarmas = []
    
    # Crear una alarma por cada métrica
    for metrica, valor in metricas.items():
        estado = 'ALARMA' if metrica == 'Errores' and valor > umbral_errores else 'OK'
        alarmas.append({
            'Nombre de la Métrica': metrica,
            'Umbral': umbral_errores,
            'Valor Actual': valor,
            'Estado': estado
        })
    
    # Mostrar el estado de cada alarma
    for alarma in alarmas:
        print(f"\t🔔 Alarma: {alarma['Nombre de la Métrica']} - Estado: {alarma['Estado']}")
    
    return alarmas


# =====================================================
# FUNCIÓN: simulacion_monitoreo_api
# =====================================================
def simulacion_monitoreo_api(api_name):
    """
    Ejecuta el flujo completo de monitoreo simulado para una API:
    1. Obtiene métricas
    2. Crea un dashboard
    3. Configura alarmas

    Args:
        api_name (str): Nombre de la API a monitorear.
    """
    metricas = simular_metricas_cloudwatch(api_name)
    crear_dashboard_cloudwatch(api_name, metricas)
    configurar_alarmas_cloudwatch(api_name, metricas, umbral_errores=10)


# =====================================================
# BLOQUE PRINCIPAL
# =====================================================
# Si el archivo se ejecuta directamente, inicia la simulación de monitoreo
# para una API llamada "ProductsAPI".
if __name__ == '__main__':
    simulacion_monitoreo_api("ProductsAPI")

