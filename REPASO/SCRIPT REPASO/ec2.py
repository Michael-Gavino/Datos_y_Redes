# Simulación de cliente EC2 de AWS para gestionar volúmenes EBS y snapshots
class MockEC2Client:
    def __init__(self):
        # Diccionario que almacena los volúmenes creados
        self.volumes = {}
        # Diccionario que almacena las instantáneas creadas
        self.snapshots = {}
        # Contadores internos para generar IDs únicos
        self.next_volume_id = 1
        self.next_snapshot_id = 1

    # Crear un volumen EBS simulado
    def create_volume(self, Size, AvailabilityZone, VolumeType):
        # Generar un ID único para el volumen
        volume_id = f"vol-{self.next_volume_id:04d}"
        # Guardar los datos del volumen en el diccionario
        self.volumes[volume_id] = {
            'VolumeId': volume_id,
            'Size': Size,
            'AvailabilityZone': AvailabilityZone,
            'VolumeType': VolumeType,
            'State': 'available',  # Estado inicial: disponible
            'Attachments': []      # Lista de instancias a las que está adjunto
        }
        self.next_volume_id += 1
        return {'VolumeId': volume_id}

    # Adjuntar un volumen EBS simulado a una instancia EC2
    def attach_volume(self, VolumeId, InstanceId, Device):
        if VolumeId in self.volumes:
            # Registrar la instancia y el dispositivo al que se adjunta
            self.volumes[VolumeId]['Attachments'].append({
                'InstanceId': InstanceId,
                'Device': Device,
                'State': 'attached'  # Estado: adjunto
            })
            # Cambiar el estado del volumen a "en uso"
            self.volumes[VolumeId]['State'] = 'in-use'
        else:
            # Lanzar error si el volumen no existe
            raise ValueError(f"Volume {VolumeId} does not exist.")

    # Crear una instantánea de un volumen EBS simulado
    def create_snapshot(self, VolumeId, Description):
        if VolumeId in self.volumes:
            # Generar un ID único para la instantánea
            snapshot_id = f"snap-{self.next_snapshot_id:04d}"
            # Guardar los datos de la instantánea
            self.snapshots[snapshot_id] = {
                'SnapshotId': snapshot_id,
                'VolumeId': VolumeId,
                'Description': Description
            }
            self.next_snapshot_id += 1
            return {'SnapshotId': snapshot_id}
        else:
            raise ValueError(f"Volume {VolumeId} does not exist.")

    # Listar todas las instantáneas creadas por el "usuario"
    def describe_snapshots(self, OwnerIds):
        # Simula el filtrado por propietario ('self')
        if 'self' in OwnerIds:
            return {'Snapshots': list(self.snapshots.values())}
        else:
            return {'Snapshots': []}


# Crear una instancia del cliente simulado
ec2 = MockEC2Client()

# 🧰 Funciones auxiliares de alto nivel

# Crear un volumen EBS
def create_ebs_volume(size, availability_zone):
    response = ec2.create_volume(Size=size, AvailabilityZone=availability_zone, VolumeType='gp2')
    volume_id = response['VolumeId']
    print(f"✅ Created EBS Volume: {volume_id}")
    return volume_id

# Adjuntar un volumen EBS a una instancia EC2
def attach_ebs_volume(volume_id, instance_id, device):
    ec2.attach_volume(VolumeId=volume_id, InstanceId=instance_id, Device=device)
    print(f"🔗 Attached Volume {volume_id} to Instance {instance_id}")

# Crear una instantánea (snapshot) de un volumen EBS
def create_snapshot(volume_id, description):
    response = ec2.create_snapshot(VolumeId=volume_id, Description=description)
    snapshot_id = response['SnapshotId']
    print(f"📸 Created Snapshot: {snapshot_id}")
    return snapshot_id

# Listar todas las instantáneas disponibles
def list_snapshots():
    response = ec2.describe_snapshots(OwnerIds=['self'])
    print("📂 Snapshots disponibles:")
    for snapshot in response['Snapshots']:
        print(f"  - ID: {snapshot['SnapshotId']}, Volume ID: {snapshot['VolumeId']}, Description: {snapshot['Description']}")


# 🧪 Ejemplo de uso de las funciones definidas
volume_id = create_ebs_volume(10, 'us-west-2a')                        # Crear volumen
attach_ebs_volume(volume_id, 'i-1234567890abcdef0', '/dev/sdf')       # Adjuntar volumen a instancia EC2
create_snapshot(volume_id, 'Snapshot of volume ' + volume_id)          # Crear snapshot
list_snapshots()                                                       # Listar snapshots
