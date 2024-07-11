class LambdaFunction:
    def __init__(self, nombre, tiempo_creacion=None, tiempo_actualizacion=None, tiempo_actual=None):
        self.nombre = nombre
        self.tiempo_creacion = tiempo_creacion
        self.tiempo_actualizacion = tiempo_actualizacion
        self.tiempo_actual = tiempo_actual

    def actualizar_codigo(self, codigo_nuevo):
        self.codigo = codigo_nuevo
        self.tiempo_actualizacion = self.obtener_tiempo_actual()

    def ejecutar(self, evento):
        print(f"Ejecutando función Lambda '{self.nombre}' con evento: {evento}")
        return f"Función Lambda '{self.nombre}' ejecutada correctamente."

    def obtener_tiempo_actual(self):
        return "2024-07-12 15:30:00"  # Simulación del tiempo actual

    def __str__(self):
        return f"LambdaFunction(nombre={self.nombre}, tiempo_creacion={self.tiempo_creacion})"


class Evento:
    def __init__(self, fuente, tipo_detalle, detalle, id_unico=None, tiempo_actual=None):
        self.fuente = fuente
        self.tipo_detalle = tipo_detalle
        self.detalle = detalle
        self.id_unico = id_unico
        self.tiempo_actual = tiempo_actual

    def obtener_id_unico(self):
        return "12345678-abcd-1234-abcd-1234567890ab"  # Simulación de ID único

    def __str__(self):
        return f"Evento(fuente={self.fuente}, tipo_detalle={self.tipo_detalle})"

# Simulación de funciones Lambda y eventos

# Crear una nueva función Lambda
print("Creando una nueva función Lambda...")
funcion_lambda = LambdaFunction(nombre='MiFuncionLambda')
print(funcion_lambda)

# Actualizar el código de la función Lambda
codigo_nuevo = """
def lambda_handler(evento, contexto):
    print('Hola desde Lambda!')
    return 'Hola Mundo'
"""
funcion_lambda.actualizar_codigo(codigo_nuevo)
print(f"Actualizando código de la función Lambda '{funcion_lambda.nombre}'...")

# Ejecutar la función Lambda con un evento simulado
print("Simulando la ejecución de la función Lambda con un evento...")
evento = Evento(fuente='AWS', tipo_detalle='EventoPrueba', detalle={'clave': 'valor'})
resultado = funcion_lambda.ejecutar(evento)
print(resultado)
