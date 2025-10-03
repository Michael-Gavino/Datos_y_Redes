# ------------------------------------------------------------
# Clase Ledger: Representa un libro mayor de transacciones
# ------------------------------------------------------------
class Ledger:
    def __init__(self):
        """
        Constructor de la clase Ledger.
        Inicializa un libro mayor vacío donde se almacenarán las transacciones.
        """
        self.transactions = []  # Lista que almacenará las transacciones registradas

    def record_transaction(self, transaction):
        """
        Registra una nueva transacción en el libro mayor.

        Parámetros:
        transaction (dict): Un diccionario que contiene la información de la transacción.
                            Debe incluir las claves: 'id', 'action' y 'data'.
        """
        self.transactions.append(transaction)  # Agrega la transacción a la lista

    def get_transactions(self):
        """
        Devuelve todas las transacciones registradas en el libro mayor.

        Retorna:
        list: Lista con todas las transacciones almacenadas.
        """
        return self.transactions


# ------------------------------------------------------------
# Clase Database: Simula una base de datos donde se migran datos
# ------------------------------------------------------------
class Database:
    def __init__(self):
        """
        Constructor de la clase Database.
        Inicializa una base de datos vacía para almacenar los datos migrados.
        """
        self.data = []  # Lista que almacenará los datos migrados desde el ledger

    def migrate_data(self, transactions):
        """
        Migra las transacciones desde el libro mayor (Ledger) a la base de datos.

        Parámetros:
        transactions (list): Lista de transacciones obtenidas del ledger.
        """
        for transaction in transactions:
            # Simulación de proceso de migración de datos
            migrated_data = {
                'id': transaction['id'],
                'action': transaction['action'],
                'data': transaction['data'] + ' (migrated)'  # Indica que el dato fue migrado
            }
            self.data.append(migrated_data)  # Guarda el dato migrado en la base de datos

    def get_data(self):
        """
        Devuelve todos los datos migrados almacenados en la base de datos.

        Retorna:
        list: Lista de datos migrados.
        """
        return self.data


# ------------------------------------------------------------
# Ejecución del programa principal
# ------------------------------------------------------------

# 1️⃣ Crear una instancia del libro mayor (Ledger)
ledger = Ledger()

# 2️⃣ Registrar transacciones en el libro mayor
ledger.record_transaction({'id': 1, 'action': 'create', 'data': 'Alice'})
ledger.record_transaction({'id': 2, 'action': 'update', 'data': 'Alice Updated'})

# 3️⃣ Mostrar las transacciones registradas en el libro mayor
print("Transacciones en el Ledger (Libro Mayor):")
for transaction in ledger.get_transactions():
    print(f"ID: {transaction['id']}, Acción: {transaction['action']}, Datos: {transaction['data']}")

print("\n")  # Línea en blanco para separar la salida

# 4️⃣ Crear una instancia de la base de datos (Database)
database = Database()

# 5️⃣ Migrar las transacciones del libro mayor a la base de datos
database.migrate_data(ledger.get_transactions())

# 6️⃣ Mostrar los datos migrados en la base de datos
print("Datos migrados en la Base de Datos:")
for dato in database.get_data():
    print(f"ID: {dato['id']}, Acción: {dato['action']}, Datos: {dato['data']}")
    print("-" * 20)  # Separador visual entre registros

