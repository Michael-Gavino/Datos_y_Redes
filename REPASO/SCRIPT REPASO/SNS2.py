# ------------------------------------------------------------
# Clase SNS: Sistema de notificaciones por temas (topics)
# ------------------------------------------------------------
class SNS:
    def __init__(self):
        """
        Constructor de la clase SNS.
        Inicializa un diccionario vacío para almacenar los temas y sus endpoints suscritos.
        """
        self.topics = {}  # Diccionario: {nombre_del_topic: [lista_de_endpoints]}

    def create_topic(self, name):
        """
        Crea un nuevo tema (topic) donde se podrán publicar mensajes.

        Parámetros:
        name (str): Nombre del tema a crear.

        Retorna:
        str: Nombre del tema creado.
        """
        self.topics[name] = []  # Inicializa la lista de suscriptores vacía
        return name

    def subscribe(self, topic, endpoint):
        """
        Suscribe un endpoint a un tema específico.

        Parámetros:
        topic (str): Nombre del tema.
        endpoint (SNSEndpoint): Instancia de SNSEndpoint que recibirá notificaciones.

        Excepciones:
        - Lanza una excepción si el tema no existe.
        """
        if topic in self.topics:
            self.topics[topic].append(endpoint)  # Añade el endpoint a la lista de suscriptores
        else:
            raise Exception("El tema no existe")

    def unsubscribe(self, topic, endpoint):
        """
        Elimina un endpoint de la lista de suscriptores de un tema.

        Parámetros:
        topic (str): Nombre del tema.
        endpoint (SNSEndpoint): Instancia de SNSEndpoint que se desea eliminar.

        Excepciones:
        - Lanza una excepción si el tema no existe.
        """
        if topic in self.topics:
            self.topics[topic].remove(endpoint)  # Quita el endpoint de la lista
        else:
            raise Exception("El tema no existe")

    def publish(self, topic, message):
        """
        Publica un mensaje en un tema y lo envía a todos los endpoints suscritos.

        Parámetros:
        topic (str): Nombre del tema.
        message (str): Mensaje a enviar.

        Excepciones:
        - Lanza una excepción si el tema no existe.
        """
        if topic in self.topics:
            for endpoint in self.topics[topic]:
                endpoint.notify(message)  # Llama al método notify de cada endpoint
        else:
            raise Exception("El tema no existe")


# ------------------------------------------------------------
# Clase SNSEndpoint: Representa un suscriptor del sistema SNS
# ------------------------------------------------------------
class SNSEndpoint:
    def __init__(self, name, endpoint_type):
        """
        Constructor de la clase SNSEndpoint.

        Parámetros:
        name (str): Nombre identificador del endpoint (por ejemplo, 'Juan', 'Soporte').
        endpoint_type (str): Tipo de endpoint (por ejemplo, 'Email', 'SMS', 'Push').
        """
        self.name = name
        self.endpoint_type = endpoint_type

    def notify(self, message):
        """
        Recibe una notificación y la muestra en consola.

        Parámetros:
        message (str): Mensaje enviado al endpoint.
        """
        print(f"📨 Notificación a {self.endpoint_type} {self.name}: {message}")


# ------------------------------------------------------------
# Ejemplo de uso del sistema SNS
# ------------------------------------------------------------

# 1️⃣ Crear una instancia del sistema SNS
sns = SNS()

# 2️⃣ Crear endpoints
email_endpoint = SNSEndpoint("Juan", "Email")
sms_endpoint = SNSEndpoint("Ana", "SMS")

# 3️⃣ Crear un tema
topic = sns.create_topic("Promociones")

# 4️⃣ Suscribir endpoints al tema
sns.subscribe(topic, email_endpoint)
sns.subscribe(topic, sms_endpoint)

# 5️⃣ Publicar un mensaje
sns.publish(topic, "¡Nueva promoción disponible!")

# 6️⃣ Dar de baja un endpoint
sns.unsubscribe(topic, sms_endpoint)

# 7️⃣ Publicar otro mensaje (solo llegará al endpoint suscrito restante)
sns.publish(topic, "Recordatorio de la promoción")
