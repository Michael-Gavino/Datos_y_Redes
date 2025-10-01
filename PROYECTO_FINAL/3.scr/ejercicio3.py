import json

# =====================================================
# Simulación de base de datos DynamoDB
# =====================================================
# En lugar de conectarnos a una base de datos real, usamos una lista de diccionarios
# para simular una tabla con productos, donde cada producto tiene:
# - id: identificador único
# - name: nombre del producto
# - price: precio del producto
products_db = [
    {'id': 1, 'name': 'Product 1', 'price': 100},
    {'id': 2, 'name': 'Product 2', 'price': 150},
]

# =====================================================
# Funciones Lambda simuladas (CRUD)
# =====================================================
# Cada función representa una Lambda que respondería a eventos HTTP en AWS API Gateway.
# Los parámetros:
# - event: contiene los datos de la solicitud (body, pathParameters, etc.)
# - context: contiene información del entorno de ejecución (no se usa aquí)


# -----------------------------------------------------
# CREATE - Crear un nuevo producto
# -----------------------------------------------------
def lambda_create_product(event, context):
    """
    Crea un nuevo producto en la base de datos simulada.
    
    Args:
        event (dict): Contiene el cuerpo ('body') en formato JSON con los datos del nuevo producto.
        context: Contexto de ejecución Lambda (no utilizado).
    
    Returns:
        tuple: Producto creado (dict) y código de estado HTTP (201).
    """
    new_product = json.loads(event['body'])          # Convertimos el JSON recibido en un diccionario
    new_product['id'] = len(products_db) + 1         # Generamos un nuevo ID automáticamente
    products_db.append(new_product)                  # Agregamos el nuevo producto a la base simulada
    return new_product, 201


# -----------------------------------------------------
# READ - Obtener todos los productos
# -----------------------------------------------------
def lambda_get_all_products(event, context):
    """
    Devuelve la lista completa de productos.
    
    Args:
        event (dict): No se utiliza en esta función.
        context: Contexto de ejecución Lambda (no utilizado).
    
    Returns:
        list: Lista de todos los productos.
    """
    return products_db


# -----------------------------------------------------
# READ - Obtener un producto por su ID
# -----------------------------------------------------
def lambda_get_product_by_id(event, context):
    """
    Obtiene un producto específico por su ID.
    
    Args:
        event (dict): Contiene 'pathParameters' con el 'id' del producto.
        context: Contexto de ejecución Lambda (no utilizado).
    
    Returns:
        dict: Producto encontrado o mensaje de error si no existe.
        int: Código de estado HTTP (200 o 404).
    """
    product_id = int(event['pathParameters']['id'])  # Extraemos el ID desde los parámetros de ruta
    product = next((prod for prod in products_db if prod['id'] == product_id), None)  # Buscamos el producto
    
    return product if product else ({'message': 'Product not found'}, 404)


# -----------------------------------------------------
# UPDATE - Actualizar un producto existente
# -----------------------------------------------------
def lambda_update_product(event, context):
    """
    Actualiza los datos de un producto existente según su ID.
    
    Args:
        event (dict): Contiene 'pathParameters' con el 'id' y 'body' con los datos a actualizar.
        context: Contexto de ejecución Lambda (no utilizado).
    
    Returns:
        dict: Producto actualizado o mensaje de error si no existe.
        int: Código de estado HTTP (200 o 404).
    """
    product_id = int(event['pathParameters']['id'])  # ID del producto a actualizar
    update_data = json.loads(event['body'])          # Datos nuevos en formato diccionario
    product = next((prod for prod in products_db if prod['id'] == product_id), None)
    
    if product:
        product.update(update_data)                  # Actualizamos los campos con los nuevos datos
        return product
    return {'message': 'Product not found'}, 404     # Si no se encuentra el producto


# -----------------------------------------------------
# DELETE - Eliminar un producto por ID
# -----------------------------------------------------
def lambda_delete_product(event, context):
    """
    Elimina un producto de la base de datos simulada según su ID.
    
    Args:
        event (dict): Contiene 'pathParameters' con el 'id' del producto.
        context: Contexto de ejecución Lambda (no utilizado).
    
    Returns:
        dict: Mensaje confirmando la eliminación.
    """
    global products_db
    product_id = int(event['pathParameters']['id'])
    # Filtramos todos los productos excepto el que coincide con el ID
    products_db = [prod for prod in products_db if prod['id'] != product_id]
    return {'message': 'Product deleted'}


# =====================================================
# Bloque principal - Simulación de ejecución local
# =====================================================
# Este bloque permite probar las funciones Lambda sin desplegarlas en AWS.
if __name__ == '__main__':
    print("📦 Crear Producto:")
    print(lambda_create_product({'body': '{"name": "New Product", "price": 120}'}, {}))
    
    print("\n📜 Obtener Todos los Productos:")
    print(lambda_get_all_products({}, {}))
    
    print("\n🔍 Obtener Producto por ID:")
    print(lambda_get_product_by_id({'pathParameters': {'id': '2'}}, {}))
    print(lambda_get_product_by_id({'pathParameters': {'id': '4'}}, {}))  # ID inexistente
    
    print("\n✏️ Actualizar Producto por ID:")
    print(lambda_update_product({'pathParameters': {'id': '1'}, 'body': '{"price": 110}'}, {}))
    print(lambda_update_product({'pathParameters': {'id': '4'}, 'body': '{"price": 300}'}, {}))  # ID inexistente
    
    print("\n🗑️ Eliminar Producto por ID:")
    print(lambda_delete_product({'pathParameters': {'id': '2'}}, {}))


