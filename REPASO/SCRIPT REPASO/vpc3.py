# Clase VPC
class VPC:
    def __init__(self, cidr):
        self.cidr = cidr
        self.subnets = []  # Lista para almacenar las subredes de la VPC
        self.internet_gateway = None  # Variable para almacenar la puerta de enlace de Internet

    # Método para añadir una subred a la VPC
    def add_subnet(self, cidr, is_public=False):
        subnet = Subnet(cidr, is_public)  # Crear una subred con el CIDR proporcionado
        self.subnets.append(subnet)  # Añadir la subred a la lista de subredes
        return subnet

    # Método para adjuntar una puerta de enlace de Internet a la VPC
    def attach_internet_gateway(self, internet_gateway):
        self.internet_gateway = internet_gateway

# Clase Subnet
class Subnet:
    def __init__(self, cidr, is_public=False):
        self.cidr = cidr
        self.is_public = is_public  # Indica si la subred es pública o privada
        self.route_table = RouteTable()  # Tabla de rutas para la subred

# Clase RouteTable
class RouteTable:
    def __init__(self):
        self.routes = []  # Lista para almacenar las rutas

    # Método para añadir una ruta a la tabla de rutas
    def add_route(self, destination, target):
        route = {"destination": destination, "target": target}  # Crear una nueva ruta
        self.routes.append(route)  # Añadir la ruta a la lista de rutas

# Clase InternetGateway
class InternetGateway:
    def __init__(self, name):
        self.name = name  # Nombre de la puerta de enlace de Internet

# Clase NatGateway
class NatGateway:
    def __init__(self, name, subnet):
        self.name = name  # Nombre de la puerta de enlace NAT
        self.subnet = subnet  # Subred donde se encuentra la NAT Gateway

# Clase EC2Instance
class EC2Instance:
    def __init__(self, name, subnet):
        self.name = name  # Nombre de la instancia EC2
        self.subnet = subnet  # Subred donde se encuentra la instancia

# Crear una VPC con el rango CIDR 10.0.0.0/16
vpc = VPC('10.0.0.0/16')

# Crear una subred pública con el rango CIDR 10.0.1.0/24
public_subnet = vpc.add_subnet('10.0.1.0/24', is_public=True)

# Crear una subred privada con el rango CIDR 10.0.2.0/24
private_subnet = vpc.add_subnet('10.0.2.0/24', is_public=False)

# Crear y adjuntar una puerta de enlace de Internet a la VPC
internet_gateway = InternetGateway('InternetGateway')
vpc.attach_internet_gateway(internet_gateway)

# Añadir una ruta a la tabla de rutas de la subred pública que apunte a la puerta de enlace de Internet
public_subnet.route_table.add_route('0.0.0.0/0', internet_gateway)

# Crear y configurar una puerta de enlace NAT en la subred pública
nat_gateway = NatGateway('NatGateway', public_subnet)

# Añadir una ruta a la tabla de rutas de la subred privada que apunte a la puerta de enlace NAT
private_subnet.route_table.add_route('0.0.0.0/0', nat_gateway)

# Lanzar una instancia EC2 en la subred pública
ec2_public = EC2Instance('EC2_Public', public_subnet)

# Lanzar una instancia EC2 en la subred privada
ec2_private = EC2Instance('EC2_Private', private_subnet)

# Mostrar la configuración de la VPC
print(f"VPC CIDR: {vpc.cidr}")
print(f"Internet Gateway: {vpc.internet_gateway.name}")

# Mostrar la configuración de las subredes y sus tablas de rutas
for subnet in vpc.subnets:
    subnet_type = "Public" if subnet.is_public else "Private"
    print(f"{subnet_type} Subnet CIDR: {subnet.cidr}")  
    for route in subnet.route_table.routes:
        print(f"Route: {route['destination']} -> {route['target'].name}")

# Mostrar la configuración de las instancias EC2
print(f"EC2 Instance in Public Subnet: {ec2_public.name} in Subnet {ec2_public.subnet.cidr}")
print(f"EC2 Instance in Private Subnet: {ec2_private.name} in Subnet {ec2_private.subnet.cidr}")
