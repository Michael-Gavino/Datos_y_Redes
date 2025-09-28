class APIGateway:
    """
    Clase APIGateway
    ----------------
    Simula el comportamiento básico de un API Gateway, permitiendo la creación 
    de recursos (endpoints) y métodos HTTP asociados a dichos recursos.

    Atributos:
    ----------
    recursos : dict
        Diccionario que almacena los recursos (rutas) y sus métodos asociados.

    Métodos:
    --------
    crear_recursos(ruta):
        Crea un nuevo recurso (endpoint) en la API.

    crear_metodo(ruta, metodo):
        Asocia un método HTTP (GET, POST, PUT, DELETE, etc.) a un recurso existente.

    simulacion():
        Muestra la configuración actual del API Gateway (recursos y métodos registrados).
    """

    def __init__(self):
        """
        Constructor de la clase APIGateway.
        
        Inicializa el diccionario 'recursos' que contendrá las rutas (endpoints)
        como claves y un subdiccionario con sus métodos como valores.
        """
        self.recursos = {}  # Diccionario para almacenar recursos y métodos asociados

    def crear_recursos(self, ruta):
        """
        Crea un nuevo recurso (endpoint) en la API.

        Parámetros:
        -----------
        ruta : str
            La ruta del recurso que se desea crear (por ejemplo: "/productos").

        Retorna:
        --------
        str : Mensaje indicando que el recurso ha sido creado exitosamente.
        """
        self.recursos[ruta] = {}  # Crea un recurso con un diccionario vacío para los métodos
        return f"Recurso {ruta} creado."

    def crear_metodo(self, ruta, metodo):
        """
        Asocia un método HTTP a un recurso existente.

        Parámetros:
        -----------
        ruta : str
            Ruta del recurso al que se le quiere añadir un método.
        metodo : str
            Método HTTP que se desea asociar (GET, POST, PUT, DELETE, etc.).

        Retorna:
        --------
        str : Mensaje de éxito o error si el recurso no existe.
        """
        if ruta in self.recursos:
            # Asociar el método HTTP al recurso
            self.recursos[ruta][metodo] = f"{metodo} método para {ruta}"
            return f"Método {metodo} para {ruta} creado."
        else:
            return "Recurso no encontrado."

    def simulacion(self):
        """
        Muestra la configuración actual del API Gateway.
        
        Imprime todos los recursos creados y los métodos asociados a cada uno.
        """
        print("Recursos del API Gateway:")
        for ruta, metodos in self.recursos.items():
            print(f"  {ruta}:")
            for metodo in metodos:
                print(f"    - {metodo}: {metodos[metodo]}")


# Ejemplo de uso de la clase APIGateway
# -------------------------------------

# Crear instancia del API Gateway
api_gateway = APIGateway()

# Crear recursos (endpoints)
print(api_gateway.crear_recursos("/productos"))
print(api_gateway.crear_metodo("/productos", "GET"))
print(api_gateway.crear_metodo("/productos", "POST"))

print(api_gateway.crear_recursos("/productos/{id}"))
print(api_gateway.crear_metodo("/productos/{id}", "GET"))
print(api_gateway.crear_metodo("/productos/{id}", "PUT"))
print(api_gateway.crear_metodo("/productos/{id}", "DELETE"))

# Mostrar simulación de la configuración del API Gateway
api_gateway.simulacion()
