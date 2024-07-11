class Ledger:
    def __init__(self):
        self.transactions = []

    def record_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions


class Database:
    def __init__(self):
        self.data = []

    def migrate_data(self, transactions):
        for transaction in transactions:
            # migración de datos
            migrated_data = {
                'id': transaction['id'],
                'action': transaction['action'],
                'data': transaction['data'] + ' (migrated)'
            }
            self.data.append(migrated_data)

    def get_data(self):
        return self.data

#  instancia Ledger 
ledger = Ledger()

# transacciones 
ledger.record_transaction({'id': 1, 'action': 'create', 'data': 'Alice'})
ledger.record_transaction({'id': 2, 'action': 'update', 'data': 'Alice Updated'})

# Obtener y mostrar transacciones del ledger (libro mayor)
print("Transacciones en el Ledger (Libro Mayor):")
for transaction in ledger.get_transactions():
    print(f"ID: {transaction['id']}, Acción: {transaction['action']}, Datos: {transaction['data']}")

print("\n")

# Crear una instancia de Database 
database = Database()

# Migrar datos del ledger a la base de datos
database.migrate_data(ledger.get_transactions())

# Obtener y mostrar los datos migrados de la base de datos
print("Datos migrados en la Base de Datos:")
for dato in database.get_data():
    print(f"ID: {dato['id']}, Acción: {dato['action']}, Datos: {dato['data']}")
    print("-" * 20) 
