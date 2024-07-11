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
        routers = [dispositivo for dispositivo in self.red if isinstance(dispositivo, Router)]
        for router in routers:
            self.tablas_ospf[router] = router.tabla_enrutamiento

        # Simulación de actualización de tablas OSPF
        # Aquí deberías implementar la lógica de propagación de rutas entre routers

# Crear dispositivos
router1 = Router("Router1")
router2 = Router("Router2")
switch1 = Switch("Switch1")
pc1 = Dispositivo("PC1")
server1 = Dispositivo("Server1")

# Establecer conexiones
router1.agregar_interfaz("eth0", "192.168.1.1")
router1.agregar_interfaz("eth1", "192.168.2.1")
router2.agregar_interfaz("eth0", "192.168.2.2")
router2.agregar_interfaz("eth1", "192.168.3.1")
switch1.agregar_interfaz("port1", "192.168.1.2")
pc1.agregar_interfaz("eth0", "192.168.3.2")
server1.agregar_interfaz("eth0", "192.168.3.3")

# Configurar tablas de enrutamiento
router1.agregar_ruta("192.168.2.0", "255.255.255.0", "192.168.1.2")
router1.agregar_ruta("192.168.3.0", "255.255.255.0", "192.168.2.2")
router2.agregar_ruta("192.168.1.0", "255.255.255.0", "192.168.2.1")
router2.agregar_ruta("192.168.3.0", "255.255.255.0", "192.168.3.2")

# Crear instancia de OSPF y actualizar tablas
ospf = OSPF([router1, router2])
ospf.actualizar_tablas()

# Mostrar tablas de enrutamiento OSPF
for router, tabla in ospf.tablas_ospf.items():
    print(f"Tabla de enrutamiento de {router.nombre}: {tabla}")
