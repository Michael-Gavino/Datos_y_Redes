## EJERCICIO 1

# Teoría sobre Amazon API Gateway

Amazon API Gateway es un servicio completamente administrado que facilita la creación, publicación, mantenimiento, monitoreo y protección de APIs RESTful y WebSocket a cualquier escala. Permite a los desarrolladores crear interfaces de programación que actúan como "puertas de enlace" para conectarse con aplicaciones y servicios detrás de ellas.

## Interacción con Otros Servicios de AWS

### Integración con AWS Lambda:

**Funciones Lambda:** API Gateway puede integrarse directamente con funciones Lambda, lo que permite ejecutar código sin servidor en respuesta a las solicitudes de la API.

**Uso en API Gateway:** Se configura un método de integración en API Gateway que invoca una función Lambda específica en respuesta a las solicitudes de la API. Esto permite implementar lógica empresarial personalizada, realizar transformaciones de datos y ejecutar operaciones adicionales antes de enviar una respuesta al cliente.

### Integración con Amazon DynamoDB:

**Base de Datos NoSQL:** API Gateway también puede integrarse con DynamoDB para proporcionar almacenamiento de datos eficiente y escalable para aplicaciones.

**Uso en API Gateway:** Se puede configurar una integración directa para que los métodos de la API Gateway interactúen con tablas DynamoDB. Esto facilita la creación de APIs que accedan, almacenen y manipulen datos en DynamoDB de manera eficiente.

## EJERCICIO 2

### Diseñar y Crear una API REST Utilizando Amazon API Gateway

Crear una API REST utilizando Amazon API Gateway implica varios conceptos y componentes clave que deben ser entendidos y configurados adecuadamente. A continuación, se presenta una explicación detallada de los aspectos teóricos involucrados en el proceso.

#### Conceptos Clave:

1. **API REST (Representational State Transfer)**:
   - Es un estilo arquitectónico para diseñar servicios web. En una API REST, los recursos (como productos, usuarios, etc.) son accesibles a través de URLs y se manipulan mediante métodos HTTP estándar como GET, POST, PUT y DELETE.

2. **Amazon API Gateway**:
   - Es un servicio totalmente gestionado que facilita la creación, publicación, mantenimiento, monitoreo y protección de APIs a cualquier escala. Con API Gateway, los desarrolladores pueden crear APIs RESTful que actúan como "puerta de entrada" para aplicaciones que acceden a datos o funcionalidad desde el backend, como aplicaciones alojadas en AWS Lambda, instancias de Amazon EC2 o cualquier otro servicio web.

3. **Recursos y Métodos**:
   - En Amazon API Gateway, un recurso es una entidad identificada por una URL, como `/products` o `/products/{id}`. Un método es una operación HTTP aplicada a un recurso, como GET, POST, PUT o DELETE.

4. **Integraciones Backend**:
   - API Gateway permite integrar recursos y métodos con varios tipos de backend, incluyendo AWS Lambda, DynamoDB, HTTP endpoints y otros servicios de AWS. La integración define cómo se transforman y transmiten las solicitudes y respuestas entre API Gateway y el backend.

5. **Etapas de Despliegue**:
   - Una etapa de despliegue en API Gateway representa un entorno (como desarrollo, prueba o producción) en el cual se implementa y gestiona una versión de la API. Cada etapa tiene una URL única para acceder a los recursos y métodos definidos.

6. **Control de Acceso**:
   - API Gateway proporciona múltiples mecanismos para controlar el acceso a las APIs, incluyendo claves API, políticas de IAM y Amazon Cognito. Estos mecanismos permiten proteger las APIs y controlar quién puede acceder a ellas y en qué capacidad.

#### Diseño de la API REST:

El diseño de una API REST eficaz implica definir claramente los recursos y los métodos que estos soportarán. En este caso, se está diseñando una API para gestionar productos con los siguientes endpoints:

- **GET /products**: Para obtener una lista de todos los productos disponibles.
- **GET /products/{id}**: Para obtener los detalles de un producto específico identificado por su ID.
- **POST /products**: Para crear un nuevo producto.
- **PUT /products/{id}**: Para actualizar los detalles de un producto existente identificado por su ID.
- **DELETE /products/{id}**: Para eliminar un producto específico identificado por su ID.

#### Integraciones Backend:

Para cada uno de estos métodos, es crucial definir cómo se integrarán con el backend:

1. **GET /products**:
   - Puede integrarse con una función AWS Lambda que realiza una operación de escaneo en una tabla de DynamoDB para recuperar todos los productos.

