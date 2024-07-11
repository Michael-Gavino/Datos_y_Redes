class MockEC2Client:
    def __init__(self):
        self.volumes = {}
        self.snapshots = {}
        self.next_volume_id = 1
        self.next_snapshot_id = 1

    def create_volume(self, Size, AvailabilityZone, VolumeType):
        volume_id = f"vol-{self.next_volume_id:04d}"
        self.volumes[volume_id] = {
            'VolumeId': volume_id,
            'Size': Size,
            'AvailabilityZone': AvailabilityZone,
            'VolumeType': VolumeType,
            'State': 'available',
            'Attachments': []
        }
        self.next_volume_id += 1
        return {'VolumeId': volume_id}

    def attach_volume(self, VolumeId, InstanceId, Device):
        if VolumeId in self.volumes:
            self.volumes[VolumeId]['Attachments'].append({
                'InstanceId': InstanceId,
                'Device': Device,
                'State': 'attached'
            })
            self.volumes[VolumeId]['State'] = 'in-use'
        else:
            raise ValueError(f"Volume {VolumeId} does not exist.")

    def create_snapshot(self, VolumeId, Description):
        if VolumeId in self.volumes:
            snapshot_id = f"snap-{self.next_snapshot_id:04d}"
            self.snapshots[snapshot_id] = {
                'SnapshotId': snapshot_id,
                'VolumeId': VolumeId,
                'Description': Description
            }
            self.next_snapshot_id += 1
            return {'SnapshotId': snapshot_id}
        else:
            raise ValueError(f"Volume {VolumeId} does not exist.")

    def describe_snapshots(self, OwnerIds):
        if 'self' in OwnerIds:
            return {'Snapshots': list(self.snapshots.values())}
        else:
            return {'Snapshots': []}

# Crear una instancia del cliente mock
ec2 = MockEC2Client()

# Crear un volumen EBS
def create_ebs_volume(size, availability_zone):
    response = ec2.create_volume(Size=size, AvailabilityZone=availability_zone, VolumeType='gp2')
    volume_id = response['VolumeId']
    print(f"Created EBS Volume: {volume_id}")
    return volume_id

# Adjuntar un volumen EBS a una instancia EC2
def attach_ebs_volume(volume_id, instance_id, device):
    ec2.attach_volume(VolumeId=volume_id, InstanceId=instance_id, Device=device)
    print(f"Attached Volume {volume_id} to Instance {instance_id}")

# Realizar una instantánea de un volumen EBS
def create_snapshot(volume_id, description):
    response = ec2.create_snapshot(VolumeId=volume_id, Description=description)
    snapshot_id = response['SnapshotId']
    print(f"Created Snapshot: {snapshot_id}")
    return snapshot_id

# Listar todas las instantáneas disponibles
def list_snapshots():
    response = ec2.describe_snapshots(OwnerIds=['self'])
    for snapshot in response['Snapshots']:
        print(f"ID: {snapshot['SnapshotId']}, Volume ID: {snapshot['VolumeId']}, Description: {snapshot['Description']}")

# Ejecución de funciones
volume_id = create_ebs_volume(10, 'us-west-2a')
attach_ebs_volume(volume_id, 'i-1234567890abcdef0', '/dev/sdf')
create_snapshot(volume_id, 'Snapshot of volume ' + volume_id)
list_snapshots()
