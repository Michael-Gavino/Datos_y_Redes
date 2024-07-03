# Simulación de función Lambda para crear un producto en una base de datos ficticia
def lambda_create_product(event, context):
    new_product = {
        'id': event['id'],
        'name': event['name'],
        'price': event['price']
    }
    # Aquí se simularía el código para insertar el producto en una base de datos (por ejemplo, lista en memoria)
    return new_product

# Simulación de función Lambda para obtener todos los productos de una base de datos ficticia
def lambda_get_all_products(event, context):
    # Aquí se simularía el código para obtener todos los productos de una base de datos (por ejemplo, lista en memoria)
    products = [
        {'id': 1, 'name': 'Product 1', 'price': 100},
        {'id': 2, 'name': 'Product 2', 'price': 150},
        {'id': 3, 'name': 'Product 3', 'price': 200}
    ]
    return products

# Simulación de integración con DynamoDB para actualizar un producto
def dynamodb_update_product(product_id, update_data):
    # actualizar un producto en DynamoDB (por ejemplo, actualizar en una lista en memoria)
    for product in products_db:
        if product['id'] == product_id:
            product.update(update_data)
            return product
    return None

# Simulación de integración con DynamoDB para eliminar un producto
def dynamodb_delete_product(product_id):
    # Aquí se simularía el código para eliminar un producto de DynamoDB (por ejemplo, eliminar de una lista en memoria)
    global products_db
    products_db = [prod for prod in products_db if prod['id'] != product_id]
    return {'message': 'Product deleted'}

# Simulación de llamadas a las funciones Lambda y a DynamoDB
if __name__ == '__main__':
    # Ejemplo de llamadas a las funciones Lambda simuladas
    print("Crear Producto:")
    print(lambda_create_product({'id': 4, 'name': 'New Product', 'price': 120}, {}))
    
    print("\nObtener Todos los Productos:")
    print(lambda_get_all_products({}, {}))
    
    # Ejemplo de llamadas a las funciones simuladas de DynamoDB
    print("\nActualizar Producto:")
    products_db = [
        {'id': 1, 'name': 'Product 1', 'price': 100},
        {'id': 2, 'name': 'Product 2', 'price': 150},
        {'id': 3, 'name': 'Product 3', 'price': 200}
    ]
    print(dynamodb_update_product(2, {'price': 180}))
    
    print("\nEliminar Producto:")
    print(dynamodb_delete_product(3))
