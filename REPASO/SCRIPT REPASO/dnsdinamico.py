# ----------------------------------------------------------
# 🌐 Simulación de un Servidor DNS en Python
# Soporta registros tipo A, CNAME y MX con una interfaz CLI
# ----------------------------------------------------------

class DNS:
    def __init__(self):
        """
        Constructor de la clase DNS.
        Inicializa un diccionario para almacenar registros de diferentes tipos:
        - A: nombre → dirección IP
        - CNAME: alias → nombre principal
        - MX: nombre → servidor de correo
        """
        self.records = {
            'A': {},       # Registros tipo A (nombre → IP)
            'CNAME': {},   # Registros tipo CNAME (alias → nombre principal)
            'MX': {}       # Registros tipo MX (nombre → servidor de correo)
        }

    def agregar_registro(self, tipo_registro, nombre, valor):
        """
        Agrega un nuevo registro DNS.

        Args:
            tipo_registro (str): Tipo de registro ('A', 'CNAME', 'MX').
            nombre (str): Nombre de dominio o alias.
            valor (str): Valor del registro (IP, nombre de dominio, servidor MX).
        """
        if tipo_registro in self.records:
            self.records[tipo_registro][nombre] = valor
            print(f"✅ Registro {tipo_registro} agregado: {nombre} → {valor}")
        else:
            print(f"❌ Tipo de registro {tipo_registro} no soportado")

    def eliminar_registro(self, tipo_registro, nombre):
        """
        Elimina un registro DNS existente.

        Args:
            tipo_registro (str): Tipo de registro a eliminar.
            nombre (str): Nombre del registro a eliminar.
        """
        if tipo_registro in self.records and nombre in self.records[tipo_registro]:
            del self.records[tipo_registro][nombre]
            print(f"🗑️ Registro {tipo_registro} eliminado: {nombre}")
        else:
            print(f"❌ Registro {nombre} no encontrado en registros de tipo {tipo_registro}")

    def actualizar_registro(self, tipo_registro, nombre, valor):
        """
        Actualiza el valor de un registro DNS existente.

        Args:
            tipo_registro (str): Tipo de registro a actualizar.
            nombre (str): Nombre del registro a actualizar.
            valor (str): Nuevo valor del registro.
        """
        if tipo_registro in self.records and nombre in self.records[tipo_registro]:
            self.records[tipo_registro][nombre] = valor
            print(f"✏️ Registro {tipo_registro} actualizado: {nombre} → {valor}")
        else:
            print(f"❌ Registro {nombre} no encontrado en registros de tipo {tipo_registro}")

    def resolver(self, nombre):
        """
        Resuelve un nombre de dominio y devuelve su valor asociado.

        Args:
            nombre (str): Nombre a resolver.

        Returns:
            str | None: Devuelve la IP (para A), el dominio final (para CNAME) o el servidor MX.
                        Si el nombre no se encuentra, devuelve None.
        """
        # Si es un registro tipo A (nombre → IP)
        if nombre in self.records['A']:
            return self.records['A'][nombre]
        # Si es un registro tipo CNAME (alias → nombre principal), se resuelve recursivamente
        elif nombre in self.records['CNAME']:
            cname = self.records['CNAME'][nombre]
            return self.resolver(cname)
        # Si es un registro tipo MX (nombre → servidor de correo)
        elif nombre in self.records['MX']:
            return self.records['MX'][nombre]
        else:
            return None  # Nombre no encontrado

    def __str__(self):
        """
        Devuelve una representación legible del estado actual de los registros DNS.
        """
        return str(self.records)


# ----------------------------------------------------------
# 🧪 Interfaz de línea de comandos (CLI) para probar el DNS
# ----------------------------------------------------------
def main():
    """
    Función principal que simula un menú interactivo en consola para gestionar registros DNS.
    Permite agregar, eliminar, actualizar y resolver registros.
    """
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
                print(f"✅ IP para {nombre}: {ip}")
            else:
                print(f"❌ {nombre} no encontrado")
        
        elif command == 'exit':
            print("👋 Saliendo del sistema DNS...")
            break
        
        else:
            print("⚠️ Comando inválido. Intente de nuevo.")


# ----------------------------------------------------------
# 🚀 Punto de entrada del programa
# ----------------------------------------------------------
if __name__ == "__main__":
    main()

