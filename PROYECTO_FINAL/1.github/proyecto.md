## Departamento Académico de Ingeniería C8280 - Comunicación de Datos y Redes

# Proyecto: Desarrollo e implementación de una API REST con Amazon API Gateway

Este proyecto tiene como objetivo que los estudiantes desarrollen e implementen una API REST utilizando Amazon API Gateway, integrando diversos servicios de AWS y controlando el acceso a la API. Los estudiantes deberán usar AWS Lab Learner y Python para realizar todas las tareas requeridas.

## Introducción

El proyecto consiste en crear una API REST para un sistema de gestión de inventarios. Los estudiantes deberán implementar endpoints para realizar operaciones CRUD (Create, Read, Update, Delete) sobre los productos en el inventario, almacenar los datos en DynamoDB, y controlar el acceso a la API utilizando Amazon API Gateway.

## Ejercicio 1: Introducción a Amazon API Gateway

**Objetivo:** Comprender los conceptos básicos de Amazon API Gateway y cómo puede integrarse con otros servicios de AWS.

### Tareas:
- Investiga y documenta cómo Amazon API Gateway puede interactuar con otros servicios de AWS como Lambda y DynamoDB.
- Usa AWS Lab Learner y configurar las credenciales necesarias para utilizar boto3 en Python.

## Ejercicio 2: Creación de una API REST

**Objetivo:** Diseñar y crear una API REST utilizando Amazon API Gateway.

### Tareas:
- Diseña la estructura de la API REST que incluirá los siguientes endpoints:
  - GET /products: Obtener todos los productos.
  - GET /products/{id}: Obtener un producto por ID.
  - POST /products: Crear un nuevo producto.
  - PUT /products/{id}: Actualizar un producto por ID.
  - DELETE /products/{id}: Eliminar un producto por ID.
- Crear la API REST en Amazon API Gateway utilizando la consola de AWS o CloudFormation.

## Ejercicio 3: Integración con Lambda y DynamoDB

**Objetivo:** Integrar la API Gateway con Lambda para manejar las solicitudes y DynamoDB para almacenar los datos del inventario.

### Tareas:
- Crea una tabla DynamoDB para almacenar los productos del inventario.
- Escribe funciones Lambda en Python para manejar cada uno de los endpoints de la API.
  - La función Lambda para crear un producto debe insertar un nuevo ítem en la tabla DynamoDB.
  - La función Lambda para obtener todos los productos debe escanear la tabla DynamoDB y devolver los resultados.
  - La función Lambda para obtener, actualizar y eliminar un producto por ID debe utilizar la clave primaria de la tabla DynamoDB.
- Configura Amazon API Gateway para invocar las funciones Lambda correspondientes para cada endpoint.

## Ejercicio 4: Despliegue de la API

**Objetivo:** Desplegar la API en Amazon API Gateway para que esté accesible públicamente.

### Tareas:
- Configurar y desplegar la API en un entorno de desarrollo (stage) en Amazon API Gateway.
- Probar la API utilizando herramientas como Postman o cURL para asegurar que todos los endpoints funcionan correctamente.

## Ejercicio 5: Control de acceso a la API REST

**Objetivo:** Implementar mecanismos de control de acceso para asegurar la API.

### Tareas:
- Investigar los diferentes métodos de autenticación y autorización disponibles en Amazon API Gateway (API Keys, IAM, Cognito).
- Configurar el control de acceso para que solo usuarios autenticados puedan acceder a ciertos endpoints de la API.
- Implementar y probar las políticas de acceso.

## Ejercicio 6: Monitoreo de la API REST

**Objetivo:** Configurar el monitoreo de la API para rastrear el uso y detectar posibles problemas.

### Tareas:
- Configurar CloudWatch para monitorear las métricas de la API, como el número de solicitudes, latencia y errores.
- Crear dashboards en CloudWatch para visualizar estas métricas.
- Configurar alarmas para notificar en caso de que ciertas métricas excedan umbrales definidos.

## Ejercicio 7: Optimización de API Gateway

**Objetivo:** Optimizar el rendimiento de Amazon API Gateway para manejar grandes volúmenes de tráfico.

### Tareas:
- Investigar las mejores prácticas para optimizar el rendimiento de Amazon API Gateway.
- Implementar caching en API Gateway para mejorar la latencia de las respuestas.
- Ajustar la configuración de la API para manejar grandes volúmenes de tráfico de manera eficiente.

## Ejercicio 8: Desarrollo de API REST con Amazon API Gateway

**Objetivo:** Desarrollar un flujo completo de trabajo para el desarrollo de API REST utilizando Amazon API Gateway.

### Tareas:
- Integrar todos los componentes desarrollados en los ejercicios anteriores en un flujo de trabajo cohesivo.
- Documentar el flujo de trabajo y los pasos necesarios para implementar una API REST utilizando Amazon API Gateway.
- Crear un repositorio en GitHub con todo el código y la documentación necesaria para desplegar y manejar la API.
