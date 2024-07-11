# Crear un grafo vacío
G = {}

# Añadir nodos (dispositivos)
G["Router"] = {}
G["Switch 1"] = {}
G["Switch 2"] = {}
G["PC 1"] = {}
G["PC 2"] = {}
G["PC 3"] = {}
G["PC 4"] = {}

# Añadir enlaces (conexiones)
G["Router"]["Switch 1"] = {}
G["Router"]["Switch 2"] = {}
G["Switch 1"]["PC 1"] = {}
G["Switch 1"]["PC 2"] = {}
G["Switch 2"]["PC 3"] = {}
G["Switch 2"]["PC 4"] = {}

# Mostrar el grafo
for nodo, conexiones in G.items():
    print(f"Nodo: {nodo}")
    for conexion in conexiones:
        print(f" - Conectado a: {conexion}")

# Nota: Este código no incluye la visualización gráfica que proporciona `networkx` y `matplotlib.pyplot`.
