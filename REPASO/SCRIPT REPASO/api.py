class Flask:
    def __init__(self, nombre):
        self.nombre = nombre
        self.rutas = {}

    def agregar_ruta(self, ruta, metodos, controlador):
        self.rutas[ruta] = {'metodos': metodos, 'controlador': controlador}

    def ejecutar(self, debug=False):
        print(f"Ejecutando la aplicación Flask {self.nombre}...")
        while True:
            try:
                ruta = input("Ingrese la ruta (por ejemplo, /recursos/1): ")
                metodo = input("Ingrese el método (GET, POST, PUT, DELETE): ").upper()

                if ruta in self.rutas and metodo in self.rutas[ruta]['metodos']:
                    self.rutas[ruta]['controlador'](ruta)
                else:
                    print("Ruta o método no encontrados. Por favor, verifique su entrada.")
            except KeyError:
                print("Ruta no encontrada. Por favor, verifique la ruta y el método.")

app = Flask(__name__)

# Estructura de datos en memoria
recursos = {}

def crear_recurso(ruta):
    resource_id = input("Ingrese el ID del recurso: ")
    resource_data = input("Ingrese los datos del recurso: ")
    recursos[resource_id] = resource_data
    print({"message": "Recurso creado"})

def obtener_recurso(ruta):
    resource_id = ruta.split('/')[-1]
    resource_data = recursos.get(resource_id)
    if resource_data:
        print({"id": resource_id, "data": resource_data})
    else:
        print({"message": "Recurso no encontrado"})

def actualizar_recurso(ruta):
    resource_id = ruta.split('/')[-1]
    resource_data = input("Ingrese los datos actualizados del recurso: ")
    if resource_id in recursos:
        recursos[resource_id] = resource_data
        print({"message": "Recurso actualizado"})
    else:
        print({"message": "Recurso no encontrado"})

def eliminar_recurso(ruta):
    resource_id = ruta.split('/')[-1]
    if resource_id in recursos:
        del recursos[resource_id]
        print({"message": "Recurso eliminado"})
    else:
        print({"message": "Recurso no encontrado"})

# Agregar rutas y métodos a la aplicación
app.agregar_ruta('/recursos', ['POST'], crear_recurso)
app.agregar_ruta('/recursos/<resource_id>', ['GET'], obtener_recurso)
app.agregar_ruta('/recursos/<resource_id>', ['PUT'], actualizar_recurso)
app.agregar_ruta('/recursos/<resource_id>', ['DELETE'], eliminar_recurso)

if __name__ == '__main__':
    app.ejecutar(debug=True)
