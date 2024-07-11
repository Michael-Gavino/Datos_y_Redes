class Ledger:
    def __init__(self):
        self.transactions = []

    def record_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

# Crear una instancia de Ledger
ledger = Ledger()

# Añadir transacciones al ledger
ledger.record_transaction({'id': 1, 'action': 'create', 'data': 'Alice'})
ledger.record_transaction({'id': 2, 'action': 'update', 'data': 'Alice Updated'})

# Obtener y mostrar las transacciones
print(ledger.get_transactions())

