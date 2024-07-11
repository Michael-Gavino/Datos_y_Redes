# Definir precios USD por hora
precio_on_demand = 0.0084 
precio_reserved = 0.005   
precio_spot = 0.003        

# Definir otros costos USD por gb al mes
horas_por_mes = 720
meses = 6
almacenamiento_gb = 20
costo_almacenamiento_por_gb = 0.10  

# Calcular costos
def calcular_costos(horas_por_mes, meses, almacenamiento_gb, costo_almacenamiento_por_gb, precio_por_hora):
    costo_computo = horas_por_mes * meses * precio_por_hora
    costo_almacenamiento = almacenamiento_gb * costo_almacenamiento_por_gb * meses
    costo_total = costo_computo + costo_almacenamiento
    return costo_total

# Calcular costos para cada tipo de instancia
costo_on_demand = calcular_costos(horas_por_mes, meses, almacenamiento_gb, costo_almacenamiento_por_gb, precio_on_demand)
costo_reserved = calcular_costos(horas_por_mes, meses, almacenamiento_gb, costo_almacenamiento_por_gb, precio_reserved)
costo_spot = calcular_costos(horas_por_mes, meses, almacenamiento_gb, costo_almacenamiento_por_gb, precio_spot)

# Imprimir resultados
print(f"Costo Total On-Demand: ${costo_on_demand:.2f} USD")
print(f"Costo Total Reserved: ${costo_reserved:.2f} USD")
print(f"Costo Total Spot: ${costo_spot:.2f} USD")
