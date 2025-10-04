class SNS:
    def __init__(self):
        # Diccionario que almacenará los "topics" (temas) creados y sus suscriptores.
        # La estructura será: {"nombre_del_topic": [lista_de_endpoints_suscritos]}
        self.topics = {}

    def create_topic(self, name):
        """
        Crea un nuevo tema (topic) en el sistema SNS.

        :param name: Nombre del topic a crear.
        :return: El nombre del topic creado.
        :raises Exception: Si el topic ya existe.
        """
        if name in self.topics:
            raise Exception(f"Topic {name} already exists")  # Evita duplicados
        
        # Si no existe, crea el topic con una lista vacía de suscriptores
        self.topics[name] = []
        return name

    def subscribe(self, topic, endpoint):
        """
        Suscribe un endpoint (destino) a un topic específico.

        :param topic: Nombre del topic al que se desea suscribir.
        :param endpoint: Objeto Endpoint que se quiere suscribir.
        :raises Exception: Si el topic no existe o si el endpoint ya está suscrito.
        """
        if topic not in self.topics:
            raise Exception(f"Topic {topic} does not exist")  # Validar existencia del topic
        
        if endpoint in self.topics[topic]:
            raise Exception(f"Endpoint {endpoint.name} is already subscribed to {topic}")
        # Evita suscripciones duplicadas

        # Añade el endpoint a la lista de suscriptores del topic
        self.topics[topic].append(endpoint)

    def publish(self, topic, message):
        """
        Publica un mensaje a todos los endpoints suscritos a un topic.

        :param topic: Nombre del topic en el que se publicará el mensaje.
        :param message: Mensaje a enviar a todos los suscriptores.
        :raises Exception: Si el topic no existe o si no tiene suscriptores.
        """
        if topic not in self.topics:
            raise Exception(f"Topic {topic} does not exist")
        
        if not self.topics[topic]:
            raise Exception(f"No endpoints subscribed to {topic}")
        
        # Envia el mensaje a cada endpoint suscrito al topic
        for endpoint in self.topics[topic]:
            endpoint.notify(message)

    def list_topics(self):
        """
        Devuelve una lista con todos los nombres de los topics creados.

        :return: Lista de nombres de topics.
        """
        return list(self.topics.keys())

    def list_subscriptions(self, topic):
        """
        Devuelve la lista de nombres de todos los endpoints suscritos a un topic.

        :param topic: Nombre del topic.
        :return: Lista de nombres de endpoints suscritos.
        :raises Exception: Si el topic no existe.
        """
        if topic not in self.topics:
            raise Exception(f"Topic {topic} does not exist")
        
        # Retorna los nombres de los endpoints suscritos
        return [endpoint.name for endpoint in self.topics[topic]]


class Endpoint:
    def __init__(self, name):
        """
        Representa un destino (endpoint) que puede recibir notificaciones.

        :param name: Nombre o identificador del endpoint (correo, número, etc.)
        """
        self.name = name

    def notify(self, message):
        """
        Recibe e imprime un mensaje de notificación enviado desde un topic.

        :param message: Mensaje enviado desde el sistema SNS.
        """
        print(f"Notification to {self.name}: {message}")


# ===========================
# EJEMPLO DE USO DEL SISTEMA
# ===========================

# Crear una instancia del sistema SNS
sns = SNS()

# Crear endpoints que recibirán notificaciones
email = Endpoint("user@example.com")
sms = Endpoint("+51987654321")

# Crear un nuevo topic llamado "MyTopic"
topic = sns.create_topic("MyTopic")

# Suscribir los endpoints creados al topic
sns.subscribe("MyTopic", email)
sns.subscribe("MyTopic", sms)

# Publicar un mensaje en el topic (se enviará a todos los suscriptores)
sns.publish("MyTopic", "Welcome to MyTopic!")

# Listar todos los topics existentes
print("Topics:", sns.list_topics())

# Listar los endpoints suscritos a un topic específico
print("Subscriptions to MyTopic:", sns.list_subscriptions("MyTopic"))