2. **GET /products/{id}**:
   - Puede integrarse con una función Lambda que realiza una operación de obtención en una tabla de DynamoDB para recuperar los detalles de un producto específico.

3. **POST /products**:
   - Puede integrarse con una función Lambda que realiza una operación de inserción en una tabla de DynamoDB para crear un nuevo producto.

4. **PUT /products/{id}**:
   - Puede integrarse con una función Lambda que realiza una operación de actualización en una tabla de DynamoDB para modificar los detalles de un producto existente.

5. **DELETE /products/{id}**:
   - Puede integrarse con una función Lambda que realiza una operación de eliminación en una tabla de DynamoDB para eliminar un producto específico.

#### Etapas de Despliegue:

Una vez definidos los recursos y métodos, y configuradas las integraciones backend, la API debe ser desplegada en una o más etapas. Las etapas comunes incluyen:

- **Desarrollo (dev)**: Para pruebas iniciales y desarrollo de nuevas funcionalidades.
- **Pruebas (test)**: Para pruebas más rigurosas, típicamente realizadas por un equipo de pruebas independiente.
- **Producción (prod)**: Para la versión final que será utilizada por los usuarios finales.

Cada etapa tiene su propia URL base y puede tener configuraciones específicas como límites de tasa de solicitudes, caché y monitoreo.

#### Control de Acceso:

1. **Claves API**:
   - Las claves API pueden ser utilizadas para controlar el acceso a la API. Cada cliente puede recibir una clave API única que debe ser incluida en las solicitudes para autenticarse.

2. **Políticas de IAM**:
   - Las políticas de IAM permiten definir permisos granulares para usuarios y roles de AWS. Estas políticas pueden controlar quién puede invocar los métodos de la API y con qué permisos.

3. **Amazon Cognito**:
   - Cognito proporciona una solución completa para la autenticación y gestión de usuarios. Puede integrarse con API Gateway para autenticar y autorizar usuarios finales.

#### Monitoreo y Optimización:

1. **Amazon CloudWatch**:
   - CloudWatch se puede utilizar para monitorear las métricas de la API, como el número de solicitudes, la latencia y los errores. Esto permite detectar y diagnosticar problemas de rendimiento y disponibilidad.

2. **Caché**:
   - API Gateway permite configurar caché en las respuestas de la API para mejorar la latencia y reducir la carga en el backend. El caché puede ser configurado por método y se puede invalidar según sea necesario.

#### Resumen:

Diseñar y crear una API REST utilizando Amazon API Gateway implica definir claramente los recursos y métodos, configurar integraciones backend, desplegar la API en diferentes etapas y establecer mecanismos de control de acceso y monitoreo. Este proceso asegura que la API sea escalable, segura y eficiente, proporcionando una experiencia de usuario óptima y facilitando el desarrollo y la gestión continua de la API.


## EJERCICIO 3

### Ejercicio 3: Integración con Lambda y DynamoDB

#### Objetivo
Integrar Amazon API Gateway con AWS Lambda para manejar las solicitudes y con DynamoDB para almacenar datos del inventario.

#### Tareas

1. **Crear una tabla DynamoDB para almacenar los productos del inventario**:
   - **Nombre de la tabla**: `TablaDynamoDB`
   - **Clave primaria**: `id` (tipo String)

2. **Escribir funciones Lambda en Python para manejar cada uno de los endpoints de la API**:
   - **Crear producto (POST /products)**: Esta función Lambda debe insertar un nuevo ítem en la tabla DynamoDB.
   - **Obtener todos los productos (GET /products)**: Esta función Lambda debe escanear la tabla DynamoDB y devolver todos los ítems.
   - **Obtener producto por ID (GET /products/{id})**: Esta función Lambda debe utilizar la clave primaria (`id`) para obtener un ítem específico de la tabla.
   - **Actualizar producto por ID (PUT /products/{id})**: Esta función Lambda debe actualizar un ítem específico en la tabla utilizando su `id`.
   - **Eliminar producto por ID (DELETE /products/{id})**: Esta función Lambda debe eliminar un ítem específico de la tabla utilizando su `id`.

3. **Configurar Amazon API Gateway para invocar las funciones Lambda correspondientes para cada endpoint**:
   - Crear la API en API Gateway.
   - Definir los recursos y métodos para cada endpoint (GET, POST, PUT, DELETE).
   - Configurar la integración de los métodos con las funciones Lambda.
   - Asegurarse de que API Gateway tenga los permisos necesarios para invocar las funciones Lambda.

#### Pasos Detallados

1. **Crear la tabla DynamoDB**:
   - Usar la consola de DynamoDB o AWS CloudFormation para crear una tabla con el nombre `TablaDynamoDB`.
   - Definir `id` como la clave primaria de tipo String.

