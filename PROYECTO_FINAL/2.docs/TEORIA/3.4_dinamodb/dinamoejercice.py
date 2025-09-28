from datetime import datetime

class TablaSimuladaDynamoDB:
    """
    Clase TablaSimuladaDynamoDB
    ---------------------------
    Simula el comportamiento de una tabla en Amazon DynamoDB.

    Atributos:
    ----------
    nombre_tabla : str
        Nombre de la tabla simulada.
    fecha_hora_creacion : datetime
        Fecha y hora en que se "creó" la tabla simulada.

    Métodos:
    --------
    cargar():
        Simula la carga de los detalles de la tabla.
    """

    def __init__(self, nombre_tabla):
        """
        Constructor de la clase TablaSimuladaDynamoDB.

        Parámetros:
        -----------
        nombre_tabla : str
            Nombre de la tabla que se desea simular.
        """
        self.nombre_tabla = nombre_tabla
        self.fecha_hora_creacion = datetime.now()  # Guarda la fecha y hora actual como creación de la tabla

    def cargar(self):
        """
        Simula la carga de los detalles de la tabla desde DynamoDB.
        En un entorno real, este método obtendría información desde AWS.
        """
        print(f"Cargando detalles para la tabla '{self.nombre_tabla}'...")


class RecursoSimuladoDynamoDB:
    """
    Clase RecursoSimuladoDynamoDB
    -----------------------------
    Simula el recurso global de DynamoDB, que permite acceder a las tablas.

    Métodos:
    --------
    Table(nombre_tabla):
        Devuelve una instancia de TablaSimuladaDynamoDB asociada a la tabla especificada.
    """

    def Table(self, nombre_tabla):
        """
        Devuelve un objeto que representa una tabla de DynamoDB simulada.

        Parámetros:
        -----------
        nombre_tabla : str
            Nombre de la tabla a la que se desea acceder.

        Retorna:
        --------
        TablaSimuladaDynamoDB:
            Objeto que representa la tabla especificada.
        """
        return TablaSimuladaDynamoDB(nombre_tabla)


# -----------------------------------------------------------
# Simulación del uso de DynamoDB con clases simuladas
# -----------------------------------------------------------

# Simula obtener el recurso de DynamoDB (como boto3.resource('dynamodb'))
dynamodb = RecursoSimuladoDynamoDB()

# Crea una instancia de una tabla simulada llamada 'usuarios'
tabla = dynamodb.Table('usuarios')

# Simula la carga de la tabla (por ejemplo, para acceder a sus propiedades)
tabla.cargar()

# Imprime detalles de la tabla simulada
print(f"Fecha y hora de creación de la tabla '{tabla.nombre_tabla}': {tabla.fecha_hora_creacion}")

