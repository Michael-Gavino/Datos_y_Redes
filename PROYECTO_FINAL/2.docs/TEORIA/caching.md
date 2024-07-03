# TEORIA DE CACHING

### ¿Qué es Caché?

El caché es un mecanismo de almacenamiento de datos que permite el acceso rápido a la información previamente solicitada, reduciendo el tiempo necesario para recuperar datos desde la fuente original. Es una memoria de alta velocidad que almacena temporalmente los datos más frecuentemente accedidos, mejorando así el rendimiento y la eficiencia de sistemas y aplicaciones.

#### Características Clave del Caché:

1. **Velocidad:**
   - El caché está diseñado para ser mucho más rápido que la memoria principal o el almacenamiento en disco, permitiendo tiempos de acceso más cortos.

2. **Temporalidad:**
   - Los datos en caché se almacenan temporalmente y pueden ser reemplazados o invalidados según las políticas de caché y las necesidades del sistema.

3. **Frecuencia de Acceso:**
   - Almacena datos que se acceden con mayor frecuencia, optimizando el rendimiento al reducir la necesidad de recuperar datos desde la fuente original repetidamente.

4. **Localidad:**
   - Utiliza los principios de localidad temporal y espacial, que se basan en la observación de que los datos recientemente accedidos o cercanos en la memoria son más propensos a ser solicitados nuevamente.

#### Tipos de Caché:

1. **Caché de Memoria:**
   - Utilizado por la CPU para almacenar instrucciones y datos recientemente usados. Se subdivide en diferentes niveles (L1, L2, L3) según su proximidad y velocidad relativa a la CPU.

2. **Caché de Disco:**
   - Almacena temporalmente los datos leídos del disco duro, mejorando el rendimiento del acceso a datos almacenados en dispositivos de almacenamiento más lentos.

3. **Caché de Web:**
   - Almacena contenido web (páginas, imágenes, archivos) para reducir el tiempo de carga de las páginas web y el uso de ancho de banda.

4. **Caché de Base de Datos:**
   - Almacena los resultados de las consultas de bases de datos, mejorando el rendimiento de aplicaciones que realizan consultas repetitivas.

#### Ventajas del Caché:

1. **Mejora del Rendimiento:**
   - Reduce significativamente los tiempos de acceso a los datos, mejorando el rendimiento general del sistema o aplicación.

2. **Reducción de Carga:**
   - Disminuye la carga en los recursos originales (como discos duros o bases de datos) al satisfacer las solicitudes de datos desde el caché.

3. **Ahorro de Ancho de Banda:**
   - En el contexto de redes, el caché de web puede reducir el uso de ancho de banda al almacenar copias locales de los datos solicitados con frecuencia.

4. **Escalabilidad:**
   - Facilita la escalabilidad de aplicaciones y sistemas al proporcionar acceso rápido a datos críticos sin aumentar la carga en la infraestructura original.


#### Ejemplo Práctico en Amazon API Gateway:

En el contexto de Amazon API Gateway, el caché se utiliza para almacenar las respuestas de las API, mejorando el rendimiento al reducir la necesidad de procesar repetidamente las mismas solicitudes. Los datos en caché pueden configurarse para expir

