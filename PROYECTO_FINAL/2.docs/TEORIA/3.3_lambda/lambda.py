class Lambda:
    """
    Clase Lambda
    ------------
    Simula el comportamiento de una función Lambda en un entorno serverless, 
    la cual ejecuta una acción específica en respuesta a un evento recibido.

    Atributos:
    ----------
    nombre : str
        Nombre descriptivo de la función Lambda.

    Métodos:
    --------
    accion(evento):
        Simula la ejecución de la función Lambda cuando se invoca con un evento.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Lambda.

        Parámetros:
        -----------
        nombre : str
            Nombre que identifica la función Lambda.
        """
        self.nombre = nombre

    def accion(self, evento):
        """
        Simula la ejecución de la función Lambda.

        Parámetros:
        -----------
        evento : dict
            Diccionario que representa el evento que desencadena la ejecución
            de la función Lambda. Puede incluir información como la acción a realizar 
            o los datos del producto.

        Retorna:
        --------
        str : Mensaje que indica qué acción ha sido realizada y con qué evento.
        """
        return f"Acción '{self.nombre}' ejecutada con el evento: {evento}"


# ------------------------------
# Creación de funciones Lambda
# ------------------------------

# Cada instancia representa una función Lambda diferente
create_producto = Lambda("crear_producto")
get_producto = Lambda("obtener_productos")
get_producto_id = Lambda("obtener_producto_por_id")
update_producto = Lambda("actualizar_producto")
delete_producto = Lambda("eliminar_producto")

# ------------------------------------------------------------
# Simulación de invocación de funciones Lambda con diferentes eventos
# ------------------------------------------------------------

# Simula la creación de un producto
print(create_producto.accion({
    "action": "crear", 
    "producto": {"id": 1, "nombre": "Producto1"}
}))

# Simula la obtención de todos los productos
print(get_producto.accion({
    "action": "get_productos"
}))

# Simula la obtención de un producto por su ID
print(get_producto_id.accion({
    "action": "get_id", 
    "id": 1
}))

# Simula la actualización de un producto existente
print(update_producto.accion({
    "action": "update", 
    "producto": {"id": 1, "nombre": "Producto1 actualizado"}
}))

# Simula la eliminación de un producto por su ID
print(delete_producto.accion({
    "action": "delete", 
    "id": 1
}))

