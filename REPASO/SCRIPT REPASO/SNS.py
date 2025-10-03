# ------------------------------------------------------------
# Clase SNS: Simula un sistema de notificaciones por temas (topics)
# ------------------------------------------------------------
class SNS:
    def __init__(self):
        """
        Constructor de la clase SNS.
        Inicializa un diccionario vacío que almacenará los temas creados
        y sus endpoints (suscriptores).
        """
        self.topics = {}  # Diccionario con el formato: {nombre_del_topic: [lista_de_endpoints]}

    def create_topic(self, name):
        """
        Crea un nuevo tema (topic) para publicar mensajes.

        Parámetros:
        name (str): Nombre del tema que se va a crear.

        Retorna:
        str: El nombre del tema creado.
        """
        self.topics[name] = []  # Inicializa la lista de suscriptores vacía para ese tema
        return name

    def subscribe(self, topic, endpoint):
        """
        Suscribe un endpoint (destinatario) a un tema específico.

        Parámetros:
        topic (str): Nombre del tema al que se suscribirá el endpoint.
        endpoint (Endpoint): Instancia de la clase Endpoint que recibirá notificaciones.

        Excepciones:
        - Lanza una excepción si el tema no existe.
        """
        if topic in self.topics:
            self.topics[topic].append(endpoint)  # Agrega el endpoint a la lista de suscriptores
        else:
            raise Exception("El tema no existe")

    def publish(self, topic, message):
        """
        Publica un mensaje en un tema y lo envía a todos los endpoints suscritos.

        Parámetros:
        topic (str): Nombre del tema donde se publicará el mensaje.
        message (str): Mensaje que se enviará a todos los suscriptores.

        Excepciones:
        - Lanza una excepción si el tema no existe.
        """
        if topic in self.topics:
            # Enviar el mensaje a cada endpoint suscrito
            for endpoint in self.topics[topic]:
                endpoint.notify(message)
        else:
            raise Exception("El tema no existe")


# ------------------------------------------------------------
# Clase Endpoint: Representa un punto de notificación (destinatario)
# ------------------------------------------------------------
class Endpoint:
    def __init__(self, name):
        """
        Constructor de la clase Endpoint.
        Representa un suscriptor que puede recibir notificaciones.

        Parámetros:
        name (str): Nombre identificador del endpoint (por ejemplo, 'Email', 'SMS').
        """
        self.name = name

    def notify(self, message):
        """
        Método para recibir una notificación.

        Parámetros:
        message (str): Mensaje que se envía al endpoint.
        """
        print(f"📨 Notificación a {self.name}: {message}")


# ------------------------------------------------------------
# Ejemplo de uso del sistema SNS
# ------------------------------------------------------------

# 1️⃣ Crear una instancia del sistema SNS
sns = SNS()

# 2️⃣ Crear endpoints que recibirán las notificaciones
email = Endpoint("Email")
sms = Endpoint("SMS")

# 3️⃣ Crear un tema (topic) donde se publicarán los mensajes
topic = sns.create_topic("MyTopic")

# 4️⃣ Suscribir los endpoints al tema creado
sns.subscribe(topic, email)
sns.subscribe(topic, sms)

# 5️⃣ Publicar un mensaje que será enviado a todos los suscriptores
sns.publish(topic, "Hello, world!")
