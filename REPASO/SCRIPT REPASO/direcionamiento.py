# ----------------------------------------------------------
# Generador de direcciones IP a partir de un rango CIDR
# ----------------------------------------------------------

# Definir el rango CIDR de la red
cidr = '192.168.1.0/24'
# CIDR (Classless Inter-Domain Routing) define la dirección base de la red
# y la cantidad de bits usados para la parte de red.
# Ejemplo: '192.168.1.0/24' → 24 bits para red, 8 bits para hosts.


def get_ip_addresses(cidr):
    """
    Genera una lista de direcciones IP disponibles dentro de un rango CIDR.

    Args:
        cidr (str): Rango CIDR en formato 'X.X.X.X/NN' (por ejemplo, '192.168.1.0/24').

    Returns:
        list: Lista de direcciones IP dentro del rango especificado (excluyendo la dirección de red y broadcast).
    """

    # 1️⃣ Dividir el rango CIDR en la dirección base y la máscara de subred
    parts = cidr.split('/')      # Ejemplo: ['192.168.1.0', '24']
    base_ip = parts[0]           # Dirección base de la red: '192.168.1.0'
    subnet_mask = int(parts[1])  # Longitud de la máscara de red: 24

    # 2️⃣ Calcular el número total de direcciones IP posibles
    # Fórmula: 2^(32 - máscara)
    num_hosts = 2 ** (32 - subnet_mask)
    # Ejemplo: 2^(32 - 24) = 2^8 = 256 direcciones totales

    # 3️⃣ Generar todas las direcciones IP posibles dentro del rango
    ip_addresses = []

    # Excluimos la primera (dirección de red) y la última (broadcast)
    for i in range(1, num_hosts - 1):
        # rsplit('.', 1) separa la dirección base en dos partes:
        # '192.168.1' y '0'. Luego reemplazamos el último octeto por el número i
        ip = base_ip.rsplit('.', 1)[0] + '.' + str(i)
        ip_addresses.append(ip)

    return ip_addresses


# ----------------------------------------------------------
# Mostrar todas las direcciones IP dentro del rango
# ----------------------------------------------------------

print(f"📡 Rango de direcciones IP para {cidr}:")

# Llamar a la función y recorrer la lista de IPs generadas
for ip in get_ip_addresses(cidr):
    print(ip)
