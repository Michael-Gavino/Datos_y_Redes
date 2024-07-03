# TEORIA DE API REST

### ¿Qué es una API REST?

Una API REST (Representational State Transfer) es un tipo de interfaz de programación de aplicaciones (API) que sigue principios y restricciones de diseño arquitectónico específicos para la comunicación y la manipulación de recursos a través de un servicio web. REST es un estilo de arquitectura que se basa en el uso de HTTP para hacer solicitudes y obtener respuestas, y se ha convertido en una de las formas más populares para construir APIs debido a su simplicidad y escalabilidad.

#### Principios Clave de REST:

1. **Cliente-Servidor:**
   - La arquitectura REST se basa en una separación clara entre el cliente y el servidor, lo que permite que ambos evolucionen de manera independiente. El cliente realiza solicitudes y el servidor procesa estas solicitudes y devuelve las respuestas.

2. **Stateless (Sin Estado):**
   - Cada solicitud del cliente al servidor debe contener toda la información necesaria para entender y procesar la solicitud. Esto significa que el servidor no almacena información sobre el estado del cliente entre las solicitudes.

3. **Cacheable (Cacheable):**
   - Las respuestas deben definirse como cacheables o no cacheables, para mejorar el rendimiento mediante el almacenamiento en caché de respuestas reutilizables.

4. **Interfaz Uniforme:**
   - La interfaz uniforme simplifica y desacopla la arquitectura. Se basa en:
     - **Identificación de Recursos:** Los recursos se identifican mediante URLs (Uniform Resource Locators).
     - **Manipulación de Recursos a través de Representaciones:** Los clientes interactúan con los recursos mediante representaciones (por ejemplo, JSON, XML).
     - **Mensajes Autodescriptivos:** Cada mensaje debe tener suficiente información para describir cómo procesarlo.
     - **Hipermedia como el Motor del Estado de la Aplicación (HATEOAS):** Los clientes navegan por la API dinámicamente a través de hipervínculos proporcionados en las respuestas.

5. **Sistema en Capas:**
   - Una arquitectura REST puede estar compuesta de múltiples capas de servidores, cada una con una funcionalidad específica (por ejemplo, servidores de autenticación, servidores de almacenamiento).

#### Operaciones HTTP Comunes en una API REST:

1. **GET:**
   - Recupera información de un recurso específico.
   - Ejemplo: `GET /products` devuelve una lista de productos.

2. **POST:**
   - Crea un nuevo recurso.
   - Ejemplo: `POST /products` crea un nuevo producto.

3. **PUT:**
   - Actualiza un recurso existente.
   - Ejemplo: `PUT /products/{id}` actualiza el producto con el ID especificado.

4. **DELETE:**
   - Elimina un recurso específico.
   - Ejemplo: `DELETE /products/{id}` elimina el producto con el ID especificado.

5. **PATCH:**
   - Aplica modificaciones parciales a un recurso.
   - Ejemplo: `PATCH /products/{id}` aplica cambios parciales al producto con el ID especificado.

#### Ventajas de usar APIs REST:

1. **Simplicidad:**
   - REST usa HTTP estándar, que es ampliamente conocido y fácil de usar.

2. **Escalabilidad:**
   - La arquitectura sin estado facilita la escalabilidad horizontal.

3. **Flexibilidad y Portabilidad:**
   - REST permite la comunicación entre diferentes sistemas, independientemente de la tecnología subyacente.

4. **Mantenibilidad:**
   - La separación clara entre cliente y servidor facilita el desarrollo y mantenimiento de ambos lados.

En resumen, una API REST proporciona una forma estructurada y eficiente de interactuar con servicios web, facilitando la construcción de aplicaciones web escalables y mantenibles.
