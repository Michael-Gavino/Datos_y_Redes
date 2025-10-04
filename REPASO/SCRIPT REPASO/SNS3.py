# ------------------------------------------------------------
# Clase SNS: Simula un servicio de notificaciones basado en temas
# ------------------------------------------------------------
class SNS:
    def __init__(self):
        """
        Constructor de la clase SNS.
        Inicializa un diccionario vacío para almacenar los temas y sus endpoints suscritos.
        """
        self.topics = {}  # Estructura: {nombre_del_tema: [lista_de_endpoints]}

    def crear_tema(self, name):
        """
        Crea un nuevo tema (topic) donde se podrán publicar notificaciones.

        Parámetros:
        name (str): Nombre del tema a crear.

        Retorna:
        str: El nombre del tema creado.
        """
        self.topics[name] = []  # Crea el tema con una lista vacía de endpoints suscritos
        return name

    def suscribir(self, tema, endpoint):
        """
        Suscribe un endpoint (destinatario) a un tema específico.

        Parámetros:
        tema (str): Nombre del tema al que se desea suscribir el endpoint.
        endpoint (Endpoint): Instancia de la clase Endpoint que recibirá las notificaciones.

        Excepciones:
        - Lanza una excepción si el tema no existe.
        """
        if tema in self.topics:
            self.topics[tema].append(endpoint)  # Agrega el endpoint a la lista de suscriptores
        else:
            raise Exception("❌ Tema no existe")

    def notificar(self, tema, mensaje):
        """
        Envía un mensaje a todos los endpoints suscritos a un tema.

        Parámetros:
        tema (str): Nombre del tema al que se enviará el mensaje.
        mensaje (str): Mensaje que se enviará a los suscriptores.

        Excepciones:
        - Lanza una excepción si el tema no existe.
        """
        if tema in self.topics:
            for endpoint in self.topics[tema]:
                endpoint.notificacion(mensaje)  # Llama al método de notificación de cada endpoint
        else:
            raise Exception("❌ Tema no existe")


# ------------------------------------------------------------
# Clase Endpoint: Representa un suscriptor al sistema SNS
# ------------------------------------------------------------
class Endpoint:
    def __init__(self, name):
        """
        Constructor de la clase Endpoint.

        Parámetros:
        name (str): Nombre o tipo del endpoint (por ejemplo: 'email', 'sms').
        """
        self.name = name

    def notificacion(self, mensaje):
        """
        Recibe y muestra un mensaje de notificación.

        Parámetros:
        mensaje (str): Mensaje enviado desde un tema.
        """
        print(f"📩 Notificación a {self.name}: {mensaje}")


# ------------------------------------------------------------
# Ejemplo de uso del sistema SNS simulado
# ------------------------------------------------------------

# 1️⃣ Crear una instancia del sistema SNS
sns = SNS()

# 2️⃣ Crear endpoints simulados
email = Endpoint("Email")
sms = Endpoint("SMS")

# 3️⃣ Crear un tema
tema = sns.crear_tema("mi_tema")

# 4️⃣ Suscribir los endpoints al tema creado
sns.suscribir("mi_tema", email)
sns.suscribir("mi_tema", sms)

# 5️⃣ Enviar una notificación a todos los suscriptores del tema
sns.notificar("mi_tema", "¡Notificación importante desde el sistema SNS!")
