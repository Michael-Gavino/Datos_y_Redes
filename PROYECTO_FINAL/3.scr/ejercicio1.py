# Simulación de funciones Lamda
def lambda_create_product(event, context):
    return {
        'id': event['id'],
        'name': event['name'],
        'price': event['price']
    }
# simulacion de la funcion lambda
def lambda_get_all_products(event, context):
    return [
        {'id': 1, 'name': 'Product 1', 'price': 100},
        {'id': 2, 'name': 'Product 2', 'price': 150},
    ]
# Simulación de integración con DynamoDB
def dynamodb_update_product(product_id, update_data):
    for product in products_db:
        if product['id'] == product_id:
            product.update(update_data)
            return product
    return None
#simulacion dynamodb para eliminar producto
def dynamodb_delete_product(product_id):
    global products_db
    products_db = [prod for prod in products_db if prod['id'] != product_id]
    return {'message': 'Product deleted'}
# Simulación de llamadas a las funciones Lambda y DynamoDB
if __name__ == '__main__':
    print("Crear Producto:")
    print(lambda_create_product({'id': 4, 'name': 'New Product', 'price': 120}, {}))   
    print("\nObtener Todos los Productos:")
    print(lambda_get_all_products({}, {}))  
    products_db = [
        {'id': 1, 'name': 'Product 1', 'price': 100},
        {'id': 2, 'name': 'Product 2', 'price': 150},
    ]   
    print("\nActualizar Producto:")
    print(dynamodb_update_product(2, {'price': 150}))
    
    print("\nEliminar Producto:")
    print(dynamodb_delete_product(2))

