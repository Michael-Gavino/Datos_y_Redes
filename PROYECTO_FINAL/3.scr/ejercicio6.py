import time

# Simulación de métricas de CloudWatch
def simular_metricas_cloudwatch(api_name):
    print(f"Configurando métricas de CloudWatch para la API: {api_name}")
    metricas = {'Número de Solicitudes': 100, 'Latencia': 200, 'Errores': 5}
    for metrica, valor in metricas.items():
        print(f"\t{metrica}: {valor}")
    return metricas

# Simulación de creación de Dashboards de CloudWatch
def crear_dashboard_cloudwatch(api_name, metricas):
    print(f"Creando dashboard de CloudWatch para la API: {api_name}")
    dashboard = {'Nombre de la API': api_name, 'Widgets': []}
    for metrica, valor in metricas.items():
        widget = {'Nombre de la Métrica': metrica, 'Valor': valor, 'Gráfico': f"Gráfico de {metrica}"}
        dashboard['Widgets'].append(widget)
    for widget in dashboard['Widgets']:
        print(f"\tWidget: {widget['Nombre de la Métrica']} - {widget['Gráfico']}")
    return dashboard

# Simulación de configuración de alarmas de CloudWatch
def configurar_alarmas_cloudwatch(api_name, metricas, umbral_errores):
    print(f"Configurando alarmas de CloudWatch para la API: {api_name}")
    alarmas = []
    for metrica, valor in metricas.items():
        estado = 'ALARMA' if metrica == 'Errores' and valor > umbral_errores else 'OK'
        alarmas.append({'Nombre de la Métrica': metrica, 'Umbral': umbral_errores, 'Valor Actual': valor, 'Estado': estado})
    for alarma in alarmas:
        print(f"\tAlarma: {alarma['Nombre de la Métrica']} - Estado: {alarma['Estado']}")
    return alarmas

# Simulación del proceso completo de monitoreo de la API
def simulacion_monitoreo_api(api_name):
    metricas = simular_metricas_cloudwatch(api_name)
    crear_dashboard_cloudwatch(api_name, metricas)
    configurar_alarmas_cloudwatch(api_name, metricas, umbral_errores=10)

if __name__ == '__main__':
    simulacion_monitoreo_api("ProductsAPI")