2. **Escribir las funciones Lambda**:
   - Crear una función Lambda para cada endpoint (crear, obtener todos, obtener por ID, actualizar por ID, eliminar por ID).
   - Usar Python como lenguaje de programación para las funciones Lambda.
   - Configurar las funciones Lambda para interactuar con DynamoDB utilizando el SDK de AWS (`boto3`).

3. **Configurar Amazon API Gateway**:
   - Crear una nueva API REST en Amazon API Gateway.
   - Definir recursos y métodos correspondientes a cada endpoint:
     - `/products` con métodos GET y POST.
     - `/products/{id}` con métodos GET, PUT, DELETE.
   - Integrar cada método con la función Lambda correspondiente.
   - Configurar los permisos necesarios para que API Gateway pueda invocar las funciones Lambda.

### Resumen de la Integración

- **Amazon API Gateway**: Actúa como el punto de entrada para las solicitudes HTTP y dirige las solicitudes a las funciones Lambda correspondientes.
- **AWS Lambda**: Maneja la lógica de negocio para cada endpoint de la API. Interactúa con DynamoDB para realizar operaciones CRUD.
- **Amazon DynamoDB**: Almacena los datos del inventario. Cada ítem en la tabla representa un producto con atributos como `id`, `nombre`, y `cantidad`.


## EJERCICIO 4

### Ejercicio 4: Despliegue de la API

#### Objetivo
Desplegar la API en Amazon API Gateway para que esté accesible públicamente.

#### Tareas

1. **Configurar y desplegar la API en un entorno de desarrollo (stage) en Amazon API Gateway**:
   - Crear un nuevo stage en API Gateway para la API (por ejemplo, "dev").
   - Configurar el stage con las opciones de despliegue necesarias.
   - Desplegar la API al stage configurado para hacerla accesible públicamente.

2. **Probar la API utilizando herramientas como Postman o cURL**:
   - Usar Postman o cURL para enviar solicitudes HTTP a cada uno de los endpoints de la API.
   - Verificar que todos los endpoints (GET, POST, PUT, DELETE) funcionan correctamente y que las respuestas son las esperadas.

### Resumen del Despliegue

- **Amazon API Gateway**: Gestiona el despliegue de la API y la hace accesible a través de un URL público.
- **Stage de Desarrollo**: Un entorno de despliegue configurado para pruebas y desarrollo antes de mover la API a producción.
- **Herramientas de Prueba**: Postman y cURL se utilizan para enviar solicitudes HTTP y verificar que la API funciona correctamente.

Este ejercicio se centra en la configuración, despliegue y prueba de la API, asegurando que esté lista para su uso público.

## EJERCICIO 5

### Ejercicio 5: Control de acceso a la API REST

#### Objetivo
Implementar mecanismos de control de acceso para asegurar la API.

#### Tareas

1. **Investigar los diferentes métodos de autenticación y autorización disponibles en Amazon API Gateway**:
   - **API Keys**:
     - **Descripción**: Un método sencillo de autenticación que requiere que los usuarios proporcionen una clave API para acceder a los endpoints protegidos.
     - **Uso**: Adecuado para controlar el acceso a la API en aplicaciones donde se necesita un control básico y directo.
   - **IAM (Identity and Access Management)**:
     - **Descripción**: Utiliza políticas de IAM para controlar quién puede acceder a la API y qué acciones pueden realizar.
     - **Uso**: Ideal para controlar el acceso a la API en entornos donde se necesita una administración detallada y granular basada en usuarios y roles de AWS.
   - **Amazon Cognito**:
     - **Descripción**: Proporciona autenticación de usuarios y autorización mediante grupos de usuarios y federación de identidades.
     - **Uso**: Apropiado para aplicaciones que requieren una gestión completa de usuarios, incluyendo el registro, inicio de sesión, y la integración con proveedores de identidad externos (como Google, Facebook, etc.).

2. **Configurar el control de acceso para que solo usuarios autenticados puedan acceder a ciertos endpoints de la API**:
   - **API Keys**:
     - Crear y habilitar API Keys en API Gateway.
     - Asociar las API Keys con los endpoints específicos que necesitan protección.
   - **IAM**:
     - Crear políticas de IAM que definan los permisos necesarios para acceder a los endpoints.
     - Asociar las políticas con los roles o usuarios que necesitarán acceso a la API.
   - **Amazon Cognito**:
     - Configurar un grupo de usuarios (User Pool) en Amazon Cognito.
     - Configurar un proveedor de identidad (Identity Pool) si se necesita federación con otros proveedores de identidad.
     - Integrar Amazon Cognito con API Gateway para proteger los endpoints.

