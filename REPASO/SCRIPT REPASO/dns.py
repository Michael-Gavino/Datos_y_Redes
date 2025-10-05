# ----------------------------------------------------------
# 🧭 Simulación básica de un DNS (Domain Name System)
# con soporte para registros tipo A y CNAME
# ----------------------------------------------------------

# Diccionario que simula una tabla de registros DNS
dns_records = {
    'example.com': '192.168.1.10',     # Registro A: dominio → dirección IP
    'www.example.com': 'example.com',  # Registro CNAME: alias → dominio principal
}


def resolve_dns(name):
    """
    Resuelve un nombre de dominio consultando los registros DNS simulados.
    Soporta registros A y CNAME.

    Args:
        name (str): Nombre de dominio que se quiere resolver (por ejemplo, 'example.com').

    Returns:
        str | None: Devuelve la dirección IP asociada al nombre, o None si no se encuentra.
    """
    
    # Verificar si el nombre existe en los registros DNS
    if name in dns_records:
        value = dns_records[name]  # Obtener el valor asociado al nombre
        
        # Si el valor también es un nombre de dominio presente en los registros,
        # significa que estamos ante un registro CNAME. Lo resolvemos recursivamente.
        if value in dns_records:
            value = dns_records[value]
        
        return value  # Retorna la dirección IP final
    
    # Si el nombre no está en los registros, retornar None
    return None


# ----------------------------------------------------------
# 🧪 Pruebas de resolución DNS
# ----------------------------------------------------------

# Consultar la dirección IP del dominio principal
print(f"IP de example.com: {resolve_dns('example.com')}")

# Consultar la dirección IP de un alias (CNAME) que apunta al dominio principal
print(f"IP de www.example.com: {resolve_dns('www.example.com')}")
