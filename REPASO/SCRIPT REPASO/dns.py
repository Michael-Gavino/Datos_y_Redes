# Simulación de un DNS con registros A y CNAME
dns_records = {
    'example.com': '192.168.1.10',
    'www.example.com': 'example.com',
}

def resolve_dns(name):
    if name in dns_records:
        value = dns_records[name]
        
        # Resolver CNAME
        if value in dns_records:
            value = dns_records[value]
        
        return value
    
    return None

# Probar la resolución de DNS
print(f"IP de example.com: {resolve_dns('example.com')}")
print(f"IP de www.example.com: {resolve_dns('www.example.com')}")
