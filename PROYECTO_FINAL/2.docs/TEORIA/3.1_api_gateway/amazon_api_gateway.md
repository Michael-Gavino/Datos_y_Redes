# Teoría sobre Amazon API Gateway

Amazon API Gateway es un servicio completamente administrado que facilita la creación, publicación, mantenimiento, monitoreo y protección de APIs RESTful y WebSocket a cualquier escala. Permite a los desarrolladores crear interfaces de programación que actúan como "puertas de enlace" para conectarse con aplicaciones y servicios detrás de ellas.

## Interacción con Otros Servicios de AWS

### Integración con AWS Lambda:

**Funciones Lambda:** API Gateway puede integrarse directamente con funciones Lambda, lo que permite ejecutar código sin servidor en respuesta a las solicitudes de la API.

**Uso en API Gateway:** Se configura un método de integración en API Gateway que invoca una función Lambda específica en respuesta a las solicitudes de la API. Esto permite implementar lógica empresarial personalizada, realizar transformaciones de datos y ejecutar operaciones adicionales antes de enviar una respuesta al cliente.

### Integración con Amazon DynamoDB:

**Base de Datos NoSQL:** API Gateway también puede integrarse con DynamoDB para proporcionar almacenamiento de datos eficiente y escalable para aplicaciones.

**Uso en API Gateway:** Se puede configurar una integración directa para que los métodos de la API Gateway interactúen con tablas DynamoDB. Esto facilita la creación de APIs que accedan, almacenen y manipulen datos en DynamoDB de manera eficiente.

