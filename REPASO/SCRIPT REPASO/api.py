# ===============================================
# Clase Flask (Simulación simplificada del framework Flask)
# ===============================================
class Flask:
    def __init__(self, nombre):
        """
        Constructor de la clase Flask.
        Simula una aplicación web básica tipo Flask, gestionando rutas y controladores.

        :param nombre: Nombre de la aplicación.
        """
        self.nombre = nombre     # Nombre de la aplicación
        self.rutas = {}          # Diccionario para almacenar rutas y sus controladores asociados

    def agregar_ruta(self, ruta, metodos, controlador):
        """
        Registra una nueva ruta en la aplicación, junto con sus métodos HTTP y su controlador.

        :param ruta: La ruta (endpoint) de la API (ejemplo: '/recursos/<resource_id>').
        :param metodos: Lista de métodos HTTP permitidos (GET, POST, PUT, DELETE).
        :param controlador: Función que se ejecuta cuando se accede a la ruta con un método válido.
        """
        self.rutas[ruta] = {'metodos': metodos, 'controlador': controlador}

    def ejecutar(self, debug=False):
        """
        Simula la ejecución de la aplicación Flask en modo interactivo por consola.
        Permite al usuario ingresar rutas y métodos manualmente para probar la API.

        :param debug: Si está en True, muestra información adicional (modo depuración).
        """
        print(f"Ejecutando la aplicación Flask {self.nombre}...")
        while True:
            try:
                # Solicita al usuario ingresar la ruta y el método HTTP
                ruta = input("Ingrese la ruta (por ejemplo, /recursos/1): ")
                metodo = input("Ingrese el método (GET, POST, PUT, DELETE): ").upper()

                # Verifica si la ruta existe y si el método es válido
                if ruta in self.rutas and metodo in self.rutas[ruta]['metodos']:
                    self.rutas[ruta]['controlador'](ruta)  # Ejecuta el controlador correspondiente
                else:
                    print("Ruta o método no encontrados. Por favor, verifique su entrada.")
            except KeyError:
                print("Ruta no encontrada. Por favor, verifique la ruta y el método.")


# ===============================================
# Inicialización de la aplicación
# ===============================================
app = Flask(__name__)   # Crea una instancia de la aplicación Flask

# Diccionario en memoria para almacenar recursos creados
recursos = {}


# ===============================================
# Controladores para manejar operaciones CRUD
# ===============================================

def crear_recurso(ruta):
    """
    Controlador para crear un nuevo recurso.
    Solicita al usuario un ID y datos, y los almacena en el diccionario 'recursos'.
    """
    resource_id = input("Ingrese el ID del recurso: ")
    resource_data = input("Ingrese los datos del recurso: ")
    recursos[resource_id] = resource_data
    print({"message": "Recurso creado"})


def obtener_recurso(ruta):
    """
    Controlador para obtener un recurso específico.
    Extrae el ID de la ruta y devuelve sus datos si existe.
    """
    resource_id = ruta.split('/')[-1]             # Obtiene el ID desde la ruta ingresada
    resource_data = recursos.get(resource_id)     # Busca el recurso en el diccionario
    if resource_data:
        print({"id": resource_id, "data": resource_data})
    else:
        print({"message": "Recurso no encontrado"})


def actualizar_recurso(ruta):
    """
    Controlador para actualizar un recurso existente.
    Si el recurso existe, permite cambiar sus datos.
    """
    resource_id = ruta.split('/')[-1]
    resource_data = input("Ingrese los datos actualizados del recurso: ")
    if resource_id in recursos:
        recursos[resource_id] = resource_data
        print({"message": "Recurso actualizado"})
    else:
        print({"message": "Recurso no encontrado"})


def eliminar_recurso(ruta):
    """
    Controlador para eliminar un recurso existente.
    Si el recurso está en el diccionario, se elimina.
    """
    resource_id = ruta.split('/')[-1]
    if resource_id in recursos:
        del recursos[resource_id]
        print({"message": "Recurso eliminado"})
    else:
        print({"message": "Recurso no encontrado"})


# ===============================================
# Registro de rutas y métodos permitidos
# ===============================================
# Agrega cada ruta con su método HTTP y su controlador asociado

# Crear recurso (POST)
app.agregar_ruta('/recursos', ['POST'], crear_recurso)

# Obtener recurso (GET)
app.agregar_ruta('/recursos/<resource_id>', ['GET'], obtener_recurso)

# Actualizar recurso (PUT)
app.agregar_ruta('/recursos/<resource_id>', ['PUT'], actualizar_recurso)

# Eliminar recurso (DELETE)
app.agregar_ruta('/recursos/<resource_id>', ['DELETE'], eliminar_recurso)


# ===============================================
# Ejecución del servidor simulado
# ===============================================
if __name__ == '__main__':
    """
    Punto de entrada principal del programa.
    Inicia la ejecución del servidor Flask simulado.
    """
    app.ejecutar(debug=True)
