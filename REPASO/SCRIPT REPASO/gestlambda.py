# ----------------------------------------------------------
# 🪄 Simulación de AWS Lambda y Eventos en Python
# Permite crear funciones Lambda, actualizar su código,
# ejecutarlas con eventos simulados y manejar sus metadatos.
# ----------------------------------------------------------

class LambdaFunction:
    """
    Representa una función Lambda simulada en un entorno similar a AWS Lambda.

    Atributos:
        nombre (str): Nombre de la función Lambda.
        tiempo_creacion (str): Fecha y hora de creación de la función.
        tiempo_actualizacion (str): Última fecha y hora de actualización del código.
        tiempo_actual (str): Tiempo actual del sistema (simulado).
        codigo (str): Código fuente de la función Lambda.
    """

    def __init__(self, nombre, tiempo_creacion=None, tiempo_actualizacion=None, tiempo_actual=None):
        """
        Inicializa una nueva función Lambda.

        Args:
            nombre (str): Nombre asignado a la función Lambda.
            tiempo_creacion (str, opcional): Fecha y hora de creación.
            tiempo_actualizacion (str, opcional): Última actualización del código.
            tiempo_actual (str, opcional): Tiempo actual del sistema.
        """
        self.nombre = nombre
        self.tiempo_creacion = tiempo_creacion
        self.tiempo_actualizacion = tiempo_actualizacion
        self.tiempo_actual = tiempo_actual
        self.codigo = None  # Código inicial vacío

    def actualizar_codigo(self, codigo_nuevo):
        """
        Actualiza el código fuente de la función Lambda.

        Args:
            codigo_nuevo (str): Nuevo código fuente de la función Lambda.
        """
        self.codigo = codigo_nuevo
        self.tiempo_actualizacion = self.obtener_tiempo_actual()
        print(f"✏️ Código de la función Lambda '{self.nombre}' actualizado correctamente.")

    def ejecutar(self, evento):
        """
        Ejecuta la función Lambda con un evento simulado.

        Args:
            evento (Evento): Evento que dispara la ejecución de la función.

        Returns:
            str: Mensaje indicando que la función fue ejecutada exitosamente.
        """
        print(f"🚀 Ejecutando función Lambda '{self.nombre}' con evento: {evento}")
        return f"✅ Función Lambda '{self.nombre}' ejecutada correctamente."

    def obtener_tiempo_actual(self):
        """
        Obtiene la hora y fecha actual del sistema (simulada).

        Returns:
            str: Fecha y hora actuales en formato 'YYYY-MM-DD HH:MM:SS'.
        """
        return "2024-07-12 15:30:00"  # 🕒 Simulación del tiempo actual

    def __str__(self):
        """
        Devuelve una representación legible de la función Lambda.

        Returns:
            str: Representación en texto del objeto LambdaFunction.
        """
        return f"LambdaFunction(nombre={self.nombre}, tiempo_creacion={self.tiempo_creacion})"


# ----------------------------------------------------------
# 📦 Clase Evento: Representa un evento que activa funciones Lambda
# ----------------------------------------------------------
class Evento:
    """
    Representa un evento que puede activar una función Lambda.

    Atributos:
        fuente (str): Fuente del evento (por ejemplo, 'AWS', 'S3', etc.).
        tipo_detalle (str): Tipo de detalle del evento.
        detalle (dict): Información adicional del evento.
        id_unico (str): Identificador único del evento.
        tiempo_actual (str): Tiempo actual del evento.
    """

    def __init__(self, fuente, tipo_detalle, detalle, id_unico=None, tiempo_actual=None):
        """
        Inicializa un evento con sus atributos principales.

        Args:
            fuente (str): Fuente del evento.
            tipo_detalle (str): Tipo de detalle del evento.
            detalle (dict): Información detallada del evento.
            id_unico (str, opcional): ID único del evento.
            tiempo_actual (str, opcional): Tiempo del evento.
        """
        self.fuente = fuente
        self.tipo_detalle = tipo_detalle
        self.detalle = detalle
        self.id_unico = id_unico
        self.tiempo_actual = tiempo_actual

    def obtener_id_unico(self):
        """
        Genera un identificador único simulado para el evento.

        Returns:
            str: ID único del evento.
        """
        return "12345678-abcd-1234-abcd-1234567890ab"

    def __str__(self):
        """
        Devuelve una representación legible del evento.

        Returns:
            str: Representación en texto del objeto Evento.
        """
        return f"Evento(fuente={self.fuente}, tipo_detalle={self.tipo_detalle})"


# ----------------------------------------------------------
# 🧪 Simulación del flujo completo de AWS Lambda y eventos
# ----------------------------------------------------------
if __name__ == "__main__":
    # Crear una nueva función Lambda
    print("📦 Creando una nueva función Lambda...")
    funcion_lambda = LambdaFunction(nombre='MiFuncionLambda')
    print(funcion_lambda)

    # Actualizar el código de la función Lambda
    codigo_nuevo = """
def lambda_handler(evento, contexto):
    print('Hola desde Lambda!')
    return 'Hola Mundo'
"""
    print(f"✏️ Actualizando código de la función Lambda '{funcion_lambda.nombre}'...")
    funcion_lambda.actualizar_codigo(codigo_nuevo)

    # Simular la ejecución de la función Lambda con un evento
    print("🚀 Simulando la ejecución de la función Lambda con un evento...")
    evento = Evento(fuente='AWS', tipo_detalle='EventoPrueba', detalle={'clave': 'valor'})
    resultado = funcion_lambda.ejecutar(evento)
    print(resultado)

