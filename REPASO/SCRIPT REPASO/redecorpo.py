import networkx as nx
import matplotlib.pyplot as plt
import ipaddress

class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.interfaces = {}

    def agregar_interfaz(self, interfaz, direccion_ip):
        self.interfaces[interfaz] = direccion_ip

class Router(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tabla_enrutamiento = {}

    def agregar_ruta(self, subred, mascara, gateway):
        self.tabla_enrutamiento[(subred, mascara)] = gateway

class Switch(Dispositivo):
    pass

class OSPF:
    def __init__(self, red):
        self.red = red
        self.tablas_ospf = {}

    def actualizar_tablas(self):
        routers = [dispositivo for dispositivo in self.red.nodes() if isinstance(dispositivo, Router)]
        for router in routers:
            self.tablas_ospf[router] = router.tabla_enrutamiento

        # Lógica de actualización de tablas OSPF
        # Simulación de propagación de rutas entre routers

def asignar_subredes(red, inicio_ip):
    subredes = list(ipaddress.ip_network(inicio_ip).subnets(new_prefix=28))
    dispositivos = list(red.nodes())

    for i, dispositivo in enumerate(dispositivos):
        if isinstance(dispositivo, Dispositivo):
            for interfaz, subred in zip(dispositivo.interfaces.keys(), subredes):
                dispositivo.interfaces[interfaz] = str(subred[i + 1])

# Crear dispositivos
router1 = Router("Router1")
router2 = Router("Router2")
switch1 = Switch("Switch1")
pc1 = Dispositivo("PC1")
server1 = Dispositivo("Server1")

# Establecer conexiones
router1.agregar_interfaz("eth0", "192.168.1.1/24")
router1.agregar_interfaz("eth1", "192.168.2.1/24")
router2.agregar_interfaz("eth0", "192.168.2.2/24")
router2.agregar_interfaz("eth1", "192.168.3.1/24")
switch1.agregar_interfaz("port1", "192.168.1.2/24")
pc1.agregar_interfaz("eth0", "192.168.3.2/24")
server1.agregar_interfaz("eth0", "192.168.3.3/24")

# Agregar dispositivos a un grafo de red
red_corporativa = nx.Graph()
red_corporativa.add_nodes_from([router1, router2, switch1, pc1, server1])

# Establecer conexiones físicas entre dispositivos
red_corporativa.add_edge(router1, switch1)
red_corporativa.add_edge(router1, router2)
red_corporativa.add_edge(router2, pc1)
red_corporativa.add_edge(router2, server1)

# Asignar subredes a la red corporativa
asignar_subredes(red_corporativa, '192.168.0.0/24')

# Mostrar direcciones IP asignadas
for dispositivo in red_corporativa.nodes():
    if isinstance(dispositivo, Dispositivo):
        print(f"{dispositivo.nombre}: {dispositivo.interfaces}")

# Crear instancia de OSPF y actualizar tablas
ospf = OSPF(red_corporativa)
ospf.actualizar_tablas()

# Mostrar tablas de enrutamiento OSPF
for router, tabla in ospf.tablas_ospf.items():
    print(f"Tabla de enrutamiento de {router.nombre}: {tabla}")

# Visualizar la topología de la red
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(red_corporativa)
nx.draw(red_corporativa, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
plt.title("Topología de Red Corporativa")
plt.show()

# Función para simular envío de paquetes
def enviar_paquete(origen, destino):
    # Implementar lógica de enrutamiento para determinar el camino
    # Simulación de envío de paquete y registro del camino
    print(f"Enviando paquete desde {origen.nombre} a {destino.nombre}")

# Ejemplo de simulación de envío de paquete
enviar_paquete(pc1, server1)