3. **Implementar y probar las políticas de acceso**:
   - **API Keys**:
     - Configurar los endpoints en API Gateway para requerir API Keys.
     - Probar el acceso enviando solicitudes HTTP con y sin la clave API.
   - **IAM**:
     - Configurar los endpoints en API Gateway para utilizar políticas de IAM.
     - Probar el acceso enviando solicitudes HTTP desde usuarios o roles con y sin los permisos adecuados.
   - **Amazon Cognito**:
     - Configurar los endpoints en API Gateway para utilizar Amazon Cognito para la autenticación.
     - Probar el acceso registrando usuarios en el grupo de usuarios, autenticándolos y enviando solicitudes HTTP con tokens de autenticación.

### Resumen de Métodos de Control de Acceso

- **API Keys**: Proporcionan una forma básica de autenticar a los usuarios mediante la clave API. Adecuado para escenarios simples.
- **IAM**: Ofrece un control detallado y granular mediante políticas de acceso basadas en usuarios y roles de AWS. Ideal para entornos con una administración de acceso compleja.
- **Amazon Cognito**: Facilita la gestión completa de usuarios y la autenticación con proveedores de identidad externos. Es ideal para aplicaciones que requieren una gestión avanzada de usuarios y autenticación federada.

### Proceso de Configuración y Prueba

1. **Configurar API Gateway**:
   - Habilitar el método de autenticación elegido en los endpoints de la API.
   - Configurar los detalles específicos del método de autenticación (como las claves API, políticas de IAM, o configuración de Cognito).

2. **Probar el Acceso**:
   - Enviar solicitudes a los endpoints protegidos utilizando las credenciales adecuadas.
   - Verificar que solo los usuarios autenticados y autorizados puedan acceder a los endpoints.

Esta implementación asegura que la API esté protegida y accesible solo para usuarios autenticados y autorizados, utilizando los métodos de autenticación y autorización disponibles en Amazon API Gateway.

## EJERCICIO 6

### Ejercicio 6: Monitoreo de la API REST

#### Objetivo
Configurar el monitoreo de la API para rastrear el uso y detectar posibles problemas.

#### Tareas

1. **Configurar CloudWatch para monitorear las métricas de la API**:
   - **Descripción**: Amazon CloudWatch es un servicio de monitoreo y observabilidad que proporciona datos y perspectivas procesables para AWS, aplicaciones y servicios. Se utiliza para monitorear métricas, recopilar y rastrear logs, y configurar alarmas.
   - **Métricas de API Gateway**:
     - **Número de solicitudes**: El número de solicitudes recibidas por la API.
     - **Latencia**: El tiempo que tarda la API en procesar las solicitudes.
     - **Errores**: El número de errores ocurridos en la API.
   - **Configuración**:
     - AWS API Gateway está integrado con CloudWatch, lo que permite que las métricas se envíen automáticamente.
     - Para habilitar el monitoreo detallado, se puede usar la consola de API Gateway o configurar las métricas en CloudFormation o Terraform.

2. **Crear dashboards en CloudWatch para visualizar estas métricas**:
   - **Descripción**: Un dashboard en CloudWatch permite visualizar y monitorear las métricas de la API en un solo lugar. Puedes agregar widgets que muestren gráficos, números y tablas basados en las métricas de CloudWatch.
   - **Pasos para crear un dashboard**:
     1. Navega a la consola de Amazon CloudWatch.
     2. Selecciona "Dashboards" en el menú de la izquierda y haz clic en "Create dashboard".
     3. Nombra el dashboard y selecciona "Create widget" para agregar widgets.
     4. Selecciona el tipo de widget (por ejemplo, gráfico de líneas, gráfico de barras, número, etc.) y configura las métricas que deseas monitorear (por ejemplo, latencia, número de solicitudes, errores).
     5. Repite el proceso para agregar más widgets según sea necesario y guarda el dashboard.

3. **Configurar alarmas para notificar en caso de que ciertas métricas excedan umbrales definidos**:
   - **Descripción**: Las alarmas de CloudWatch se utilizan para enviar notificaciones cuando las métricas monitoreadas superan o caen por debajo de los umbrales definidos. Esto ayuda a detectar y responder rápidamente a problemas potenciales.
   - **Pasos para configurar una alarma**:
     1. Navega a la consola de Amazon CloudWatch.
     2. Selecciona "Alarms" en el menú de la izquierda y haz clic en "Create alarm".
     3. Selecciona la métrica que deseas monitorear (por ejemplo, latencia, errores, número de solicitudes).
     4. Configura el umbral para la métrica. Por ejemplo, puedes configurar una alarma para que se dispare si la latencia supera los 500 ms.
     5. Define las acciones de la alarma, como enviar una notificación a través de Amazon SNS (Simple Notification Service) a un correo electrónico o un número de teléfono.
     6. Revisa y crea la alarma.

