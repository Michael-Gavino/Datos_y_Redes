import time

class CDN:
    def __init__(self, max_cache_size, cache_expiration):
        self.cache = {}
        self.max_cache_size = max_cache_size
        self.cache_expiration = cache_expiration
    
    def get_content(self, url):
        if url in self.cache:
            content, timestamp = self.cache[url]
            if time.time() - timestamp < self.cache_expiration:
                print("Contenido servido desde la caché")
                return content
            else:
                print("Caché expirada, obteniendo nuevo contenido")
                self.cache.pop(url)
        
        content = self.fetch_from_origin(url)
        self.add_to_cache(url, content)
        return content
    
    def fetch_from_origin(self, url):
        print(f"Obteniendo contenido desde el servidor de origen para {url}...")
        time.sleep(2)  # Simular tiempo de respuesta del servidor de origen
        return f"Contenido de {url}"
    
    def add_to_cache(self, url, content):
        if len(self.cache) >= self.max_cache_size:
            self.evict_cache()
        self.cache[url] = (content, time.time())
    
    def evict_cache(self):
        # Eliminar la entrada de caché más antigua
        oldest_url = min(self.cache, key=lambda k: self.cache[k][1])
        print(f"Eliminando caché para {oldest_url}")
        self.cache.pop(oldest_url)
    
    def __str__(self):
        return str(self.cache)

def main():
    cdn = CDN(max_cache_size=3, cache_expiration=10)
    
    while True:
        command = input("Ingrese comando (get, exit): ")
        
        if command == 'get':
            url = input("Ingrese la URL para obtener el contenido: ")
            content = cdn.get_content(url)
            print(content)
        elif command == 'exit':
            break
        else:
            print("Comando inválido")

if __name__ == "__main__":
    main()
