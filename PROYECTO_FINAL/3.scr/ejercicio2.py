import json

# Simulación de la base de datos
productos_db = [
    {'id': 1, 'nombre': 'Producto 1', 'precio': 100},
    {'id': 2, 'nombre': 'Producto 2', 'precio': 150},
]
# Funciones CRUD
def obtener_productos(event, context):
    return productos_db

def obtener_producto(event, context):
    producto_id = int(event['pathParameters']['id'])
    producto = next((prod for prod in productos_db if prod['id'] == producto_id), None)
    return producto if producto else ({'mensaje': 'Producto no encontrado'})

def crear_producto(event, context):
    nuevo_producto = json.loads(event['body'])
    nuevo_producto['id'] = len(productos_db) + 1
    productos_db.append(nuevo_producto)
    return nuevo_producto, 201

def actualizar_producto(event, context):
    producto_id = int(event['pathParameters']['id'])
    datos_actualizados = json.loads(event['body'])
    producto = next((prod for prod in productos_db if prod['id'] == producto_id), None)
    if producto:
        producto.update(datos_actualizados)
        return producto
    return {'mensaje': 'Producto no encontrado'}

def eliminar_producto(event, context):
    global productos_db
    producto_id = int(event['pathParameters']['id'])
    productos_db = [prod for prod in productos_db if prod['id'] != producto_id]
    return {'mensaje': 'Producto eliminado'}

# Ejemplo de invocación de funciones lambda
if __name__ == '__main__':
    print("Obtener Todos los Productos:")
    print(obtener_productos({}, {}))
    
    print("\nObtener Producto por ID:")
    print(obtener_producto({'pathParameters': {'id': '2'}}, {}))
    print(obtener_producto({'pathParameters': {'id': '4'}}, {}))
    
    print("\nCrear Producto:")
    print(crear_producto({'body': '{"nombre": "Nuevo Producto", "precio": 120}'}, {}))
    
    print("\nActualizar Producto por ID:")
    print(actualizar_producto({'pathParameters': {'id': '1'}, 'body': '{"precio": 110}'}, {}))
    print(actualizar_producto({'pathParameters': {'id': '4'}, 'body': '{"precio": 300}'}, {}))
    
    print("\nEliminar Producto por ID:")
    print(eliminar_producto({'pathParameters': {'id': '3'}}, {}))


