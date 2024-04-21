# Actividad 7 : Investigación de los modelos TCP/IP y OSI

## Objetivos

**Parte 1: Examinar el tráfico web HTTP**

**Parte 2: Mostrar elementos de la suite de protocolos TCP/IP**

Utiliza el archivo .pka que acompaña la actividad.

## Aspectos básicos

Esta actividad de simulación tiene como objetivo proporcionar una base para comprender la suite de protocolos TCP/IP y la relación con el modelo OSI. El modo de simulación le permite ver el contenido de los datos que se envían a través de la red en cada capa.

A medida que los datos se desplazan por la red, se dividen en partes más pequeñas y se identifican de modo que las piezas se puedan volver a unir cuando lleguen al destino. A cada pieza se le asigna un nombre específico (unidad de datos del protocolo [PDU]) y se la asocia a una capa específica de los modelos TCP/IP y OSI. El modo de simulación de Packet Tracer te permite ver cada una de las capas y la PDU asociada. Los siguientes pasos te guían a través del proceso de solicitud de una página web desde un servidor web mediante la aplicación de navegador web disponible en una PC cliente.

## Instrucciones

### 1. Examinar el tráfico web HTTP

En la parte 1 de esta actividad, utilizarás el modo de simulación de Packet Tracer (PT) para generar tráfico web y examinar HTTP.

**Cambia del modo de tiempo real al modo de simulación:**

- Haz clic en el ícono del modo de Simulación para cambiar del modo de Tiempo real al modo de Simulación.
- Selecciona HTTP en Filtros de lista de eventos.

  - Es posible que HTTP ya sea el único evento visible. Si es necesario, haz clic en el botón Editar filtros en la parte inferior del panel de simulación para mostrar los eventos visibles disponibles. Alterna la casilla de verificación Mostrar todo/ninguno y observa cómo las casillas de verificación se desactivan y se activan, o viceversa, según el estado actual.
  - Haz clic en la casilla de verificación Mostrar todo/ninguno hasta que se desactiven todas las casillas y luego selecciona HTTP. Haz clic en la X situada en la esquina superior derecha de la ventana para cerrar la ventana Editar filtros. Los eventos visibles ahora deben mostrar sólo HTTP.

**Genera tráfico web (HTTP):**

Actualmente, el panel de simulación está vacío. En la parte superior de Lista de eventos dentro del panel de simulación, se indican cinco columnas. A medida que se genera y se revisa el tráfico, aparecen los eventos en la lista.

Nota: el servidor web y el cliente web se muestran en el panel de la izquierda. Se puede ajustar el tamaño de los paneles manteniendo el mouse junto a la barra de desplazamiento y arrastrando a la izquierda o a la derecha cuando aparece la flecha de dos puntas.

- Haz clic en Cliente web en el panel del extremo izquierdo.
- Haz clic en la ficha Escritorio y luego en el ícono Navegador web para abrirlo.
- En el campo de dirección URL, introduce www.osi.local y haga clic en Ir.

Debido a que el tiempo en el modo de simulación se desencadena por eventos, debes usar el botón Capturar/avanzar para mostrar los eventos de red. El botón de captura hacia adelante se encuentra en el lado izquierdo de la banda azul que está debajo de la ventana de topología. De los tres botones, es el de la derecha.

- Haz clic en Capturar/Avanzar cuatro veces. Deberías haber cuatro eventos en la Lista de eventos.

**Pregunta:**

Observa la página del navegador web del cliente web. ¿Cambió algo?

Escriba sus respuestas aquí.

**Explora el contenido del paquete HTTP:**

- Haz clic en el primer cuadro coloreado debajo de la columna Lista de eventos > Información. Quizá sea necesario expandir el panel de simulación o usar la barra de desplazamiento que se encuentra directamente debajo de la lista de eventos.

Se muestra la ventana Información de PDU en dispositivo: cliente web. En esta ventana, solo hay dos fichas, (Modelo OSI y Detalles de PDU saliente), debido a que este es el inicio de la transmisión. A medida que se analizan más eventos, se muestran tres fichas, ya que se agrega la ficha Detalles de PDU entrante. Cuando un evento es el último evento de la transmisión de tráfico, solo se muestran las fichas Modelo OSI y Detalles de PDU entrante.

- Asegúrate de que esté seleccionada la ficha Modelo OSI.
  - En la columna Capas de salida, haz clic en Capa 7.

**Preguntas:**

1. ¿Qué información se indica en los pasos numerados directamente debajo de los cuadros Capas de entrada y Capas de salida?
2. ¿Cuál es el valor del puerto Dst para la capa 4 en la columna Capas de salida?
3. ¿Cuál es el destino? ¿Valor IP para la Capa 3 en la columna Capas de salida?
4. ¿Qué información se muestra en la Capa 2 en la columna Capas de salida?
5. ¿Cuál es la información frecuente que se indica en la sección IP de detalles de PDU comparada con la información que se indica en la ficha Modelo OSI? ¿Con qué capa se relaciona?
6. ¿Cuál es el host que se indica en la sección HTTP de Detalles de PDU? ¿Con qué capa se relacionaría esta información en la ficha Modelo OSI?

