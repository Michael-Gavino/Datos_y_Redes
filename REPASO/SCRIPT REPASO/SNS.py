class SNS:
    def __init__(self):
        self.topics = {}
        
    def create_topic(self, name):
        self.topics[name] = []
        return name

    def subscribe(self, topic, endpoint):
        if topic in self.topics:
            self.topics[topic].append(endpoint)
        else:
            raise Exception("Topic does not exist")
    
    def publish(self, topic, message):
        if topic in self.topics:
            for endpoint in self.topics[topic]:
                endpoint.notify(message)
        else:
            raise Exception("Topic does not exist")
    
class Endpoint:
    def __init__(self, name):
        self.name = name
        
    def notify(self, message):
        print(f"Notification to {self.name}: {message}")
# Ejemplo de uso
sns = SNS()
email = Endpoint("Email")
sms = Endpoint("SMS")
topic = sns.create_topic("MyTopic")
sns.subscribe(topic, email)
sns.subscribe(topic, sms)
sns.publish(topic, "Hello, world!")
