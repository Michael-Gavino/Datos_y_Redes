class EBSVolume:
    def __init__(self, volume_id, size):
        self.volume_id = volume_id
        self.size = size
        self.instancia_adjunto_id = None
        self.data = {}

    def adjuntar(self, instance_id):
        if self.instancia_adjunto_id is None:
            self.instancia_adjunto_id = instance_id
            print(f"Volumen EBS {self.volume_id} adjuntado a la instancia {instance_id}")
        else:
            print(f"Volumen EBS {self.volume_id} ya está adjuntado a la instancia {self.instancia_adjunto_id}")

    def desadjuntar(self):
        if self.instancia_adjunto_id is not None:
            print(f"Volumen EBS {self.volume_id} desadjuntado de la instancia {self.instancia_adjunto_id}")
            self.instancia_adjunto_id = None
        else:
            print(f"Volumen EBS {self.volume_id} no está adjuntado a ninguna instancia")

    def almacenar_datos(self, key, value):
        if self.instancia_adjunto_id is not None:
            self.data[key] = value
            print(f"Datos almacenados en el volumen EBS {self.volume_id}")
        else:
            print(f"Volumen EBS {self.volume_id} no está adjuntado a ninguna instancia. No se pueden almacenar datos.")

    def recuperar_datos(self, key):
        return self.data.get(key, "Datos no encontrados")

class InstanceStoreVolume:
    def __init__(self, volume_id, size):
        self.volume_id = volume_id
        self.size = size
        self.instancia_adjunto_id = None
        self.data = {}

    def adjuntar(self, instance_id):
        if self.instancia_adjunto_id is None:
            self.instancia_adjunto_id = instance_id
            print(f"Volumen de almacenamiento de instancia {self.volume_id} adjuntado a la instancia {instance_id}")
        else:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} ya está adjuntado a la instancia {self.instancia_adjunto_id}")

    def desadjuntar(self):
        if self.instancia_adjunto_id is not None:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} desadjuntado de la instancia {self.instancia_adjunto_id}")
            self.instancia_adjunto_id = None
        else:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} no está adjuntado a ninguna instancia")

    def almacenar_datos(self, key, value):
        if self.instancia_adjunto_id is not None:
            self.data[key] = value
            print(f"Datos almacenados en el volumen de almacenamiento de instancia {self.volume_id}")
        else:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} no está adjuntado a ninguna instancia. No se pueden almacenar datos.")

    def recuperar_datos(self, key):
        return self.data.get(key, "Datos no encontrados")

class EC2Manager:
    def __init__(self):
        self.volumenes_ebs = {}
        self.volumenes_almacenamiento_instancia = {}
        self.siguiente_volume_id = 1

    def crear_volumen_ebs(self, size):
        volume_id = f"vol-{self.siguiente_volume_id:04d}"
        volume = EBSVolume(volume_id, size)
        self.volumenes_ebs[volume_id] = volume
        self.siguiente_volume_id += 1
        print(f"Creado volumen EBS {volume_id} con tamaño {size}GB")
        return volume_id

    def crear_volumen_almacenamiento_instancia(self, size):
        volume_id = f"istore-{self.siguiente_volume_id:04d}"
        volume = InstanceStoreVolume(volume_id, size)
        self.volumenes_almacenamiento_instancia[volume_id] = volume
        self.siguiente_volume_id += 1
        print(f"Creado volumen de almacenamiento de instancia {volume_id} con tamaño {size}GB")
        return volume_id

    def eliminar_volumen_ebs(self, volume_id):
        if volume_id in self.volumenes_ebs:
            del self.volumenes_ebs[volume_id]
            print(f"Volumen EBS {volume_id} eliminado")
        else:
            print(f"Volumen EBS {volume_id} no encontrado")

    def adjuntar_volumen(self, volume_id, instance_id, tipo_volumen='ebs'):
        if tipo_volumen == 'ebs' and volume_id in self.volumenes_ebs:
            self.volumenes_ebs[volume_id].adjuntar(instance_id)
        elif tipo_volumen == 'almacenamiento_instancia' and volume_id in self.volumenes_almacenamiento_instancia:
            self.volumenes_almacenamiento_instancia[volume_id].adjuntar(instance_id)
        else:
            print(f"Volumen {volume_id} no encontrado")

    def desadjuntar_volumen(self, volume_id, tipo_volumen='ebs'):
        if tipo_volumen == 'ebs' and volume_id in self.volumenes_ebs:
            self.volumenes_ebs[volume_id].desadjuntar()
        elif tipo_volumen == 'almacenamiento_instancia' and volume_id in self.volumenes_almacenamiento_instancia:
            self.volumenes_almacenamiento_instancia[volume_id].desadjuntar()
        else:
            print(f"Volumen {volume_id} no encontrado")

    def simular_fallo(self, volume_id, tipo_volumen='ebs'):
        if tipo_volumen == 'ebs' and volume_id in self.volumenes_ebs:
            self.volumenes_ebs[volume_id].data = {}
            print(f"Fallo simulado para volumen EBS {volume_id}. Datos perdidos.")
        elif tipo_volumen == 'almacenamiento_instancia' and volume_id in self.volumenes_almacenamiento_instancia:
            self.volumenes_almacenamiento_instancia[volume_id].data = {}
            print(f"Fallo simulado para volumen de almacenamiento de instancia {volume_id}. Datos perdidos.")
        else:
            print(f"Volumen {volume_id} no encontrado")

# Simulación de uso
def main():
    manager = EC2Manager()

    # Crear algunos volúmenes para la simulación
    id_volumen_ebs = manager.crear_volumen_ebs(10)
    id_volumen_almacenamiento_instancia = manager.crear_volumen_almacenamiento_instancia(20)

    # Adjuntar volúmenes a instancias
    manager.adjuntar_volumen(id_volumen_ebs, 'i-12345678')
    manager.adjuntar_volumen(id_volumen_almacenamiento_instancia, 'i-87654321', tipo_volumen='almacenamiento_instancia')

    # Almacenar y recuperar datos
    manager.volumenes_ebs[id_volumen_ebs].almacenar_datos('clave1', 'valor1')
    print(manager.volumenes_ebs[id_volumen_ebs].recuperar_datos('clave1'))

    manager.volumenes_almacenamiento_instancia[id_volumen_almacenamiento_instancia].almacenar_datos('clave2', 'valor2')
    print(manager.volumenes_almacenamiento_instancia[id_volumen_almacenamiento_instancia].recuperar_datos('clave2'))

    # Simular fallo en un volumen
    manager.simular_fallo(id_volumen_ebs)
    print(manager.volumenes_ebs[id_volumen_ebs].recuperar_datos('clave1'))

    # Desadjuntar volúmenes
    manager.desadjuntar_volumen(id_volumen_ebs)
    manager.desadjuntar_volumen(id_volumen_almacenamiento_instancia, tipo_volumen='almacenamiento_instancia')

    # Eliminar un volumen EBS
    manager.eliminar_volumen_ebs(id_volumen_ebs)

if __name__ == "__main__":
    main()
