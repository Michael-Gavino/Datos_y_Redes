class CDN:
    """
    Clase CDN (Content Delivery Network)
    ------------------------------------
    Simula el comportamiento básico de una red de entrega de contenido.
    Permite obtener contenido desde un servidor de origen y almacenarlo en una
    caché local para responder más rápido a solicitudes repetidas.

    Atributos:
        cache (dict): Almacena el contenido en caché, con la URL como clave y el contenido como valor.
    """

    def __init__(self):
        """
        Constructor de la clase CDN.
        Inicializa la caché como un diccionario vacío.
        """
        self.cache = {}

    def get_content(self, url):
        """
        Obtiene el contenido solicitado desde la caché o desde el servidor de origen.

        - Si la URL está en la caché, devuelve el contenido almacenado.
        - Si no está, obtiene el contenido del servidor de origen y lo guarda en la caché.

        Args:
            url (str): URL del contenido que se desea obtener.

        Returns:
            str: Contenido solicitado (desde la caché o el servidor).
        """
        if url in self.cache:
            # Si el contenido ya está almacenado en la caché, lo devuelve directamente
            print("✅ Contenido servido desde la caché")
            return self.cache[url]
        else:
            # Si el contenido no está en caché, lo obtiene del servidor de origen
            content = self.fetch_from_origin(url)
            # Luego, lo guarda en la caché para futuras solicitudes
            self.cache[url] = content
            return content

    def fetch_from_origin(self, url):
        """
        Simula la obtención del contenido desde el servidor de origen.

        Args:
            url (str): URL del contenido solicitado.

        Returns:
            str: Contenido simulado obtenido del servidor.
        """
        print("🌐 Obteniendo contenido desde el servidor de origen...")
        # Aquí normalmente podríamos simular el tiempo de respuesta con time.sleep(2)
        return f"Contenido de {url}"

# ----------------------------- USO DEL CDN -----------------------------

# Crear una instancia de la red de entrega de contenido (CDN)
cdn = CDN()

# Primera solicitud: el contenido no está en caché, se obtiene del servidor
print(cdn.get_content("https://example.com/image.png"))

# Segunda solicitud: el contenido ya está en caché, se devuelve sin ir al servidor
print(cdn.get_content("https://example.com/image.png"))
