"""
Simulación del manejo de volúmenes EBS y almacenamiento de instancia en Amazon EC2.

Este script implementa una simulación del comportamiento de los volúmenes EBS (Elastic Block Store) 
y los volúmenes de almacenamiento de instancia, incluyendo operaciones como:
- Crear volúmenes.
- Adjuntar y desadjuntar volúmenes a instancias.
- Almacenar y recuperar datos.
- Simular fallos (pérdida de datos).
- Eliminar volúmenes.

También se incluye un gestor (`EC2Manager`) que administra todos los volúmenes creados.
"""

# Clase que representa un volumen EBS (almacenamiento persistente)
class EBSVolume:
    def __init__(self, volume_id, size):
        """
        Inicializa un volumen EBS con un ID y tamaño determinado.
        :param volume_id: Identificador único del volumen.
        :param size: Tamaño del volumen en GB.
        """
        self.volume_id = volume_id
        self.size = size
        self.instancia_adjunto_id = None  # ID de la instancia a la que está adjuntado
        self.data = {}  # Almacenamiento simulado de datos

    def adjuntar(self, instance_id):
        """
        Adjunta el volumen EBS a una instancia específica.
        :param instance_id: ID de la instancia a la que se adjunta el volumen.
        """
        if self.instancia_adjunto_id is None:
            self.instancia_adjunto_id = instance_id
            print(f"Volumen EBS {self.volume_id} adjuntado a la instancia {instance_id}")
        else:
            print(f"Volumen EBS {self.volume_id} ya está adjuntado a la instancia {self.instancia_adjunto_id}")

    def desadjuntar(self):
        """
        Desadjunta el volumen EBS de la instancia a la que está conectado.
        """
        if self.instancia_adjunto_id is not None:
            print(f"Volumen EBS {self.volume_id} desadjuntado de la instancia {self.instancia_adjunto_id}")
            self.instancia_adjunto_id = None
        else:
            print(f"Volumen EBS {self.volume_id} no está adjuntado a ninguna instancia")

    def almacenar_datos(self, key, value):
        """
        Almacena un par clave-valor en el volumen EBS.
        Solo es posible si el volumen está adjuntado a una instancia.
        """
        if self.instancia_adjunto_id is not None:
            self.data[key] = value
            print(f"Datos almacenados en el volumen EBS {self.volume_id}")
        else:
            print(f"Volumen EBS {self.volume_id} no está adjuntado a ninguna instancia. No se pueden almacenar datos.")

    def recuperar_datos(self, key):
        """
        Recupera un dato almacenado por su clave.
        :param key: Clave del dato a recuperar.
        :return: Valor asociado a la clave o mensaje si no se encuentra.
        """
        return self.data.get(key, "Datos no encontrados")


# Clase que representa un volumen de almacenamiento de instancia (no persistente)
class InstanceStoreVolume:
    def __init__(self, volume_id, size):
        """
        Inicializa un volumen de almacenamiento de instancia.
        """
        self.volume_id = volume_id
        self.size = size
        self.instancia_adjunto_id = None
        self.data = {}

    def adjuntar(self, instance_id):
        """
        Adjunta el volumen de almacenamiento a una instancia.
        """
        if self.instancia_adjunto_id is None:
            self.instancia_adjunto_id = instance_id
            print(f"Volumen de almacenamiento de instancia {self.volume_id} adjuntado a la instancia {instance_id}")
        else:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} ya está adjuntado a la instancia {self.instancia_adjunto_id}")

    def desadjuntar(self):
        """
        Desadjunta el volumen de almacenamiento de la instancia.
        """
        if self.instancia_adjunto_id is not None:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} desadjuntado de la instancia {self.instancia_adjunto_id}")
            self.instancia_adjunto_id = None
        else:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} no está adjuntado a ninguna instancia")

    def almacenar_datos(self, key, value):
        """
        Almacena datos si el volumen está adjunto.
        """
        if self.instancia_adjunto_id is not None:
            self.data[key] = value
            print(f"Datos almacenados en el volumen de almacenamiento de instancia {self.volume_id}")
        else:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} no está adjuntado a ninguna instancia. No se pueden almacenar datos.")

    def recuperar_datos(self, key):
        """
        Recupera datos almacenados en el volumen.
        """
        return self.data.get(key, "Datos no encontrados")


