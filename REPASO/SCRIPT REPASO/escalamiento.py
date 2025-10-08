# ----------------------------------------------------------
# Simulación de un Clúster de Servidores en Python
# Permite crear servidores, escalar recursos, eliminar nodos
# y distribuir carga de trabajo entre ellos.
# ----------------------------------------------------------

class Server:
    """
    Representa un servidor individual con capacidades de CPU y memoria.

    Atributos:
        cpu_capacity (int): Capacidad total de CPU del servidor.
        memory_capacity (int): Capacidad total de memoria del servidor.
        current_load (float): Carga actual del servidor.
    """

    def __init__(self, cpu_capacity, memory_capacity):
        """
        Inicializa un servidor con capacidades específicas de CPU y memoria.

        Args:
            cpu_capacity (int): Capacidad inicial de CPU.
            memory_capacity (int): Capacidad inicial de memoria.
        """
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.current_load = 0  # Inicialmente sin carga

    def scale_up(self, additional_cpu, additional_memory):
        """
        Escala el servidor aumentando su capacidad de CPU y memoria.

        Args:
            additional_cpu (int): CPU adicional a agregar.
            additional_memory (int): Memoria adicional a agregar.
        """
        self.cpu_capacity += additional_cpu
        self.memory_capacity += additional_memory  # ✅ corregido: era '=+' en lugar de '+='


# ----------------------------------------------------------
#  Clase ServerCluster: Maneja un conjunto de servidores
# ----------------------------------------------------------
class ServerCluster:
    """
    Representa un clúster de servidores.

    Permite agregar o eliminar servidores y distribuir carga entre ellos.
    """

    def __init__(self):
        """Inicializa un clúster vacío sin servidores."""
        self.servers = []

    def add_server(self, server):
        """
        Agrega un nuevo servidor al clúster.

        Args:
            server (Server): Instancia del servidor a agregar.
        """
        self.servers.append(server)
        print("✅ Servidor agregado al clúster.")

    def remove_server(self):
        """
        Elimina el último servidor agregado al clúster, si existe.
        """
        if self.servers:
            removed = self.servers.pop()
            print("🗑️ Servidor eliminado del clúster.")
        else:
            print("⚠️ No hay servidores para eliminar.")

    def distribute_load(self, load):
        """
        Distribuye la carga total entre todos los servidores del clúster.

        Args:
            load (float): Carga total a distribuir.
        """
        if not self.servers:
            print("❌ No hay servidores disponibles para distribuir la carga.")
            return

        load_per_server = load / len(self.servers)  # Carga equitativa por servidor

        for server in self.servers:
            server.current_load += load_per_server

        print(f"⚙️ Carga distribuida: {load} unidades totales, "
              f"{load_per_server:.2f} por servidor.")


# ----------------------------------------------------------
#  Ejemplo de uso
# ----------------------------------------------------------
if __name__ == "__main__":
    # Crear servidores individuales
    server1 = Server(4, 8)
    server2 = Server(4, 8)

    # Crear un clúster y agregar servidores
    cluster = ServerCluster()
    cluster.add_server(server1)
    cluster.add_server(server2)

    # Distribuir carga de trabajo
    cluster.distribute_load(10)

