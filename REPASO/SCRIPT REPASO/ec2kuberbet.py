import time

# Clase para representar un clúster de Amazon ECS
class ECSCluster:
    def __init__(self, nombre):
        self.nombre = nombre
        self.servicios = {}

    def definir_tarea(self, nombre_tarea, imagen):
        print(f"Tarea '{nombre_tarea}' definida en ECS '{self.nombre}' con imagen '{imagen}'")

    def definir_servicio(self, nombre_servicio, nombre_tarea, numero_instancias):
        if nombre_tarea in self.servicios:
            print(f"Error: La tarea '{nombre_tarea}' ya está siendo utilizada en otro servicio en ECS '{self.nombre}'")
        else:
            self.servicios[nombre_servicio] = {
                'tarea': nombre_tarea,
                'instancias': numero_instancias
            }
            print(f"Servicio '{nombre_servicio}' definido en ECS '{self.nombre}' con {numero_instancias} instancia(s)")

    def escalar_servicio(self, nombre_servicio, numero_instancias):
        if nombre_servicio in self.servicios:
            self.servicios[nombre_servicio]['instancias'] = numero_instancias
            print(f"Servicio '{nombre_servicio}' en ECS '{self.nombre}' escalado a {numero_instancias} instancia(s)")
        else:
            print(f"Error: Servicio '{nombre_servicio}' no encontrado en ECS '{self.nombre}'")

    def eliminar_servicio(self, nombre_servicio):
        if nombre_servicio in self.servicios:
            del self.servicios[nombre_servicio]
            print(f"Servicio '{nombre_servicio}' eliminado de ECS '{self.nombre}'")
        else:
            print(f"Error: Servicio '{nombre_servicio}' no encontrado en ECS '{self.nombre}'")

# Clase para representar un clúster de Kubernetes
class KubernetesCluster:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pods = {}

    def definir_pod(self, nombre_pod, contenedor):
        if nombre_pod in self.pods:
            print(f"Error: El pod '{nombre_pod}' ya está definido en Kubernetes '{self.nombre}'")
        else:
            self.pods[nombre_pod] = contenedor
            print(f"Pod '{nombre_pod}' definido en Kubernetes '{self.nombre}' con contenedor '{contenedor}'")

    def escalar_pod(self, nombre_pod, replicas):
        if nombre_pod in self.pods:
            print(f"Pod '{nombre_pod}' en Kubernetes '{self.nombre}' escalado a {replicas} replicas")
        else:
            print(f"Error: Pod '{nombre_pod}' no encontrado en Kubernetes '{self.nombre}'")

    def eliminar_pod(self, nombre_pod):
        if nombre_pod in self.pods:
            del self.pods[nombre_pod]
            print(f"Pod '{nombre_pod}' eliminado de Kubernetes '{self.nombre}'")
        else:
            print(f"Error: Pod '{nombre_pod}' no encontrado en Kubernetes '{self.nombre}'")

# Función para simular escenarios de despliegue y gestión en ECS y Kubernetes
def simular_orquestacion():
    # Simulación en Amazon ECS
    ecs_cluster = ECSCluster("MiClusterECS")
    ecs_cluster.definir_tarea("tarea1", "mi-imagen:latest")
    ecs_cluster.definir_servicio("servicio1", "tarea1", 2)
    ecs_cluster.escalar_servicio("servicio1", 3)
    ecs_cluster.eliminar_servicio("servicio1")

    print("\n---\n")

    # Simulación en Kubernetes
    kubernetes_cluster = KubernetesCluster("MiClusterKubernetes")
    kubernetes_cluster.definir_pod("pod1", "mi-contenedor")
    kubernetes_cluster.escalar_pod("pod1", 5)
    kubernetes_cluster.eliminar_pod("pod1")

# Ejemplo de uso
if __name__ == "__main__":
    simular_orquestacion()
