class AMI:
    def __init__(self, ami_id, name, source_instance_id):
        self.ami_id = ami_id
        self.name = name
        self.source_instance_id = source_instance_id

class EC2Instance:
    def __init__(self, instance_id, ami_id):
        self.instance_id = instance_id
        self.ami_id = ami_id
        self.state = 'stopped'

    def start(self):
        if self.state == 'stopped':
            self.state = 'running'
            print(f"Instance {self.instance_id} started.")
        else:
            print(f"Instance {self.instance_id} is already running.")

    def stop(self):
        if self.state == 'running':
            self.state = 'stopped'
            print(f"Instance {self.instance_id} stopped.")
        else:
            print(f"Instance {self.instance_id} is not running.")

    def terminate(self):
        if self.state in ['running', 'stopped']:
            self.state = 'terminated'
            print(f"Instance {self.instance_id} terminated.")
        else:
            print(f"Instance {self.instance_id} is already terminated.")

class EC2Manager:
    def __init__(self):
        self.instances = {}
        self.amis = {}
        self.next_instance_id = 1
        self.next_ami_id = 1

    def create_instance(self, ami_id):
        instance_id = f"i-{self.next_instance_id:04d}"
        instance = EC2Instance(instance_id, ami_id)
        self.instances[instance_id] = instance
        self.next_instance_id += 1
        print(f"Created instance {instance_id} from AMI {ami_id}")
        return instance_id

    def create_ami(self, name, source_instance_id):
        ami_id = f"ami-{self.next_ami_id:04d}"
        ami = AMI(ami_id, name, source_instance_id)
        self.amis[ami_id] = ami
        self.next_ami_id += 1
        print(f"Created AMI {ami_id} from instance {source_instance_id}")
        return ami_id

    def list_amis(self):
        for ami_id, ami in self.amis.items():
            print(f"AMI ID: {ami_id}, Name: {ami.name}, Source Instance ID: {ami.source_instance_id}")

    def list_instances(self):
        for instance_id, instance in self.instances.items():
            print(f"Instance ID: {instance_id}, AMI ID: {instance.ami_id}, State: {instance.state}")

# Simulación de uso
def main():
    manager = EC2Manager()

    # Crear algunas instancias y AMIs para la simulación
    instance_id = manager.create_instance('ami-0001')
    ami_id = manager.create_ami('MyFirstAMI', instance_id)

    # Listar AMIs
    print("\nList of AMIs:")
    manager.list_amis()

    # Lanzar nuevas instancias desde una AMI
    new_instance_id = manager.create_instance(ami_id)

    # Listar instancias
    print("\nList of Instances:")
    manager.list_instances()

    # Gestionar estado de las instancias
    instance = manager.instances[instance_id]
    instance.start()
    instance.stop()
    instance.terminate()

    # Listar instancias después de gestionar el estado
    print("\nList of Instances after state changes:")
    manager.list_instances()

if __name__ == "__main__":
    main()
