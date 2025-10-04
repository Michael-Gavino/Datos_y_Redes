import time

# ===============================================
# Clase EFS (Elastic File System)
# ===============================================
class EFS:
    def __init__(self, nombre):
        """
        Constructor de la clase EFS.
        Representa un sistema de archivos elástico (similar a Amazon EFS).

        :param nombre: Nombre del sistema de archivos EFS.
        """
        self.nombre = nombre  # Nombre identificador del sistema de archivos
        self.archivos = {}    # Diccionario que simula los archivos almacenados en EFS

    def crear_archivo(self, nombre_archivo):
        """
        Crea un nuevo archivo vacío dentro del sistema de archivos EFS.

        :param nombre_archivo: Nombre del archivo a crear.
        """
        if nombre_archivo not in self.archivos:
            self.archivos[nombre_archivo] = ""  # Inicializa el archivo vacío
            print(f"Archivo '{nombre_archivo}' creado en EFS '{self.nombre}'")

    def eliminar_archivo(self, nombre_archivo):
        """
        Elimina un archivo del sistema de archivos EFS.

        :param nombre_archivo: Nombre del archivo a eliminar.
        """
        if nombre_archivo in self.archivos:
            del self.archivos[nombre_archivo]
            print(f"Archivo '{nombre_archivo}' eliminado de EFS '{self.nombre}'")

    def leer_archivo(self, nombre_archivo):
        """
        Lee el contenido de un archivo en el sistema EFS.

        :param nombre_archivo: Nombre del archivo a leer.
        :return: Contenido del archivo o None si no existe.
        """
        if nombre_archivo in self.archivos:
            return self.archivos[nombre_archivo]
        else:
            print(f"Archivo '{nombre_archivo}' no encontrado en EFS '{self.nombre}'")
            return None

    def escribir_archivo(self, nombre_archivo, datos):
        """
        Escribe o actualiza el contenido de un archivo en el sistema EFS.

        :param nombre_archivo: Nombre del archivo.
        :param datos: Contenido que se desea escribir.
        """
        if nombre_archivo in self.archivos:
            self.archivos[nombre_archivo] = datos
            print(f"Archivo '{nombre_archivo}' actualizado en EFS '{self.nombre}'")
        else:
            print(f"Archivo '{nombre_archivo}' no encontrado en EFS '{self.nombre}'. No se pudo actualizar.")


# ===============================================
# Clase InstanciaEC2 (Simula una instancia de cómputo EC2)
# ===============================================
class InstanciaEC2:
    def __init__(self, id_instancia):
        """
        Constructor de la clase InstanciaEC2.
        Representa una instancia de cómputo que puede montar un sistema de archivos EFS.

        :param id_instancia: ID único que identifica la instancia EC2.
        """
        self.id_instancia = id_instancia
        self.sistema_archivos_montado = None  # Aquí se almacenará la referencia al EFS montado

    def montar_sistema_archivos(self, nombre_efs):
        """
        Monta un sistema de archivos EFS en la instancia EC2.

        :param nombre_efs: Nombre del sistema de archivos EFS a montar.
        """
        if self.sistema_archivos_montado is None:
            self.sistema_archivos_montado = EFS(nombre_efs)
            print(f"Sistema de archivos EFS '{nombre_efs}' montado en la instancia '{self.id_instancia}'")
        else:
            print(f"El sistema de archivos EFS ya está montado en la instancia '{self.id_instancia}'")

    def desmontar_sistema_archivos(self):
        """
        Desmonta el sistema de archivos EFS de la instancia EC2.
        """
        if self.sistema_archivos_montado is not None:
            self.sistema_archivos_montado = None
            print(f"Sistema de archivos EFS desmontado de la instancia '{self.id_instancia}'")
        else:
            print(f"No hay sistema de archivos EFS montado en la instancia '{self.id_instancia}'")

    def leer_archivo(self, nombre_archivo):
        """
        Lee un archivo desde el sistema de archivos montado.

        :param nombre_archivo: Nombre del archivo que se desea leer.
        :return: Contenido del archivo o None si no existe.
        """
        if self.sistema_archivos_montado:
            return self.sistema_archivos_montado.leer_archivo(nombre_archivo)
        else:
            print(f"No hay sistema de archivos EFS montado en la instancia '{self.id_instancia}'")
            return None

    def escribir_archivo(self, nombre_archivo, datos):
        """
        Escribe o actualiza el contenido de un archivo en el sistema EFS montado.

        :param nombre_archivo: Nombre del archivo.
        :param datos: Contenido a escribir en el archivo.
        """
        if self.sistema_archivos_montado:
            self.sistema_archivos_montado.escribir_archivo(nombre_archivo, datos)
        else:
            print(f"No hay sistema de archivos EFS montado en la instancia '{self.id_instancia}'. No se pudo escribir el archivo.")

    def eliminar_archivo(self, nombre_archivo):
        """
        Elimina un archivo del sistema de archivos montado.

        :param nombre_archivo: Nombre del archivo a eliminar.
        """
        if self.sistema_archivos_montado:
            self.sistema_archivos_montado.eliminar_archivo(nombre_archivo)
        else:
            print(f"No hay sistema de archivos EFS montado en la instancia '{self.id_instancia}'. No se pudo eliminar el archivo.")


# ===============================================
# Función para simular operaciones en el sistema de archivos EFS
# ===============================================
def simular_operaciones(nombre_efs, id_instancia):
    """
    Simula el uso de un sistema EFS desde una instancia EC2.

    1. Monta el sistema de archivos.
    2. Escribe archivos.
    3. Lee el contenido de los archivos.
    4. Desmonta el sistema de archivos.

    :param nombre_efs: Nombre del sistema de archivos EFS.
    :param id_instancia: ID de la instancia EC2.
    """
    instancia = InstanciaEC2(id_instancia)              # Crear la instancia EC2
    instancia.montar_sistema_archivos(nombre_efs)       # Montar el sistema EFS
    
    # Intentar escribir archivos (nota: si no existen previamente, mostrará advertencia)
    instancia.escribir_archivo("archivo1.txt", "Contenido del archivo 1")
    time.sleep(2)  # Simula tiempo de procesamiento
    instancia.escribir_archivo("archivo2.txt", "Contenido del archivo 2")

    # Leer archivos creados
    print(f"\nLeyendo archivos desde la instancia '{id_instancia}':")
    print(instancia.leer_archivo("archivo1.txt"))
    print(instancia.leer_archivo("archivo2.txt"))

    # Desmontar el sistema de archivos
    instancia.desmontar_sistema_archivos()


# ===============================================
# Ejecución del programa principal
# ===============================================
if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Aquí se ejecuta la simulación del uso del sistema de archivos EFS
    desde una instancia EC2 específica.
    """
    simular_operaciones("EFS1", "i-1234567890abcdef0")

