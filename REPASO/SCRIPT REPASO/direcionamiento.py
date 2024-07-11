# Rango CIDR
cidr = '192.168.1.0/24'

# Función para obtener la lista de direcciones IP
def get_ip_addresses(cidr):
    # Parsear el CIDR
    parts = cidr.split('/')
    base_ip = parts[0]
    subnet_mask = int(parts[1])
    
    # Calcular el número de hosts
    num_hosts = 2 ** (32 - subnet_mask)
    
    # Obtener las direcciones IP dentro del rango
    ip_addresses = []
    for i in range(1, num_hosts - 1):
        ip = base_ip.rsplit('.', 1)[0] + '.' + str(i)
        ip_addresses.append(ip)
    
    return ip_addresses

# Mostrar todas las direcciones IP en la red
print(f"Rango de direcciones IP para {cidr}:")
for ip in get_ip_addresses(cidr):
    print(ip)
