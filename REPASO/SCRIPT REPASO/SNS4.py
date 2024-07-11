class SNS:
    def __init__(self):
        self.topics = {}
        # Diccionario para almacenar los topics y sus suscripciones

    def create_topic(self, name):
        if name in self.topics:
            raise Exception(f"Topic {name} already exists")
        # Verifica si el topic ya existe
        self.topics[name] = []
        # Crea un nuevo topic con una lista vacía de suscripciones
        return name

    def subscribe(self, topic, endpoint):
        if topic not in self.topics:
            raise Exception(f"Topic {topic} does not exist")
        # Verifica si el topic existe
        if endpoint in self.topics[topic]:
            raise Exception(f"Endpoint {endpoint.name} is already subscribed to {topic}")
        # Verifica si el endpoint ya está suscrito al topic
        self.topics[topic].append(endpoint)
        # Añade el endpoint a la lista de suscripciones del topic

    def publish(self, topic, message):
        if topic not in self.topics:
            raise Exception(f"Topic {topic} does not exist")
        # Verifica si el topic existe
        if not self.topics[topic]:
            raise Exception(f"No endpoints subscribed to {topic}")
        # Verifica si hay endpoints suscritos al topic
        for endpoint in self.topics[topic]:
            endpoint.notify(message)
        # Envía el mensaje a todos los endpoints suscritos

    def list_topics(self):
        return list(self.topics.keys())
        # Devuelve una lista de todos los nombres de topics

    def list_subscriptions(self, topic):
        if topic not in self.topics:
            raise Exception(f"Topic {topic} does not exist")
        # Verifica si el topic existe
        return [endpoint.name for endpoint in self.topics[topic]]
        # Devuelve una lista de los nombres de endpoints suscritos al topic

class Endpoint:
    def __init__(self, name):
        self.name = name
        # Inicializa el endpoint con nombre

    def notify(self, message):
        print(f"Notification to {self.name}: {message}")
        # Imprime un mensaje de notificación para el endpoint

sns = SNS()  # Crear una instancia del sistema SNS

# Crear endpoints
email = Endpoint("user@example.com")
sms = Endpoint("+51987654321")

# Crear un topic
topic = sns.create_topic("MyTopic")  # Crear un nuevo topic llamado "MyTopic"

# Suscribir endpoints al topic
sns.subscribe("MyTopic", email)  # Suscribir el endpoint email al topic "MyTopic"
sns.subscribe("MyTopic", sms)    # Suscribir el endpoint sms al topic "MyTopic"

# Publicar un mensaje en el topic
sns.publish("MyTopic", "Welcome to MyTopic!")  # Publicar un mensaje en el topic "MyTopic"

# Listar topics y suscripciones
print("Topics:", sns.list_topics())  # Listar todos los topics creados
print("Subscriptions to MyTopic:", sns.list_subscriptions("MyTopic"))  # Listar las suscripciones del topic "MyTopic"

