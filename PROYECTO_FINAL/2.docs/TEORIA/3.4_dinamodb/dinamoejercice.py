from datetime import datetime

class TablaSimuladaDynamoDB:
    def __init__(self, nombre_tabla):
        self.nombre_tabla = nombre_tabla
        self.fecha_hora_creacion = datetime.now()

    def cargar(self):
        # Simula la carga de los detalles de la tabla
        print(f"Cargando detalles para la tabla {self.nombre_tabla}...")

# Simula el recurso de DynamoDB
class RecursoSimuladoDynamoDB:
    def Table(self, nombre_tabla):
        return TablaSimuladaDynamoDB(nombre_tabla)

# Simula obtener el recurso de DynamoDB
dynamodb = RecursoSimuladoDynamoDB()

# Instancia un objeto de recurso de la tabla
tabla = dynamodb.Table('usuarios')

# Carga la tabla para simular el acceso a sus atributos
tabla.cargar()

# Imprime algunos datos sobre la tabla
print(f"Fecha y hora de creación de la tabla '{tabla.nombre_tabla}': {tabla.fecha_hora_creacion}")

