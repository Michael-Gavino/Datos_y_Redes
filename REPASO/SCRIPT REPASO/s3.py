import os

class AlmacenamientoEnBloque:
    def __init__(self, tamaño):
        self.almacenamiento = bytearray(tamaño)
    
    def escribir(self, datos, offset):
        self.almacenamiento[offset:offset+len(datos)] = datos.encode('utf-8')

    def leer(self, offset, tamaño):
        return self.almacenamiento[offset:offset+tamaño].decode('utf-8')

# Ejemplo de uso
almacenamiento_en_bloque = AlmacenamientoEnBloque(1024)
almacenamiento_en_bloque.escribir("Hello World", 0)
print(almacenamiento_en_bloque.leer(0, 5))  



class AlmacenamientoDeArchivos:
    def __init__(self, directorio_raiz):
        self.directorio_raiz = directorio_raiz
        os.makedirs(directorio_raiz, exist_ok=True)

    def escribir(self, ruta, datos):
        with open(os.path.join(self.directorio_raiz, ruta), 'w') as f:
            f.write(datos)
    
    def leer(self, ruta):
        with open(os.path.join(self.directorio_raiz, ruta), 'r') as f:
            return f.read()

# Ejemplo de uso
almacenamiento_de_archivos = AlmacenamientoDeArchivos('almacenamientodearchivos')
almacenamiento_de_archivos.escribir('ejemplo.txt', '¡Hola, Almacenamiento de Archivos!')
print(almacenamiento_de_archivos.leer('ejemplo.txt'))


class S3Bucket:
    def __init__(self):
        self.buckets = {}

    def create_bucket(self, name):
        self.buckets[name] = {}

    def put_object(self, bucket, key, data):
        if bucket in self.buckets:
            self.buckets[bucket][key] = data

    def get_object(self, bucket, key):
        return self.buckets.get(bucket, {}).get(key, None)
# Ejemplo de uso
s3 = S3Bucket()
s3.create_bucket('mybucket')
s3.put_object('mybucket', 'file1.txt', 'Hello, S3 Bucket!')
print(s3.get_object('mybucket', 'file1.txt')) 

