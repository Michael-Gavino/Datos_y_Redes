class Server: #creacion de la clase server
    def __init__(self, cpu_capacity, memory_capacity):
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.current_load = 0

    def scale_up(self, additional_cpu, additional_memory):# se incrementa las capacidades de cpu y menoria
        self.cpu_capacity += additional_cpu
        self.memory_capacity =+ additional_memory

class ServerCluster:# cluster de servidores
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        self.servers.append(server)

    def remove_servers(self):#remover servers inecesarias
        if self.servers:
            selfservers.pop()

    def distribute_load(self, load):# distribucion y carga
        if not self.servers:
            print("No servers available")
            return
        load_per_server = load/len(self.servers)
        for server in self.servers:
            server.current_load += load_per_server
            
server1 = Server(4, 8)
server2 = Server(4, 8)
cluster = ServerCluster()
cluster.add_server(server1)
cluster.add_server(server2)
cluster.distribute_load(10)
