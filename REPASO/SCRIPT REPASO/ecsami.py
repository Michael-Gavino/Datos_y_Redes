#  Clase que representa una Amazon Machine Image (AMI)
class AMI:
    def __init__(self, ami_id, name, source_instance_id):
        # ID único de la AMI
        self.ami_id = ami_id
        # Nombre asignado a la AMI
        self.name = name
        # ID de la instancia a partir de la cual se creó la AMI
        self.source_instance_id = source_instance_id


#  Clase que representa una instancia EC2
class EC2Instance:
    def __init__(self, instance_id, ami_id):
        # ID único de la instancia
        self.instance_id = instance_id
        # ID de la AMI desde la cual se lanzó la instancia
        self.ami_id = ami_id
        # Estado inicial de la instancia (detenida por defecto)
        self.state = 'stopped'

    #  Iniciar una instancia EC2
    def start(self):
        if self.state == 'stopped':
            self.state = 'running'
            print(f"Instance {self.instance_id} started.")
        else:
            print(f"Instance {self.instance_id} is already running.")

    #  Detener una instancia EC2 en ejecución
    def stop(self):
        if self.state == 'running':
            self.state = 'stopped'
            print(f"Instance {self.instance_id} stopped.")
        else:
            print(f"Instance {self.instance_id} is not running.")

    #  Terminar una instancia EC2 (eliminación definitiva)
    def terminate(self):
        if self.state in ['running', 'stopped']:
            self.state = 'terminated'
            print(f"Instance {self.instance_id} terminated.")
        else:
            print(f"Instance {self.instance_id} is already terminated.")


#  Clase que administra la creación de instancias EC2 y AMIs
class EC2Manager:
    def __init__(self):
        # Diccionario para almacenar instancias creadas
        self.instances = {}
        # Diccionario para almacenar AMIs creadas
        self.amis = {}
        # Contadores para generar IDs únicos
        self.next_instance_id = 1
        self.next_ami_id = 1

    # Crear una nueva instancia EC2 desde una AMI existente
    def create_instance(self, ami_id):
        instance_id = f"i-{self.next_instance_id:04d}"  # Formato: i-0001
        instance = EC2Instance(instance_id, ami_id)
        self.instances[instance_id] = instance
        self.next_instance_id += 1
        print(f"Created instance {instance_id} from AMI {ami_id}")
        return instance_id

    #  Crear una nueva AMI desde una instancia existente
    def create_ami(self, name, source_instance_id):
        ami_id = f"ami-{self.next_ami_id:04d}"  # Formato: ami-0001
        ami = AMI(ami_id, name, source_instance_id)
        self.amis[ami_id] = ami
        self.next_ami_id += 1
        print(f"Created AMI {ami_id} from instance {source_instance_id}")
        return ami_id

    #  Listar todas las AMIs disponibles
    def list_amis(self):
        for ami_id, ami in self.amis.items():
            print(f"AMI ID: {ami_id}, Name: {ami.name}, Source Instance ID: {ami.source_instance_id}")

    # Listar todas las instancias creadas
    def list_instances(self):
        for instance_id, instance in self.instances.items():
            print(f"Instance ID: {instance_id}, AMI ID: {instance.ami_id}, State: {instance.state}")


#  Función principal: simulación completa del flujo de trabajo EC2
def main():
    manager = EC2Manager()  # Crear el gestor de recursos EC2

    #  Crear una instancia desde una AMI base
    instance_id = manager.create_instance('ami-0001')

    #  Crear una AMI desde esa instancia
    ami_id = manager.create_ami('MyFirstAMI', instance_id)

    #  Listar todas las AMIs creadas
    print("\nList of AMIs:")
    manager.list_amis()

    # Crear una nueva instancia a partir de la AMI recién creada
    new_instance_id = manager.create_instance(ami_id)

    # Listar todas las instancias disponibles
    print("\nList of Instances:")
    manager.list_instances()

    # 🔄 Gestionar el ciclo de vida de una instancia
    instance = manager.instances[instance_id]
    instance.start()      # Iniciar
    instance.stop()       # Detener
    instance.terminate()  # Terminar

    #  Verificar el estado final de todas las instancias
    print("\nList of Instances after state changes:")
    manager.list_instances()


#  Punto de entrada del programa
if __name__ == "__main__":
    main()

