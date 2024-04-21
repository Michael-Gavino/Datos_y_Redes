# Actividad 8: Comunicaciones de TCP y UDP

## Objetivos

- Parte 1: Generar tráfico de red en el modo de simulación
- Parte 2: Examinar la funcionalidad de los protocolos TCP y UDP

## Aspectos básicos

Esta actividad de simulación está destinada a proporcionar una base para comprender TCP y UDP en detalle. El modo de simulación Packet Tracer le proporciona la capacidad de ver el estado de diferentes PDU a medida que viajan a través de la red.

El modo de simulación de Packet Tracer te permite ver cada uno de los protocolos y las PDU asociadas. Los pasos descritos a continuación lo guían a través del proceso de solicitud de servicios de red utilizando diversas aplicaciones que están disponibles en una PC cliente. Explorarás la funcionalidad de los protocolos TCP y UDP, la multiplexación y la función de los números de puerto para determinar qué aplicación local solicitó los datos o los envía.

## Instrucciones

1. Genera tráfico de red en modo de simulación y vea multiplexación

   Genera tráfico para completar las tablas del protocolo de resolución de direcciones (ARP):

   - Haz clic en MultiServer y luego haz click en Desktop tab > Command Prompt.
   - Ingresa el comando `ping -n 1 192.168.1.255`. Estás haciendo ping a la dirección broadcast de la LAN del cliente. La opción de comando enviará sólo una solicitud de ping en lugar de las cuatro habituales. Esto tomará unos segundos ya que cada dispositivo en la red responde a la solicitud de ping de MultiServer.
   - Cierra la ventana MultiServer.

   Genera tráfico web (HTTP):

   - Cambia a modo de simulación.
   - Haz clic en Cliente HTTP y abre el Explorador Web desde el escritorio.
   - En el campo URL, introduce `192.168.1.254` y haz clic en Go (Ir). Los sobres (PDU) aparecerán en la ventana de topología.
   - Minimiza, pero no cierres, la ventana de configuración de HTTP Client.

   Genera tráfico FTP:

   - Haz clic en FTP Client y abra el Command Prompt desde el escritorio.
   - Introduce el comando `ftp 192.168.1.254`. Las PDU aparecerán en la ventana de simulación.
   - Minimiza, pero no cierres, la ventana de configuración de FTP Client.

   Genera tráfico DNS:

   - Haz clic en DNS Client y abra el Command Prompt.
   - Introduce el comando `nslookup multiserver.pt.ptu`. Aparecerá una PDU en la ventana de simulación.
   - Minimiza, pero no cierre, la ventana de configuración de DNS Client.

   Genera tráfico de correo electrónico:

   - Haz clic en E-Mail Client y abre la herramienta E Mail desde el escritorio.
   - Haz clic en Compose (Redactar) y escribe la siguiente información:
     1) To: user@multiserver.pt.ptu
     2) Subject: Personalizar la línea de asunto
     3) E-Mail Body: personalizar el correo electrónico
   - Haz clic en Send (Enviar).
   - Minimiza, pero no cierres, la ventana de configuración de E-Mail Client.

   Verifica que se haya generado tráfico y que esté preparado para la simulación.

   Ahora debería haber entradas de PDU en el panel de simulación para cada uno de los equipos cliente.

   Examina la multiplexación a medida que el tráfico cruza la red.

   Ahora utilizarás el botón Capturar/Reenviar del Panel de Simulación para observar los diferentes protocolos que viajan por la red.

   - Haz clic una vez en Capture/Forward. Todas las PDU se transfieren al switch.
   - Haz clic en Capturar/Reenviar seis veces y observe las PDU de los diferentes hosts mientras viajan por la red. Observa que solo una PDU puede cruzar un cable en cada dirección en un momento determinado.

