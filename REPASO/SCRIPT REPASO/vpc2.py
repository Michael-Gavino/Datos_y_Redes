# Definimos la clase 'VPC' para representar una Virtual Private Cloud
class VPC:
    # Inicializamos la VPC con un bloque CIDR
    def __init__(self, cidr):
        self.cidr = cidr  # CIDR para asignar las direcciones IP
        self.subnets = []  # Lista para almacenar las subredes

    # Método para añadir subredes a la VPC
    def add_subnet(self, cidr):
        subnet = Subnet(cidr)  # Creamos una nueva subred con el CIDR dado
        self.subnets.append(subnet)  # Añadimos la subred a la lista de subredes

# Definimos la clase 'Subnet' para representar una subred dentro de la VPC
class Subnet:
    def __init__(self, cidr):
        self.cidr = cidr  # CIDR de la subred

# Ejemplo de una clase adicional que hereda de 'Subnet'
class Nuevo(Subnet):
    def __init__(self, cidr, new_value):
        super().__init__(cidr)  # Llamamos a la clase 'Subnet'
        self.new_value = new_value  # nombrrando 'Nuevo'

# Crear una instancia de VPC con un CIDR específico
vpc = VPC('10.0.0.0/16')

# Añadir subredes a la VPC
vpc.add_subnet('10.0.1.0/24')
vpc.add_subnet('10.0.2.0/24')
vpc.add_subnet('10.0.3.0/24')

# Mostrar la configuración de la VPC
print(f"VPC CIDR: {vpc.cidr}")
for subnet in vpc.subnets:
    print(f"Subred CIDR: {subnet.cidr}")

# Ejemplo de uso de la clase 'Nuevo'
nueva_subnet = Subnet('10.0.4.0/16')
nueva_subnet = Subnet('10.0.5.0/16')
print(f"Nuevo Subred: {nueva_subnet.cidr}")
print(f"Nuevo Subred: {nueva_subnet.cidr}")
