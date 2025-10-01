import json

# ------------------------------------------------------------
# Simulación de base de datos en memoria (lista de productos)
# ------------------------------------------------------------
productos_db = [
    {'id': 1, 'nombre': 'Producto 1', 'precio': 100},
    {'id': 2, 'nombre': 'Producto 2', 'precio': 150},
]

# ------------------------------------------------------------
# Funciones CRUD simulando funciones Lambda en AWS
# ------------------------------------------------------------

def obtener_productos(event, context):
    """
    Obtiene la lista completa de productos.

    Parámetros:
    -----------
    event : dict
        Evento que activa la función (no se utiliza en esta simulación).
    context : dict
        Contexto de ejecución de Lambda (no se utiliza en esta simulación).

    Retorna:
    --------
    list:
        Lista de todos los productos almacenados en la base de datos simulada.
    """
    return productos_db


def obtener_producto(event, context):
    """
    Obtiene un producto específico por su ID.

    Parámetros:
    -----------
    event : dict
        Contiene la ruta del parámetro 'id' dentro de 'pathParameters'.
    context : dict
        Contexto de ejecución de Lambda (no se utiliza en esta simulación).

    Retorna:
    --------
    dict:
        El producto encontrado o un mensaje indicando que no existe.
    """
    producto_id = int(event['pathParameters']['id'])  # Extraer el ID desde el evento
    producto = next((prod for prod in productos_db if prod['id'] == producto_id), None)
    return producto if producto else {'mensaje': 'Producto no encontrado'}


def crear_producto(event, context):
    """
    Crea un nuevo producto y lo añade a la base de datos simulada.

    Parámetros:
    -----------
    event : dict
        Contiene los datos del nuevo producto en formato JSON dentro de 'body'.
    context : dict
        Contexto de ejecución de Lambda (no se utiliza en esta simulación).

    Retorna:
    --------
    tuple:
        - dict: El nuevo producto creado.
        - int: Código de estado HTTP (201 indica creación exitosa).
    """
    nuevo_producto = json.loads(event['body'])  # Convertir el cuerpo JSON a diccionario
    nuevo_producto['id'] = len(productos_db) + 1  # Asignar un nuevo ID incremental
    productos_db.append(nuevo_producto)  # Agregar a la base de datos
    return nuevo_producto, 201


def actualizar_producto(event, context):
    """
    Actualiza un producto existente por su ID.

    Parámetros:
    -----------
    event : dict
        Contiene el 'id' en 'pathParameters' y los datos a actualizar en 'body'.
    context : dict
        Contexto de ejecución de Lambda (no se utiliza en esta simulación).

    Retorna:
    --------
    dict:
        El producto actualizado o un mensaje si no se encontró.
    """
    producto_id = int(event['pathParameters']['id'])
    datos_actualizados = json.loads(event['body'])  # Convertir datos JSON a diccionario
    producto = next((prod for prod in productos_db if prod['id'] == producto_id), None)
    if producto:
        producto.update(datos_actualizados)  # Actualiza los campos indicados
        return producto
    return {'mensaje': 'Producto no encontrado'}


def eliminar_producto(event, context):
    """
    Elimina un producto de la base de datos por su ID.

    Parámetros:
    -----------
    event : dict
        Contiene el 'id' del producto a eliminar dentro de 'pathParameters'.
    context : dict
        Contexto de ejecución de Lambda (no se utiliza en esta simulación).

    Retorna:
    --------
    dict:
        Mensaje indicando que el producto fue eliminado.
    """
    global productos_db
    producto_id = int(event['pathParameters']['id'])
    # Filtra la lista dejando solo los productos que no coincidan con el ID
    productos_db = [prod for prod in productos_db if prod['id'] != producto_id]
    return {'mensaje': 'Producto eliminado'}


# ------------------------------------------------------------
# Ejemplo de invocación de las funciones Lambda (simulación)
# ------------------------------------------------------------
if __name__ == '__main__':
    # Obtener todos los productos
    print("Obtener Todos los Productos:")
    print(obtener_productos({}, {}))

    # Obtener un producto por ID existente e inexistente
    print("\nObtener Producto por ID:")
    print(obtener_producto({'pathParameters': {'id': '2'}}, {}))
    print(obtener_producto({'pathParameters': {'id': '4'}}, {}))  # No existe

    # Crear un nuevo producto
    print("\nCrear Producto:")
    print(crear_producto({'body': '{"nombre": "Nuevo Producto", "precio": 120}'}, {}))

    # Actualizar un producto existente y uno inexistente
    print("\nActualizar Producto por ID:")
    print(actualizar_producto({'pathParameters': {'id': '1'}, 'body': '{"precio": 110}'}, {}))
    print(actualizar_producto({'pathParameters': {'id': '4'}, 'body': '{"precio": 300}'}, {}))

    # Eliminar un producto por ID
    print("\nEliminar Producto por ID:")
    print(eliminar_producto({'pathParameters': {'id': '3'}}, {}))
