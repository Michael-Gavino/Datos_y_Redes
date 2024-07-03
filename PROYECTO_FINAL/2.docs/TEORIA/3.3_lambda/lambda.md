# TEORIA DE FUNCION LAMBDA

### ¿Qué es AWS Lambda?

AWS Lambda es un servicio de computación sin servidor proporcionado por Amazon Web Services (AWS). Permite ejecutar código en respuesta a eventos sin necesidad de aprovisionar o gestionar servidores. AWS Lambda se encarga automáticamente del aprovisionamiento de la infraestructura, el escalado, la supervisión y la administración del entorno de ejecución, lo que permite a los desarrolladores concentrarse en escribir y desplegar código.

#### Características Clave de AWS Lambda:

1. **Sin Servidor (Serverless):**
   - No se necesita gestionar servidores. AWS Lambda maneja automáticamente la infraestructura necesaria para ejecutar el código, incluyendo el aprovisionamiento, el escalado y el mantenimiento de los servidores.

2. **Ejecución basada en Eventos:**
   - Lambda se activa en respuesta a eventos específicos. Estos eventos pueden provenir de una variedad de fuentes, como cambios en una base de datos, solicitudes HTTP a través de Amazon API Gateway, modificaciones en archivos en Amazon S3, o incluso disparadores personalizados definidos por el usuario.

3. **Escalado Automático:**
   - Lambda escala automáticamente en función de la carga de trabajo. Si hay muchas solicitudes, Lambda crea más instancias de la función para manejar el tráfico adicional, y reduce el número de instancias cuando la carga disminuye.

4. **Pagos por Uso:**
   - Solo se paga por el tiempo de ejecución de las funciones Lambda y la cantidad de solicitudes. Esto significa que no hay costos por tiempos de inactividad.

5. **Soporte Multilingüe:**
   - AWS Lambda soporta varios lenguajes de programación, incluyendo Node.js, Python, Ruby, Java, Go, y .NET. También permite la integración con contenedores Docker para ejecutar cualquier entorno de ejecución personalizado.

#### Componentes Principales:

1. **Funciones:**
   - Una función Lambda es una pieza de código que se ejecuta en respuesta a un evento. Cada función tiene su propio entorno de ejecución y configuración.

2. **Eventos:**
   - Un evento es cualquier acción que puede activar una función Lambda. Los eventos pueden ser solicitudes HTTP, cambios en una base de datos, cargas de archivos, etc.

3. **Roles y Permisos:**
   - AWS Lambda utiliza roles de AWS Identity and Access Management (IAM) para definir los permisos necesarios para ejecutar las funciones y acceder a otros recursos de AWS.

#### Casos de Uso Comunes:

1. **Procesamiento de Datos en Tiempo Real:**
   - Procesar datos a medida que se generan, como el análisis de flujos de datos en tiempo real provenientes de servicios como Amazon Kinesis o AWS IoT.

2. **Backend para Aplicaciones Web y Móviles:**
   - Lambda puede servir como backend para aplicaciones web y móviles, manejando solicitudes HTTP a través de Amazon API Gateway.

3. **Automatización de la Infraestructura:**
   - Realizar tareas de administración de la infraestructura, como la creación de copias de seguridad de bases de datos, limpieza de archivos temporales, y mantenimiento de instancias de servidor.

4. **Integración con otros Servicios de AWS:**
   - Ejecutar código en respuesta a eventos generados por otros servicios de AWS, como Amazon S3, DynamoDB, SNS, SQS, y más.

5. **Microservicios:**
   - Desarrollar aplicaciones basadas en microservicios donde cada función Lambda maneja una parte específica de la lógica de la aplicación.

En resumen, AWS Lambda es una poderosa herramienta para ejecutar código en la nube sin la necesidad de gestionar infraestructura. Su capacidad para escalar automáticamente, junto con el modelo de pago por uso, lo convierte en una opción atractiva para una amplia gama de aplicaciones y casos de uso.

