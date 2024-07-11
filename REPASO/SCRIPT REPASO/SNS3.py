class SNS:
    def __init__(self):
        self.topics = {}

    def crear_tema(self, name):
        self.topics[name] = []
        return name
    
    def suscribir(self, tema, endpoint):
        if tema in self.topics:
            self.topics[tema].append(endpoint)
        else:
            raise Exception("Tema no existe")
        
    def notificar(self, tema, mensaje):
        if tema in self.topics:
            for endpoint in self.topics[tema]:
                endpoint.notificacion(mensaje)
        else:
            raise Exception("Tema no existe") 
            
class Endpoint:
    def __init__(self, name):
        self.name = name

    def notificacion(self, mensaje):
        print(f"Notificación {self.name}: {mensaje}")
        
# Ejemplo de uso corregido
sns = SNS()

email = Endpoint("email")
sms = Endpoint("sms")

tema = sns.crear_tema("mi tema")
sns.suscribir("mi tema", email)
sns.suscribir("mi tema", sms)

sns.notificar("mi tema", "notificación")

## crear un generador de credenciales para usasr boto 3