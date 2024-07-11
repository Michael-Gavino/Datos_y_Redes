class DNS:
    def __init__(self):
        self.records = {
            'A': {},
            'CNAME': {},
            'MX': {}
        }

    def agregar_registro(self, tipo_registro, nombre, valor):
        if tipo_registro in self.records:
            self.records[tipo_registro][nombre] = valor
        else:
            print(f"Tipo de registro {tipo_registro} no soportado")

    def eliminar_registro(self, tipo_registro, nombre):
        if tipo_registro in self.records and nombre in self.records[tipo_registro]:
            del self.records[tipo_registro][nombre]
        else:
            print(f"Registro {nombre} no encontrado en registros de {tipo_registro}")

    def actualizar_registro(self, tipo_registro, nombre, valor):
        if tipo_registro in self.records and nombre in self.records[tipo_registro]:
            self.records[tipo_registro][nombre] = valor
        else:
            print(f"Registro {nombre} no encontrado en registros de {tipo_registro}")

    def resolver(self, nombre):
        if nombre in self.records['A']:
            return self.records['A'][nombre]
        elif nombre in self.records['CNAME']:
            cname = self.records['CNAME'][nombre]
            return self.resolver(cname)
        elif nombre in self.records['MX']:
            return self.records['MX'][nombre]
        else:
            return None

    def __str__(self):
        return str(self.records)

# Simulación de la interfaz de línea de comandos (CLI)
def main():
    dns = DNS()
    while True:
        command = input("Ingrese el comando (add, delete, update, resolve, exit): ")
        if command == 'add':
            tipo_registro = input("Ingrese el tipo de registro (A, CNAME, MX): ")
            nombre = input("Ingrese el nombre: ")
            valor = input("Ingrese el valor: ")
            dns.agregar_registro(tipo_registro, nombre, valor)
        elif command == 'delete':
            tipo_registro = input("Ingrese el tipo de registro (A, CNAME, MX): ")
            nombre = input("Ingrese el nombre: ")
            dns.eliminar_registro(tipo_registro, nombre)
        elif command == 'update':
            tipo_registro = input("Ingrese el tipo de registro (A, CNAME, MX): ")
            nombre = input("Ingrese el nombre: ")
            valor = input("Ingrese el nuevo valor: ")
            dns.actualizar_registro(tipo_registro, nombre, valor)
        elif command == 'resolve':
            nombre = input("Ingrese el nombre a resolver: ")
            ip = dns.resolver(nombre)
            if ip:
                print(f"IP para {nombre} es {ip}")
            else:
                print(f"{nombre} no encontrado")
        elif command == 'exit':
            break
        else:
            print("Comando inválido")

if __name__ == "__main__":
    main()
