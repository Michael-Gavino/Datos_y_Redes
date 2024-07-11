class Dispositivo:
    def __init__(self, nombre, tipo_dispositivo):
        self.nombre = nombre
        self.tipo_dispositivo = tipo_dispositivo
        self.direccion_ip = None

class Router(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre, 'Router')
        self.tabla_enrutamiento = {}

    def agregar_ruta(self, red, siguiente_salto):
        self.tabla_enrutamiento[red] = siguiente_salto

    def obtener_ruta(self, ip_destino):
        for red, siguiente_salto in self.tabla_enrutamiento.items():
            if self._verificar_ip_en_red(ip_destino, red):
                return siguiente_salto
        return None

    def _verificar_ip_en_red(self, ip, red):
        ip_addr = self._parsear_ip(ip)
        red_addr, mascara_red = red.split('/')
        direccion_red = self._parsear_ip(red_addr)
        mascara_red = int(mascara_red)
        return (ip_addr & (2**32 - 1 << (32 - mascara_red))) == direccion_red

    def _parsear_ip(self, ip):
        return int(ip_address(ip).packed.hex(), 16)

class Switch(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre, 'Switch')

class PC(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre, 'PC')

class Red:
    def __init__(self):
        self.dispositivos = []
        self.conexiones = []

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def conectar(self, dispositivo1, dispositivo2):
        self.conexiones.append((dispositivo1, dispositivo2))

    def asignar_direcciones_ip(self, cidr):
        red, tamano_subred = cidr.split('/')
        tamano_subred = int(tamano_subred)
        base_ip = red[:-len(red.split('.')[-1])]  # Eliminar la última parte de la IP
        ip_actual = 1  # Comenzar a asignar IPs desde 1

        for dispositivo in self.dispositivos:
            if isinstance(dispositivo, PC):
                dispositivo.direccion_ip = base_ip + str(ip_actual)
                ip_actual += 1

    def visualizar(self):
        print("Dispositivos en la red:")
        for dispositivo in self.dispositivos:
            print(f"{dispositivo.nombre} - Tipo: {dispositivo.tipo_dispositivo}, IP: {dispositivo.direccion_ip}")

    def simular_trafico(self, origen, destino):
        print(f"Simulando tráfico desde {origen.nombre} hacia {destino.nombre}")

# Crear la red y dispositivos
red = Red()
router1 = Router("Router1")
router2 = Router("Router2")
switch1 = Switch("Switch1")
switch2 = Switch("Switch2")
pc1 = PC("PC1")
pc2 = PC("PC2")
pc3 = PC("PC3")
pc4 = PC("PC4")

# Agregar dispositivos a la red
red.agregar_dispositivo(router1)
red.agregar_dispositivo(router2)
red.agregar_dispositivo(switch1)
red.agregar_dispositivo(switch2)
red.agregar_dispositivo(pc1)
red.agregar_dispositivo(pc2)
red.agregar_dispositivo(pc3)
red.agregar_dispositivo(pc4)

# Conectar dispositivos
red.conectar(router1, switch1)
red.conectar(router1, switch2)
red.conectar(switch1, pc1)
red.conectar(switch1, pc2)
red.conectar(switch2, pc3)
red.conectar(switch2, pc4)
red.conectar(router1, router2)

# Asignar direcciones IP
red.asignar_direcciones_ip('192.168.1.0/24')

# Visualizar la red y asignaciones de IP
red.visualizar()

# Simular tráfico
red.simular_trafico(pc1, pc3)