# Clase gestora de volúmenes que simula la consola de administración de EC2
class EC2Manager:
    def __init__(self):
        """
        Inicializa el gestor de volúmenes con contenedores para EBS y almacenamiento de instancia.
        """
        self.volumenes_ebs = {}
        self.volumenes_almacenamiento_instancia = {}
        self.siguiente_volume_id = 1  # Contador para generar IDs únicos

    def crear_volumen_ebs(self, size):
        """
        Crea un volumen EBS y lo registra en el sistema.
        """
        volume_id = f"vol-{self.siguiente_volume_id:04d}"
        volume = EBSVolume(volume_id, size)
        self.volumenes_ebs[volume_id] = volume
        self.siguiente_volume_id += 1
        print(f"Creado volumen EBS {volume_id} con tamaño {size}GB")
        return volume_id

    def crear_volumen_almacenamiento_instancia(self, size):
        """
        Crea un volumen de almacenamiento de instancia.
        """
        volume_id = f"istore-{self.siguiente_volume_id:04d}"
        volume = InstanceStoreVolume(volume_id, size)
        self.volumenes_almacenamiento_instancia[volume_id] = volume
        self.siguiente_volume_id += 1
        print(f"Creado volumen de almacenamiento de instancia {volume_id} con tamaño {size}GB")
        return volume_id

    def eliminar_volumen_ebs(self, volume_id):
        """
        Elimina un volumen EBS del sistema.
        """
        if volume_id in self.volumenes_ebs:
            del self.volumenes_ebs[volume_id]
            print(f"Volumen EBS {volume_id} eliminado")
        else:
            print(f"Volumen EBS {volume_id} no encontrado")

    def adjuntar_volumen(self, volume_id, instance_id, tipo_volumen='ebs'):
        """
        Adjunta un volumen a una instancia, dependiendo del tipo especificado.
        """
        if tipo_volumen == 'ebs' and volume_id in self.volumenes_ebs:
            self.volumenes_ebs[volume_id].adjuntar(instance_id)
        elif tipo_volumen == 'almacenamiento_instancia' and volume_id in self.volumenes_almacenamiento_instancia:
            self.volumenes_almacenamiento_instancia[volume_id].adjuntar(instance_id)
        else:
            print(f"Volumen {volume_id} no encontrado")

    def desadjuntar_volumen(self, volume_id, tipo_volumen='ebs'):
        """
        Desadjunta un volumen según su tipo.
        """
        if tipo_volumen == 'ebs' and volume_id in self.volumenes_ebs:
            self.volumenes_ebs[volume_id].desadjuntar()
        elif tipo_volumen == 'almacenamiento_instancia' and volume_id in self.volumenes_almacenamiento_instancia:
            self.volumenes_almacenamiento_instancia[volume_id].desadjuntar()
        else:
            print(f"Volumen {volume_id} no encontrado")

    def simular_fallo(self, volume_id, tipo_volumen='ebs'):
        """
        Simula un fallo que borra todos los datos del volumen.
        """
        if tipo_volumen == 'ebs' and volume_id in self.volumenes_ebs:
            self.volumenes_ebs[volume_id].data = {}
            print(f"Fallo simulado para volumen EBS {volume_id}. Datos perdidos.")
        elif tipo_volumen == 'almacenamiento_instancia' and volume_id in self.volumenes_almacenamiento_instancia:
            self.volumenes_almacenamiento_instancia[volume_id].data = {}
            print(f"Fallo simulado para volumen de almacenamiento de instancia {volume_id}. Datos perdidos.")
        else:
            print(f"Volumen {volume_id} no encontrado")


# Simulación de uso del sistema
def main():
    manager = EC2Manager()

    # Crear volúmenes
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

    # Simular un fallo en el volumen EBS
    manager.simular_fallo(id_volumen_ebs)
    print(manager.volumenes_ebs[id_volumen_ebs].recuperar_datos('clave1'))

    # Desadjuntar volúmenes
    manager.desadjuntar_volumen(id_volumen_ebs)
    manager.desadjuntar_volumen(id_volumen_almacenamiento_instancia, tipo_volumen='almacenamiento_instancia')

    # Eliminar un volumen EBS
    manager.eliminar_volumen_ebs(id_volumen_ebs)


if __name__ == "__main__":
    main()