2. Examinar la funcionalidad de los protocolos TCP y UDP

   **Examinar el tráfico HTTP cuando los clientes se comunican con el servidor.**

   - Haz clic en Reset Simulation (Restablecer simulación).
   - Filtra el tráfico que se muestra actualmente solo a las PDU HTTP y TCP. Para filtrar el tráfico que se muestra actualmente:
     1) Haz clic en Edit Filters y alterna el botón Show All/None.
     2) Selecciona HTTP y TCP. Haz clic en la "x" roja en la esquina superior derecha del cuadro Editar filtros para cerrarla. Los eventos visibles ahora deberían mostrar solo las PDU HTTP y TCP.
   - Abre el navegador en HTTP Client e ingresa `192.168.1.254` en el campo URL. Haz clic en Ir para conectarse al servidor a través de HTTP. Minimiza HTTP Client window.
   - Haz clic en Capturar/Reenviar hasta que aparezca una PDU para HTTP. Tenga en cuenta que el color del envolvente de la ventana de topología coincide con el código de color de la PDU HTTP del Panel de simulación.

   Pregunta:

   - ¿Por qué tardó tanto en aparecer la PDU HTTP?

   - Haz clic en el sobre de la PDU para mostrar los detalles de la PDU. Haz clic en Outbound PDU Details y desplázate hacia abajo hasta la segunda sección.

   Preguntas:

   - ¿Cómo se rotula la sección?
   - ¿Se consideran confiables estas comunicaciones?
   - Registra los valores de SRC PORT (PUERTO DE ORIGEN), DEST PORT (PUERTO DE DESTINO), SEQUENCE NUM (NÚMERO DE SECUENCIA) y ACK NUM (NÚMERO DE RECONOCIMIENTO).
   - Mira el valor en el campo Indicadores, que se encuentra junto al campo Ventana. Los valores a la derecha de la «b» representan los indicadores TCP que se establecen para esta etapa de la conversación de datos.

   Pregunta:

   - ¿Qué indicadores TCP se establecen en esta PDU?

   - Cierra la PDU y Haz clic en Capture/Forward hasta que una PDU con una marca de verificación regrese al HTTP Client.

   - Cierra el sobre de PDU y selecciona Inbound PDU Details. ¿En qué cambiaron los números de puerto y de secuencia? Haz clic en la PDU HTTP que HTTP Client ha preparado para enviar a MultiServer. Este es el comienzo de la comunicación HTTP. Haz clic en este segundo sobre de PDU y seleccione Outbound PDU Details (Detalles de PDU saliente).

   Pregunta:

   - ¿Qué información aparece ahora en la sección TCP? ¿En qué se diferencian los números de puerto y de secuencia con respecto a las dos PDU anteriores?

   Restablece la simulación.

   **Examinar el tráfico FTP cuando los clientes se comunican con el servidor.**

   a. Abre el símbolo del sistema en el escritorio del cliente FTP. Inicia una conexión FTP ingresando `ftp 192.168.1.254`.
   b. En el Panel de simulación, cambia Edit Filters para mostrar solo FTP y TCP.
   c. Haz clic en Capture/Forward. Haz clic en el segundo sobre PDU para abrirlo. Haz clic en la pestaña Outbound PDU Details y desplázate hacia abajo hasta la sección TCP.

   Pregunta:

   - ¿Se consideran confiables estas comunicaciones?

   d. Registra los valores de SRC PORT (PUERTO DE ORIGEN), DEST PORT (PUERTO DE DESTINO), SEQUENCE NUM (NÚMERO DE SECUENCIA) y ACK NUM (NÚMERO DE RECONOCIMIENTO).

   Pregunta:

   - ¿Cuál es el valor en el campo de bandera?

   Cierra la PDU y haz clic en Capture/Forward hasta que una PDU vuelva a FTP Client con una marca de verificación.
   Cierra el sobre de PDU y seleccione Inbound PDU Details.

   Pregunta:

   - ¿En qué cambiaron los números de puerto y de secuencia?

   Haz clic en la ficha de detalles de la PDU saliente.

   Pregunta:

   - ¿En qué se diferencian los números de puerto y secuencia de los resultados anteriores?

   Cierra la PDU y haz clic en Capture/Forward hasta que una segunda PDU vuelva a FTP Client. La PDU es de un color diferente.
   Abre la PDU y selecciona Inbound PDU Details. Desplázate hasta después de la sección TCP.

   Pregunta:

   - ¿Cuál es el mensaje del servidor?

   Restablece la simulación.

   **Examinar el tráfico DNS cuando los clientes se comunican con el servidor.**

   k. Repite los pasos de la Parte 1 para crear tráfico DNS.
   l. En el panel de simulación, modifica las opciones de Edit Filters para que solo se muestren DNS y UDP.
   m. Haz clic en el sobre de PDU para abrirlo.
   n. Mira los detalles del modelo OSI para la PDU saliente.

   Pregunta:

   - ¿Qué es el protocolo de capa 4?

   Preguntas:

   - ¿Se consideran confiables estas comunicaciones?
   - Abre la ficha Detalles de PDU saliente y busca la sección UDP de los formatos de PDU. Registra los valores de SRC PORT y DEST PORT.

   Pregunta:

   - ¿Por qué no hay números de secuencia y reconocimiento?

   Cierra la PDU y haz clic en Capture/Forward hasta que una PDU con una marca de verificación regrese al DNS Client.
   Cierra el sobre de PDU y seleccione Inbound PDU Details.

   Pregunta:

   - ¿En qué cambiaron los números de puerto y de secuencia?

   Preguntas:

   - ¿Cómo se llama la última sección de la PDU? ¿Cuál es la dirección IP para el nombre multiserver.pt.ptu?

   Restablece la simulación.

   **Examinar el tráfico de correo electrónico cuando los clientes se comunican con el servidor.**

   a. Repite los pasos de la Parte 1 para enviar un correo electrónico a user@multiserver.pt.ptu.
   b. En el panel de simulación, modifica las opciones de Edit Filters para que solo se muestren POP3, SMTP y TCP.
   c. Haz clic en el primer sobre de la PDU para abrirlo.
   d. Haz clic en la pestaña Outbound PDU Details y desplázate hacia abajo hasta la última sección.

   Preguntas:

   - ¿Qué protocolo de la capa de transporte utiliza el tráfico de correo electrónico? ¿Se consideran confiables estas comunicaciones?

   e. Registra los valores de SRC PORT (PUERTO DE ORIGEN), DEST PORT (PUERTO DE DESTINO), SEQUENCE NUM (NÚMERO DE SECUENCIA) y ACK NUM (NÚMERO DE RECONOCIMIENTO). ¿Cuál es el valor del campo de bandera?

   f. Cierra la PDU y haz clic en Capture/Forward hasta que una PDU regrese al E-Mail Client con una marca de verificación.
   g. Haz clic en el sobre TCP PDU y seleccione Inbound PDU Details.

   Pregunta:

   - ¿En qué cambiaron los números de puerto y de secuencia?

   Haz clic en la ficha de detalles de la PDU saliente.

   Pregunta:

   - ¿En qué se diferencian los números de puerto y de secuencia con respecto a los dos resultados anteriores?

   Hay una segunda PDU de un color diferente que E-Mail Client ha preparado para enviar a MultiServer. Este es el comienzo de la comunicación de correo electrónico. Haz clic en este segundo sobre de PDU y seleccione Outbound PDU Details.

   Preguntas:

   - ¿En qué se diferencian los números de puerto y de secuencia con respecto a las dos PDU anteriores?
   - ¿Qué protocolo de correo electrónico se relaciona con el puerto TCP 25? ¿Qué protocolo se relaciona con el puerto TCP 110?