- Haz clic en la ficha de Detalles de la PDU saliente.

**Preguntas:**

7. ¿Cuál es la información frecuente que se indica en la sección IP de Detalles de PDU comparada con la información que se indica en la ficha Modelo OSI?
8. ¿Qué información se indica en NOMBRE: en la sección CONSULTA DNS?

- Haz clic en el primer cuadro coloreado debajo de la columna Lista de eventos > Tipo. Solo la capa 1 está activa (sin atenuar). El dispositivo mueve el frame desde el búfer y la coloca en la red.
- Avanza al siguiente cuadro Tipo de HTTP dentro de la lista de eventos y haz clic en el cuadro coloreado. Esta ventana contiene las columnas Capas de entrada y Capas de salida. Observa la dirección de la flecha que está directamente debajo de la columna Capas de entrada; esta apunta hacia arriba, lo que indica la dirección en la que se transfiere la información. Desplázate por estas capas y toma nota de los elementos vistos anteriormente. En la parte superior de la columna, la flecha apunta hacia la derecha. Esto indica que el servidor ahora envía la información de regreso al cliente. Compara la información que se muestra en la columna Capas de entrada con la de la columna Capas de salida: ¿cuáles son las diferencias principales?
- Haz clic en la ficha Inbound PDU Details (Detalles de PDU entrante). Revisa los detalles de la PDU.
- Haz clic en el último cuadro coloreado de la columna Información. Explica los resultados.

### 2. Mostrar elementos de la suite de protocolos TCP/IP

En la parte 2 de esta actividad, utilizarás el modo de simulación de Packet Tracer para ver y examinar algunos de los otros protocolos que componen la suite TCP/IP.

**Ver eventos adicionales:**

- Cierra todas las ventanas de información de PDU abiertas.
- En la sección Filtros de lista de eventos > Eventos visibles, haz clic en Mostrar todo.

**Pregunta:**

¿Qué tipos de eventos adicionales se muestran?

Estas entradas adicionales cumplen diversas funciones dentro de la suite TCP/IP. El Protocolo de resolución de direcciones (ARP) solicita direcciones MAC para los hosts de destino. El protocolo DNS es responsable de convertir un nombre (por ejemplo, www.osi.local) a una dirección IP. Los eventos de TCP adicionales son responsables de la conexión, del acuerdo de los parámetros de comunicación y de la desconexión de las sesiones de comunicación entre los dispositivos.

- Haz clic en el primer evento de DNS en la columna Información. Examina las fichas Modelo OSI y Detalles de PDU, y observa el proceso de encapsulamiento. Al observar la ficha Modelo OSI con el cuadro capa 7 resaltado, se incluye una descripción de lo que ocurre, inmediatamente debajo de las Capas de entrada y las Capas de salida: (“1. The DNS client sends a DNS query to the DNS server.” [“El cliente DNS envía una consulta DNS al servidor DNS”]). Esta información es muy útil para ayudarte a comprender qué ocurre durante el proceso de comunicación.
- Haz clic en la ficha de Detalles de la PDU saliente.

**Pregunta:**

¿Qué información se indica en NOMBRE: en la sección CONSULTA DNS?

- Haz clic en el último cuadro coloreado Información de DNS en la lista de eventos.

**Preguntas:**

1. ¿En qué dispositivo se capturó la PDU?
2. ¿Cuál es el valor que se indica junto a DIRECCIÓN: en la sección RESPUESTA DE DNS de Detalles de la PDU entrante?

- Busca el primer evento de HTTP en la lista y haga clic en el cuadro coloreado del evento de TCP que le sigue inmediatamente a este evento. Resalte capa 4 en la ficha Modelo OSI.

**Pregunta:**

¿En la lista numerada que está directamente debajo de Capas de entrada y Capas de salida, cuál es la información que se muestra en los elementos 4 y 5?. El protocolo TCP administra la conexión y la desconexión del canal de comunicaciones, además de tener otras responsabilidades. Este evento específico muestra que SE ESTABLECIÓ el canal de comunicaciones.

- Haz clic en el último evento de TCP. Resalte capa 4 en la ficha Modelo OSI. Examine los pasos que se indican directamente a continuación de Capas de entrada y Capas de salida.

**Pregunta:**

¿Cuál es el propósito de este evento, según la información proporcionada en el último elemento de la lista (debe ser el elemento 4)?

**Preguntas finales:**

En esta simulación, se proporcionó un ejemplo de una sesión web entre un cliente y un servidor en una red de área local (LAN). El cliente realiza solicitudes de servicios específicos que se ejecutan en el servidor. Se debe configurar el servidor para que escuche puertos específicos y detecte una solicitud de cliente. (Sugerencia: observe la capa 4 en la ficha Modelo OSI para obtener información del puerto).

- Sobre la base de la información que se analizó durante la captura de Packet Tracer, ¿qué número de puerto escucha el servidor web para detectar la solicitud web?
- ¿Qué puerto escucha el servidor web para detectar una solicitud de DNS?


