import time

class CDN:
    """
    Clase CDN (Content Delivery Network)
    ------------------------------------
    Esta clase simula el comportamiento básico de una red de entrega de contenido.
    Permite obtener contenido desde un servidor de origen y almacenarlo en una caché local
    para servirlo más rápido en futuras solicitudes, evitando acceder al servidor cada vez.

    Atributos:
        cache (dict): Diccionario que almacena contenido en caché con su marca de tiempo.
        max_cache_size (int): Tamaño máximo permitido de la caché.
        cache_expiration (int): Tiempo máximo que un contenido puede permanecer en caché (en segundos).
    """

    def __init__(self, max_cache_size, cache_expiration):
        """
        Inicializa el CDN con un tamaño máximo de caché y un tiempo de expiración.

        Args:
            max_cache_size (int): Número máximo de elementos que puede almacenar la caché.
            cache_expiration (int): Tiempo en segundos que un contenido puede permanecer en caché.
        """
        self.cache = {}  # Almacenará el contenido en forma {url: (contenido, timestamp)}
        self.max_cache_size = max_cache_size
        self.cache_expiration = cache_expiration
    
    def get_content(self, url):
        """
        Obtiene el contenido solicitado desde la caché o el servidor de origen.

        - Si el contenido está en la caché y no ha expirado, se devuelve desde la caché.
        - Si ha expirado o no está en caché, se obtiene del servidor de origen y se almacena.

        Args:
            url (str): URL del contenido solicitado.

        Returns:
            str: Contenido obtenido (desde caché o servidor).
        """
        if url in self.cache:
            # Si la URL está en caché, verificar si ha expirado
            content, timestamp = self.cache[url]
            if time.time() - timestamp < self.cache_expiration:
                print("✅ Contenido servido desde la caché")
                return content
            else:
                print("⚠️ Caché expirada, obteniendo nuevo contenido")
                self.cache.pop(url)  # Eliminar contenido expirado
        
        # Si no está en caché o ha expirado, se obtiene del servidor de origen
        content = self.fetch_from_origin(url)
        self.add_to_cache(url, content)  # Guardar en caché para futuras solicitudes
        return content
    
    def fetch_from_origin(self, url):
        """
        Simula la obtención del contenido desde el servidor de origen.

        Args:
            url (str): URL del contenido solicitado.

        Returns:
            str: Contenido obtenido del servidor de origen.
        """
        print(f"🌐 Obteniendo contenido desde el servidor de origen para {url}...")
        time.sleep(2)  # Simula el tiempo de respuesta del servidor
        return f"Contenido de {url}"
    
    def add_to_cache(self, url, content):
        """
        Agrega un nuevo contenido a la caché.

        - Si la caché está llena, elimina el contenido más antiguo.

        Args:
            url (str): URL asociada al contenido.
            content (str): Contenido a almacenar.
        """
        if len(self.cache) >= self.max_cache_size:
            self.evict_cache()  # Si la caché está llena, eliminar el más antiguo
        self.cache[url] = (content, time.time())  # Guardar con la hora actual
    
    def evict_cache(self):
        """
        Elimina la entrada de caché más antigua para liberar espacio.
        """
        oldest_url = min(self.cache, key=lambda k: self.cache[k][1])  # Buscar la más antigua
        print(f"🗑️ Eliminando caché para {oldest_url}")
        self.cache.pop(oldest_url)
    
    def __str__(self):
        """
        Representación en cadena del estado actual de la caché.

        Returns:
            str: Representación de la caché.
        """
        return str(self.cache)

def main():
    """
    Función principal del programa.
    --------------------------------
    Crea una instancia del CDN y permite al usuario interactuar con él desde la terminal.
    Comandos disponibles:
        - 'get': Solicitar contenido desde una URL (se obtiene desde la caché o el servidor).
        - 'exit': Salir del programa.
    """
    cdn = CDN(max_cache_size=3, cache_expiration=10)  # Crear CDN con 3 elementos y 10 seg de expiración
    
    while True:
        command = input("Ingrese comando (get, exit): ")  # Solicitar comando
        
        if command == 'get':
            url = input("Ingrese la URL para obtener el contenido: ")
            content = cdn.get_content(url)  # Obtener contenido
            print(content)
        elif command == 'exit':
            print("🚪 Saliendo del programa...")
            break
        else:
            print("❌ Comando inválido. Intente con 'get' o 'exit'.")

# Ejecutar la función principal si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()

