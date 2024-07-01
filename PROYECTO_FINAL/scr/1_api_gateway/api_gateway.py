class APIGateway:
    def __init__(self):
        self.recursos = {} #lista para los recursos y metodos

    def crear_recursos(self, ruta):
        self.recursos[ruta] = {} #crear un recurso a una ruta   
        return f"Recurso{ruta} creado."

    def crear_metodo(self, ruta, metodo):
        if ruta in self.recursos: #crear un metodo oara el recurso
            self.recursos[ruta][metodo] = f"{metodo} metodo para {ruta}"
            return f"Metodo {metodo} para {ruta} creado."
        else:
            return "Recurso no encontrado."

    def simulacion(self): #simulacion de la configuracion
        print("Simulacion de API Gateway")
        print(self.recursos)

#la creación de recursos y métodos
api_gateway = APIGateway()
print(api_gateway.crear_recursos("/productos"))
print(api_gateway.crear_metodo("/productos", "GET"))
print(api_gateway.crear_metodo("/productos", "POST"))
print(api_gateway.crear_recursos("/productos/{id}"))
print(api_gateway.crear_metodo("/productos/{id}", "GET"))
print(api_gateway.crear_metodo("/productos/{id}", "PUT"))
print(api_gateway.crear_metodo("/productos/{id}", "DELETE"))
#mostrar la simulacion
print(api_gateway.simulacion())
