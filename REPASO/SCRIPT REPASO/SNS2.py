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
        
    def unsubscribe(self, topic, endpoint):
        if topic in self.topics:
            self.topics[topic].remove(endpoint)
        else:
            raise Exception("Topic does not exist")
        
    def publish(self, topic, message):
        if topic in self.topics:
            for endpoint in self.topics[topic]:
                endpoint.notify(message)
        else:
            raise Exception("Topic does not exist")
        
class SNSEndpoint:
    def __init__(self, name, endpoint_type):
        self.name = name
        self.endpoint_type = endpoint_type
        
    def notify(self, message):
        print(f"Notification to {self.endpoint_type} {self.name}: {message}")
