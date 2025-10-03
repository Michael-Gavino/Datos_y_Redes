# Clase Ledger para registrar y gestionar transacciones
class Ledger:
    def __init__(self):
        """
        Constructor de la clase Ledger.
        Inicializa un libro de registros (ledger) vacío para almacenar transacciones.
        """
        self.transactions = []  # Lista donde se guardarán todas las transacciones registradas

    def record_transaction(self, transaction):
        """
        Registra una nueva transacción en el ledger.

        Parámetros:
        transaction (dict): Un diccionario que representa la transacción,
                            debe contener al menos un 'id', una 'action' y 'data'.
        """
        self.transactions.append(transaction)  # Agrega la transacción a la lista

    def get_transactions(self):
        """
        Devuelve todas las transacciones registradas en el ledger.

        Retorna:
        list: Lista de todas las transacciones almacenadas.
        """
        return self.transactions  # Retorna la lista completa de transacciones


# ------------------- Ejemplo de uso de la clase Ledger -------------------

# Crear una instancia de la clase Ledger
ledger = Ledger()

# Registrar transacciones en el ledger
# Cada transacción es un diccionario con un ID, una acción y los datos asociados
ledger.record_transaction({'id': 1, 'action': 'create', 'data': 'Alice'})
ledger.record_transaction({'id': 2, 'action': 'update', 'data': 'Alice Updated'})

# Obtener y mostrar todas las transacciones registradas
print(ledger.get_transactions())
