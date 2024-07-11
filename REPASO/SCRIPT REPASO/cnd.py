class CDN:
    def __init__(self):
        self.cache = {}

    def get_content(self, url):
        if url in self.cache:
            print("Contenido servido desde la caché")
            return self.cache[url]
        else:
            content = self.fetch_from_origin(url)
            self.cache[url] = content
            return content

    def fetch_from_origin(self, url):
        print("Obteniendo contenido desde el servidor de origen...")
        # Simular tiempo de respuesta del servidor de origen
        # time.sleep(2)  # Esta línea normalmente estaría aquí para simular el tiempo de respuesta
        return f"Contenido de {url}"

# Crear una instancia de CDN
cdn = CDN()

# Solicitar contenido
print(cdn.get_content("https://example.com/image.png"))
print(cdn.get_content("https://example.com/image.png"))
