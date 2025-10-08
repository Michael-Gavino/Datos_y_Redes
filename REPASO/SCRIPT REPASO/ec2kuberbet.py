import time  # (Opcional) Módulo usado si se quiere simular demoras en procesos

# 🟡 Clase para representar un clúster de Amazon ECS
class ECSCluster:
    def __init__(self, nombre):
        # Nombre del clúster ECS
        self.nombre = nombre
        # Diccionario para almacenar servicios desplegados en el clúster
        self.servicios = {}

    # Definir una nueva tarea en ECS (imagen de contenedor)
    def definir_tarea(self, nombre_tarea, imagen):
        print(f"Tarea '{nombre_tarea}' definida en ECS '{self.nombre}' con imagen '{imagen}'")

    # Crear un nuevo servicio en el clúster ECS
    def definir_servicio(self, nombre_servicio, nombre_tarea, numero_instancias):
        # Verificar si la tarea ya está asociada a otro servicio
        if nombre_tarea in self.servicios:
            print(f"Error: La tarea '{nombre_tarea}' ya está siendo utilizada en otro servicio en ECS '{self.nombre}'")
        else:
            # Registrar el servicio con su tarea e instancias
            self.servicios[nombre_servicio] = {
                'tarea': nombre_tarea,
                'instancias': numero_instancias
            }
            print(f"Servicio '{nombre_servicio}' definido en ECS '{self.nombre}' con {numero_instancias} instancia(s)")

    # Escalar un servicio existente en ECS (cambiar número de instancias)
    def escalar_servicio(self, nombre_servicio, numero_instancias):
        if nombre_servicio in self.servicios:
            # Actualizar el número de instancias
            self.servicios[nombre_servicio]['instancias'] = numero_instancias
            print(f"Servicio '{nombre_servicio}' en ECS '{self.nombre}' escalado a {numero_instancias} instancia(s)")
        else:
            print(f"Error: Servicio '{nombre_servicio}' no encontrado en ECS '{self.nombre}'")

    # Eliminar un servicio de ECS
    def eliminar_servicio(self, nombre_servicio):
        if nombre_servicio in self.servicios:
            # Eliminarlo del diccionario
            del self.servicios[nombre_servicio]
            print(f"Servicio '{nombre_servicio}' eliminado de ECS '{self.nombre}'")
        else:
            print(f"Error: Servicio '{nombre_servicio}' no encontrado en ECS '{self.nombre}'")


# 🔵 Clase para representar un clúster de Kubernetes
class KubernetesCluster:
    def __init__(self, nombre):
        # Nombre del clúster Kubernetes
        self.nombre = nombre
        # Diccionario que almacena pods desplegados
        self.pods = {}

    # Crear un nuevo pod con un contenedor
    def definir_pod(self, nombre_pod, contenedor):
        if nombre_pod in self.pods:
            print(f"Error: El pod '{nombre_pod}' ya está definido en Kubernetes '{self.nombre}'")
        else:
            # Registrar el pod
            self.pods[nombre_pod] = contenedor
            print(f"Pod '{nombre_pod}' definido en Kubernetes '{self.nombre}' con contenedor '{contenedor}'")

    # Escalar un pod (crear réplicas adicionales)
    def escalar_pod(self, nombre_pod, replicas):
        if nombre_pod in self.pods:
            print(f"Pod '{nombre_pod}' en Kubernetes '{self.nombre}' escalado a {replicas} replicas")
        else:
            print(f"Error: Pod '{nombre_pod}' no encontrado en Kubernetes '{self.nombre}'")

    # Eliminar un pod existente
    def eliminar_pod(self, nombre_pod):
        if nombre_pod in self.pods:
            del self.pods[nombre_pod]
            print(f"Pod '{nombre_pod}' eliminado de Kubernetes '{self.nombre}'")
        else:
            print(f"Error: Pod '{nombre_pod}' no encontrado en Kubernetes '{self.nombre}'")


# 🧪 Función principal: Simula escenarios de despliegue en ECS y Kubernetes
def simular_orquestacion():
    # ----- Simulación en Amazon ECS -----
    ecs_cluster = ECSCluster("MiClusterECS")  # Crear clúster ECS
    ecs_cluster.definir_tarea("tarea1", "mi-imagen:latest")  # Definir tarea
    ecs_cluster.definir_servicio("servicio1", "tarea1", 2)   # Crear servicio con 2 instancias
    ecs_cluster.escalar_servicio("servicio1", 3)            # Escalar a 3 instancias
    ecs_cluster.eliminar_servicio("servicio1")              # Eliminar servicio

    print("\n---\n")  # Separador visual

    # ----- Simulación en Kubernetes -----
    kubernetes_cluster = KubernetesCluster("MiClusterKubernetes")  # Crear clúster K8s
    kubernetes_cluster.definir_pod("pod1", "mi-contenedor")        # Crear pod
    kubernetes_cluster.escalar_pod("pod1", 5)                      # Escalar pod a 5 réplicas
    kubernetes_cluster.eliminar_pod("pod1")                        # Eliminar pod


# 🚀 Ejecución principal del script
if __name__ == "__main__":
    simular_orquestacion()

