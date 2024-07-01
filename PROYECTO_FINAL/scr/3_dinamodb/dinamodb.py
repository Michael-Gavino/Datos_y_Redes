class DynamoDB:
    def __init__(self):
        self.tabla_productos = {}

    def crear_producto(self, producto):
        if 'id' in producto:
            self.tabla_productos[producto['id']] = producto
            return f"Producto con ID {producto['id']} creado."
        else:
            return "El producto debe tener un ID."

    def obtener_producto_id(self, producto_id):
        if producto_id in self.tabla_productos:
            return self.tabla_productos[producto_id]
        else:
            return f"Producto con ID {producto_id} no encontrado."

    def actualizar_producto(self, producto_id, nuevos_datos):
        if producto_id in self.tabla_productos:
            self.tabla_productos[producto_id].update(nuevos_datos)
            return f"Producto con ID {producto_id} actualizado."
        else:
            return f"Producto con ID {producto_id} no encontrado."

    def eliminar_producto(self, producto_id):
        if producto_id in self.tabla_productos:
            del self.tabla_productos[producto_id]
            return f"Producto con ID {producto_id} eliminado."
        else:
            return f"Producto con ID {producto_id} no encontrado."

# Simulación de interacción con DynamoDB
dynamodb = DynamoDB()

# Creación de productos simulados
print(dynamodb.crear_producto({"id": 1, "nombre": "Producto1", "precio": 10.99}))
print(dynamodb.crear_producto({"id": 2, "nombre": "Producto2", "precio": 15.99}))

# Obtención y actualización de productos simulados
print(dynamodb.obtener_producto_id(1))
print(dynamodb.actualizar_producto(1, {"nombre": "Producto1 Actualizado"}))

# Eliminación de un producto simulado
print(dynamodb.eliminar_producto(2))
