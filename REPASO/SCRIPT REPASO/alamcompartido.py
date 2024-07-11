import time

# Clase para representar el sistema de archivos EFS
class EFS:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos = {}

    def crear_archivo(self, nombre_archivo):
        if nombre_archivo not in self.archivos:
            self.archivos[nombre_archivo] = ""
            print(f"Archivo '{nombre_archivo}' creado en EFS '{self.nombre}'")

    def eliminar_archivo(self, nombre_archivo):
        if nombre_archivo in self.archivos:
            del self.archivos[nombre_archivo]
            print(f"Archivo '{nombre_archivo}' eliminado de EFS '{self.nombre}'")

    def leer_archivo(self, nombre_archivo):
        if nombre_archivo in self.archivos:
            return self.archivos[nombre_archivo]
        else:
            print(f"Archivo '{nombre_archivo}' no encontrado en EFS '{self.nombre}'")
            return None

    def escribir_archivo(self, nombre_archivo, datos):
        if nombre_archivo in self.archivos:
            self.archivos[nombre_archivo] = datos
            print(f"Archivo '{nombre_archivo}' actualizado en EFS '{self.nombre}'")
        else:
            print(f"Archivo '{nombre_archivo}' no encontrado en EFS '{self.nombre}'. No se pudo actualizar.")

# Clase para representar una instancia EC2
class InstanciaEC2:
    def __init__(self, id_instancia):
        self.id_instancia = id_instancia
        self.sistema_archivos_montado = None

    def montar_sistema_archivos(self, nombre_efs):
        if self.sistema_archivos_montado is None:
            self.sistema_archivos_montado = EFS(nombre_efs)
            print(f"Sistema de archivos EFS '{nombre_efs}' montado en la instancia '{self.id_instancia}'")
        else:
            print(f"El sistema de archivos EFS ya está montado en la instancia '{self.id_instancia}'")

    def desmontar_sistema_archivos(self):
        if self.sistema_archivos_montado is not None:
            self.sistema_archivos_montado = None
            print(f"Sistema de archivos EFS desmontado de la instancia '{self.id_instancia}'")
        else:
            print(f"No hay sistema de archivos EFS montado en la instancia '{self.id_instancia}'")

    def leer_archivo(self, nombre_archivo):
        if self.sistema_archivos_montado:
            return self.sistema_archivos_montado.leer_archivo(nombre_archivo)
        else:
            print(f"No hay sistema de archivos EFS montado en la instancia '{self.id_instancia}'")
            return None

    def escribir_archivo(self, nombre_archivo, datos):
        if self.sistema_archivos_montado:
            self.sistema_archivos_montado.escribir_archivo(nombre_archivo, datos)
        else:
            print(f"No hay sistema de archivos EFS montado en la instancia '{self.id_instancia}'. No se pudo escribir el archivo.")

    def eliminar_archivo(self, nombre_archivo):
        if self.sistema_archivos_montado:
            self.sistema_archivos_montado.eliminar_archivo(nombre_archivo)
        else:
            print(f"No hay sistema de archivos EFS montado en la instancia '{self.id_instancia}'. No se pudo eliminar el archivo.")

# Función para simular operaciones en el sistema de archivos EFS
def simular_operaciones(nombre_efs, id_instancia):
    instancia = InstanciaEC2(id_instancia)
    instancia.montar_sistema_archivos(nombre_efs)
    
    instancia.escribir_archivo("archivo1.txt", "Contenido del archivo 1")
    time.sleep(2)  # Simular una operación de espera
    instancia.escribir_archivo("archivo2.txt", "Contenido del archivo 2")

    print(f"\nLeyendo archivos desde la instancia '{id_instancia}':")
    print(instancia.leer_archivo("archivo1.txt"))
    print(instancia.leer_archivo("archivo2.txt"))

    instancia.desmontar_sistema_archivos()

# Ejemplo de uso
if __name__ == "__main__":
    # Simulación de operaciones con un sistema de archivos EFS llamado 'EFS1' en la instancia 'i-1234567890abcdef0'
    simular_operaciones("EFS1", "i-1234567890abcdef0")
