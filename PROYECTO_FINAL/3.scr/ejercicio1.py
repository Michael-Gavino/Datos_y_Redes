# ----------------------------------------------
# Simulación de funciones Lambda y DynamoDB en Python
# ----------------------------------------------

# --------------------------------------------------------
# Función Lambda simulada para crear un nuevo producto
# --------------------------------------------------------
def lambda_create_product(event, context):
    """
    Simula una función Lambda que crea un producto.

    Parámetros:
    -----------
    event : dict
        Contiene los datos del producto a crear. Debe incluir:
        - 'id': int - Identificador del producto
        - 'name': str - Nombre del producto
        - 'price': float - Precio del producto
    context : dict
        Contexto de ejecución de Lambda (no utilizado en la simulación).

    Retorna:
    --------
    dict:
        Diccionario con los datos del producto creado.
    """
    return {
        'id': event['id'],
        'name': event['name'],
        'price': event['price']
    }


# --------------------------------------------------------
# Función Lambda simulada para obtener todos los productos
# --------------------------------------------------------
def lambda_get_all_products(event, context):
    """
    Simula una función Lambda que obtiene todos los productos disponibles.

    Parámetros:
    -----------
    event : dict
        Evento que activa la función (no se utiliza en esta simulación).
    context : dict
        Contexto de ejecución de Lambda (no se utiliza en esta simulación).

    Retorna:
    --------
    list:
        Lista de productos disponibles con sus atributos.
    """
    return [
        {'id': 1, 'name': 'Product 1', 'price': 100},
        {'id': 2, 'name': 'Product 2', 'price': 150},
    ]


# --------------------------------------------------------
# Simulación de actualización de producto en DynamoDB
# --------------------------------------------------------
def dynamodb_update_product(product_id, update_data):
    """
    Simula la actualización de un producto en DynamoDB.

    Parámetros:
    -----------
    product_id : int
        ID del producto que se desea actualizar.
    update_data : dict
        Datos que se quieren actualizar en el producto.

    Retorna:
    --------
    dict or None:
        - El producto actualizado si se encontró y modificó.
        - None si el producto no existe.
    """
    for product in products_db:
        if product['id'] == product_id:
            product.update(update_data)  # Actualiza los datos del producto
            return product
    return None  # Si no se encontró el producto


# --------------------------------------------------------
# Simulación de eliminación de producto en DynamoDB
# --------------------------------------------------------
def dynamodb_delete_product(product_id):
    """
    Simula la eliminación de un producto en DynamoDB.

    Parámetros:
    -----------
    product_id : int
        ID del producto que se desea eliminar.

    Retorna:
    --------
    dict:
        Mensaje indicando que el producto fue eliminado.
    """
    global products_db
    # Crea una nueva lista sin el producto que coincide con el ID
    products_db = [prod for prod in products_db if prod['id'] != product_id]
    return {'message': 'Product deleted'}


# --------------------------------------------------------
# Simulación de ejecución principal
# --------------------------------------------------------
if __name__ == '__main__':
    # Simula la creación de un nuevo producto
    print("Crear Producto:")
    print(lambda_create_product({'id': 4, 'name': 'New Product', 'price': 120}, {}))

    # Simula la obtención de todos los productos disponibles
    print("\nObtener Todos los Productos:")
    print(lambda_get_all_products({}, {}))

    # Base de datos simulada en memoria
    products_db = [
        {'id': 1, 'name': 'Product 1', 'price': 100},
        {'id': 2, 'name': 'Product 2', 'price': 150},
    ]

    # Simula la actualización del producto con ID 2
    print("\nActualizar Producto:")
    print(dynamodb_update_product(2, {'price': 150}))

    # Simula la eliminación del producto con ID 2
    print("\nEliminar Producto:")
    print(dynamodb_delete_product(2))
