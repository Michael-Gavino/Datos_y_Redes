import json

# Simulación de base de datos DynamoDB
products_db = [
    {'id': 1, 'name': 'Product 1', 'price': 100},
    {'id': 2, 'name': 'Product 2', 'price': 150},
]

# Funciones Lambda simuladas
def lambda_create_product(event, context):
    new_product = json.loads(event['body'])
    new_product['id'] = len(products_db) + 1
    products_db.append(new_product)
    return new_product, 201

def lambda_get_all_products(event, context):
    return products_db

def lambda_get_product_by_id(event, context):
    product_id = int(event['pathParameters']['id'])
    product = next((prod for prod in products_db if prod['id'] == product_id), None)
    return product if product else ({'message': 'Product not found'}, 404)

def lambda_update_product(event, context):
    product_id = int(event['pathParameters']['id'])
    update_data = json.loads(event['body'])
    product = next((prod for prod in products_db if prod['id'] == product_id), None)
    if product:
        product.update(update_data)
        return product
    return {'message': 'Product not found'}, 404

def lambda_delete_product(event, context):
    global products_db
    product_id = int(event['pathParameters']['id'])
    products_db = [prod for prod in products_db if prod['id'] != product_id]
    return {'message': 'Product deleted'}

# Ejemplo de invocación de funciones (simulación de Lambda)
if __name__ == '__main__':
    print("Crear Producto:")
    print(lambda_create_product({'body': '{"name": "New Product", "price": 120}'}, {}))
    
    print("\nObtener Todos los Productos:")
    print(lambda_get_all_products({}, {}))
    
    print("\nObtener Producto por ID:")
    print(lambda_get_product_by_id({'pathParameters': {'id': '2'}}, {}))
    print(lambda_get_product_by_id({'pathParameters': {'id': '4'}}, {}))
    
    print("\nActualizar Producto por ID:")
    print(lambda_update_product({'pathParameters': {'id': '1'}, 'body': '{"price": 110}'}, {}))
    print(lambda_update_product({'pathParameters': {'id': '4'}, 'body': '{"price": 300}'}, {}))
    
    print("\nEliminar Producto por ID:")
    print(lambda_delete_product({'pathParameters': {'id': '2'}}, {}))

