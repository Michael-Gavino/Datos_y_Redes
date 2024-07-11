import matplotlib.pyplot as plt

# Clase para representar una instancia EC2
class EC2Instance:
    def __init__(self, tipo, cpu, almacenamiento_gb):
        self.tipo = tipo
        self.cpu = cpu
        self.almacenamiento_gb = almacenamiento_gb

# Clase para representar una opción de precios (On-Demand, Reserved, Spot)
class OpcionPrecio:
    def __init__(self, nombre, tarifa_por_hora):
        self.nombre = nombre
        self.tarifa_por_hora = tarifa_por_hora

# Función para calcular el costo de una instancia EC2 con una opción de precio específica
def calcular_costo(instancia, opcion_precio, horas):
    costo_total = opcion_precio.tarifa_por_hora * horas
    return costo_total

# Función para comparar las opciones de precios y calcular los costos para una instancia EC2 dada
def comparar_opciones_precio(instancia, opciones_precio, horas):
    resultados = {}
    for opcion in opciones_precio:
        costo = calcular_costo(instancia, opcion, horas)
        resultados[opcion.nombre] = costo
    return resultados

# Función para graficar los costos comparativos
def graficar_costos(resultados):
    opciones = list(resultados.keys())
    costos = list(resultados.values())

    plt.figure(figsize=(10, 6))
    plt.bar(opciones, costos, color=['blue', 'green', 'orange'])
    plt.xlabel('Opciones de Precio')
    plt.ylabel('Costo ($)')
    plt.title('Comparación de Costos de Opciones de Precio de EC2')
    plt.show()

# Función principal
def main():
    # Crear instancias EC2
    instancia_a = EC2Instance("t2.micro", 1, 30)
    instancia_b = EC2Instance("m5.large", 2, 100)

    # Definir opciones de precios
    on_demand = OpcionPrecio("On-Demand", 0.05)  # $0.05 por hora
    reserved = OpcionPrecio("Reserved", 0.03)   # $0.03 por hora (ejemplo de precio reducido)
    spot = OpcionPrecio("Spot", 0.02)           # $0.02 por hora (ejemplo de precio spot)

    # Simulación de costos para las instancias
    horas = 24  # Ejemplo de 24 horas de uso

    print(f"Simulación de costos para la instancia {instancia_a.tipo} durante {horas} horas:")
    resultados_a = comparar_opciones_precio(instancia_a, [on_demand, reserved, spot], horas)
    for opcion, costo in resultados_a.items():
        print(f"{opcion}: ${costo:.2f}")

    print()

    print(f"Simulación de costos para la instancia {instancia_b.tipo} durante {horas} horas:")
    resultados_b = comparar_opciones_precio(instancia_b, [on_demand, reserved, spot], horas)
    for opcion, costo in resultados_b.items():
        print(f"{opcion}: ${costo:.2f}")

    # Comparación visual de costos
    graficar_costos(resultados_a)

if __name__ == "__main__":
    main()


##sin grafico
# Clase para representar una instancia EC2
class EC2Instance:
    def __init__(self, tipo, cpu, almacenamiento_gb):
        self.tipo = tipo
        self.cpu = cpu
        self.almacenamiento_gb = almacenamiento_gb

# Clase para representar una opción de precios (On-Demand, Reserved, Spot)
class OpcionPrecio:
    def __init__(self, nombre, tarifa_por_hora):
        self.nombre = nombre
        self.tarifa_por_hora = tarifa_por_hora

# Función para calcular el costo de una instancia EC2 con una opción de precio específica
def calcular_costo(instancia, opcion_precio, horas):
    costo_total = opcion_precio.tarifa_por_hora * horas
    return costo_total

# Función para comparar las opciones de precios y calcular los costos para una instancia EC2 dada
def comparar_opciones_precio(instancia, opciones_precio, horas):
    resultados = {}
    for opcion in opciones_precio:
        costo = calcular_costo(instancia, opcion, horas)
        resultados[opcion.nombre] = costo
    return resultados

# Función principal
def main():
    # Crear instancias EC2
    instancia_a = EC2Instance("t2.micro", 1, 30)
    instancia_b = EC2Instance("m5.large", 2, 100)

    # Definir opciones de precios
    on_demand = OpcionPrecio("On-Demand", 0.05)  # $0.05 por hora
    reserved = OpcionPrecio("Reserved", 0.03)   # $0.03 por hora (ejemplo de precio reducido)
    spot = OpcionPrecio("Spot", 0.02)           # $0.02 por hora (ejemplo de precio spot)

    # Simulación de costos para las instancias
    horas = 24  # Ejemplo de 24 horas de uso

    print(f"Simulación de costos para la instancia {instancia_a.tipo} durante {horas} horas:")
    resultados_a = comparar_opciones_precio(instancia_a, [on_demand, reserved, spot], horas)
    for opcion, costo in resultados_a.items():
        print(f"{opcion}: ${costo:.2f}")

    print()

    print(f"Simulación de costos para la instancia {instancia_b.tipo} durante {horas} horas:")
    resultados_b = comparar_opciones_precio(instancia_b, [on_demand, reserved, spot], horas)
    for opcion, costo in resultados_b.items():
        print(f"{opcion}: ${costo:.2f}")

if __name__ == "__main__":
    main()
