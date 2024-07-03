import time

# Simulación de DynamoDB
class DynamoDBSimulado:
    def __init__(self):
        self.tablas = {}

    def crear_tabla(self, nombre_tabla, esquema_clave, definiciones_atributo, rendimiento_provisionado):
        if nombre_tabla in self.tablas:
            raise Exception(f"La tabla '{nombre_tabla}' ya existe.")
        
        self.tablas[nombre_tabla] = {
            'nombre': nombre_tabla,
            'esquema_clave': esquema_clave,
            'definiciones_atributo': definiciones_atributo,
            'rendimiento_provisionado': rendimiento_provisionado,
            'items': []
        }
        print(f"Tabla '{nombre_tabla}' está siendo creada...")
        time.sleep(2)  # Simulación de tiempo de espera para la creación
        print(f"Tabla '{nombre_tabla}' creada exitosamente.")
        return self.tablas[nombre_tabla]

    def esperar_hasta_exista(self, nombre_tabla):
        if nombre_tabla not in self.tablas:
            raise Exception(f"La tabla '{nombre_tabla}' no existe.")
        
        # Simulación de espera hasta que la tabla exista
        time.sleep(2)
        print(f"La tabla '{nombre_tabla}' ahora existe.")

    def obtener_conteo_items(self, nombre_tabla):
        if nombre_tabla not in self.tablas:
            raise Exception(f"La tabla '{nombre_tabla}' no existe.")
        
        return len(self.tablas[nombre_tabla]['items'])

# Uso de la simulación de DynamoDB
dynamodb = DynamoDBSimulado()

# Crear la tabla de DynamoDB
tabla = dynamodb.crear_tabla(
    nombre_tabla='usuarios',
    esquema_clave=[
        {'nombre_atributo': 'nombre_usuario', 'tipo_clave': 'HASH'},
        {'nombre_atributo': 'apellido', 'tipo_clave': 'RANGE'}
    ],
    definiciones_atributo=[
        {'nombre_atributo': 'nombre_usuario', 'tipo_atributo': 'S'},
        {'nombre_atributo': 'apellido', 'tipo_atributo': 'S'}
    ],
    rendimiento_provisionado={'unidades_lectura': 5, 'unidades_escritura': 5}
)

# Esperar hasta que la tabla exista
dynamodb.esperar_hasta_exista('usuarios')

# Imprimir la cantidad de items en la tabla
print(f"Cantidad de items en la tabla 'usuarios': {dynamodb.obtener_conteo_items('usuarios')}")
