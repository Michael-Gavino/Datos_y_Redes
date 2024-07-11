# Definición de la clase Subnet
class Subnet:
    def __init__(self, cidr):
        self.cidr = cidr

# Definición de la clase VPC que contiene subredes
class VPC:
    def __init__(self, cidr):
        self.cidr = cidr
        self.subnets = []

    def add_subnet(self, cidr):
        subnet = Subnet(cidr)
        self.subnets.append(subnet)

# Crear una VPC
vpc = VPC('10.0.0.0/16')

# Añadir subredes a la VPC
vpc.add_subnet('10.0.1.0/24')
vpc.add_subnet('10.0.2.0/24')

# Mostrar la configuración de la VPC y sus subredes
print(f"VPC CIDR: {vpc.cidr}")
for subnet in vpc.subnets:
    print(f"Subred CIDR: {subnet.cidr}")
