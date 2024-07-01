class Lambda:
    def __init__(self, nombre):
        self.nombre = nombre

    def accion(self, evento):
        return f"accion {self.nombre} el evento {evento}"

# Funciones Lambda
create_producto = Lambda("ccrear_producto")
get_producto = Lambda("obtener los prodcutos")
get_producto_id = Lambda("obtener productos por id")
update_producto = Lambda("actualizar productos")
delete_producto = Lambda("eliminar productos")

# Simulación de invocación de funciones Lambda
print(create_producto.accion({"action": "crear", "producto": {"id": 1, "nombre": "Producto1"}}))
print(get_producto.accion({"action": "get_productos"}))
print(get_producto_id.accion({"action": "get_id", "id": 1}))
print(update_producto.accion({"action": "update", "productos": {"id": 1, "nombre": "actualizar Producto1"}}))
print(delete_producto.accion({"action": "delete", "id": 1}))
