# Problema 7: Cache de red

#### Conceptos: Cache de red, Protocolo de cache, Eficiencia de red

Crea una función que simule un cache de red simple. Esta función deberá almacenar resultados de operaciones o datos frecuentemente accesados y servirlos rápidamente sin necesidad de una nueva operación de red.

Implementa un mecanismo de cache utilizando diccionarios.
Demostrar la mejora en eficiencia al evitar operaciones repetidas.

```python
cache_de_red = {}

def obtener_datos_desde_cache(identificador):
    """Obtiene datos del caché si están disponibles."""
    if identificador in cache_de_red:
        print(f"Datos obtenidos desde el caché para: {identificador}")
        return cache_de_red[identificador]
    else:
        print(f"No se encontraron datos en el caché para: {identificador}")
        return None

def almacenar_cache(identificador, datos):
    """Almacena datos en el caché."""
    cache_de_red[identificador] = datos
    print(f'Datos almacenados en el caché para: {identificador}')

def identicar_datos(identificador):
    print(f'Obteniendo datos desde el caché para: {identificador}')
    return obtener_datos_desde_cache(identificador)
```