### Resumen de Configuración y Monitoreo

1. **Configurar métricas de API Gateway en CloudWatch**:
   - Habilitar el monitoreo de métricas como número de solicitudes, latencia y errores.
   - Utilizar la consola de API Gateway o herramientas de infraestructura como código (IaC) para configurar las métricas.

2. **Crear dashboards en CloudWatch**:
   - Utilizar la consola de CloudWatch para crear un dashboard y agregar widgets que muestren las métricas clave.
   - Personalizar el dashboard para incluir gráficos, números y tablas que faciliten la visualización de las métricas.

3. **Configurar alarmas en CloudWatch**:
   - Definir umbrales para las métricas monitoreadas.
   - Configurar notificaciones para alertar cuando las métricas excedan los umbrales definidos.
   - Utilizar Amazon SNS para enviar notificaciones por correo electrónico o mensaje de texto.

Esta configuración permite monitorear efectivamente el desempeño de la API, visualizar las métricas clave en dashboards y recibir notificaciones proactivas sobre posibles problemas, asegurando una respuesta rápida y efectiva a cualquier incidente.


EJERCICIO 7

### Optimización del Rendimiento de Amazon API Gateway

#### Objetivo
Optimizar el rendimiento de Amazon API Gateway para manejar grandes volúmenes de tráfico de manera eficiente.

#### Tareas

1. **Investigar las mejores prácticas para optimizar el rendimiento de Amazon API Gateway**:
   - **Descripción**: Amazon API Gateway es escalable y puede manejar grandes volúmenes de tráfico, pero es crucial implementar las mejores prácticas para optimizar su rendimiento.
   - **Mejores Prácticas**:
     - **Uso de Caching**: Implementar caching para reducir la latencia de las respuestas y minimizar la carga en los backends. Esto almacena temporalmente las respuestas de los endpoints en CloudFront o en la memoria de API Gateway.
     - **Configuración de Escalado Automático**: Utilizar configuraciones automáticas de escalado para ajustar la capacidad de API Gateway según la demanda.
     - **Optimización de Integraciones**: Ajustar las integraciones con Lambda o servicios backend para minimizar el tiempo de procesamiento.
     - **Control de Acceso y Seguridad**: Implementar políticas de acceso y seguridad adecuadas para proteger la API y mantener el rendimiento.
     - **Monitoreo y Optimización Continua**: Utilizar CloudWatch para monitorear métricas clave y ajustar configuraciones según sea necesario.

2. **Implementar caching en API Gateway para mejorar la latencia de las respuestas**:
   - **Descripción**: Implementar caching en API Gateway puede mejorar significativamente la latencia de las respuestas al almacenar en caché las respuestas de los endpoints.
   - **Pasos para implementar caching**:
     1. Navega a la consola de Amazon API Gateway.
     2. Selecciona tu API y navega a la sección de **Stages**.
     3. Haz clic en el nombre del **Stage**.
     4. Configura el **Cache Settings** para habilitar y configurar el caching.
     5. Define el TTL (Time-to-Live) y el tamaño de la caché según tus necesidades.
     6. Guarda los cambios para aplicar la configuración de caching.

3. **Ajustar la configuración de la API para manejar grandes volúmenes de tráfico de manera eficiente**:
   - **Descripción**: Ajustar la configuración de API Gateway es crucial para manejar grandes volúmenes de tráfico de manera eficiente y escalable.
   - **Consideraciones**:
     - **Escalado Automático**: Configurar la capacidad de escalar automáticamente para manejar picos de tráfico sin degradación del rendimiento.
     - **Optimización de Integraciones**: Ajustar los timeouts, ajustes de conexión y configuraciones de caché para maximizar la eficiencia.
     - **Implementación de Políticas de Throttling**: Utilizar políticas de throttling para controlar la tasa de solicitudes y proteger los backends de sobrecargas.

### Resumen

Optimizar Amazon API Gateway para manejar grandes volúmenes de tráfico implica implementar caching para reducir la latencia, configurar escalado automático para manejar picos de tráfico, y ajustar configuraciones para optimizar el rendimiento general. Al seguir las mejores prácticas y configuraciones recomendadas, se garantiza un rendimiento óptimo y una experiencia eficiente para los usuarios de la API.




