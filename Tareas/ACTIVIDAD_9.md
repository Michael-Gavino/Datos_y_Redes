# Actividad 9: Uso de Wireshark para ver el tráfico de la topología de red

## Objetivos

### Parte 1: Capturar y analizar datos ICMP locales en Wireshark

### Parte 2: Capturar y analizar datos ICMP remotos en Wireshark

## Información básica/situación

Wireshark es un analizador de protocolos de software o una aplicación “husmeador de paquetes” que se utiliza para la solución de problemas de red, análisis, desarrollo de protocolo y software y educación. Mientras el flujo de datos va y viene en la red, el husmeador “captura” cada unidad de datos del protocolo (PDU) y puede decodificar y analizar su contenido de acuerdo a la RFC correcta u otras especificaciones. Es una herramienta útil para cualquiera que trabaje con redes y se puede utilizar en la mayoría de las prácticas de laboratorio en los cursos de CCNA para el análisis de datos y la solución de problemas. En esta práctica de laboratorio, usará Wireshark para capturar direcciones IP del paquete de datos ICMP y direcciones MAC de la trama de Ethernet.

## Recursos necesarios

- 1 PC (Windows con acceso a internet)
- Se utilizarán PC adicionales en una red de área local (LAN) para responder a las solicitudes de ping.

## Instrucciones

### 1. Captura y análisis de datos ICMP locales en Wireshark

En la parte 1 de esta práctica de laboratorio, harás ping a otra PC en la LAN y capturará solicitudes y respuestas ICMP en Wireshark. También verá dentro de las tramas capturadas para obtener información específica. Este análisis debe ayudar a aclarar de qué manera se utilizan los encabezados de paquetes para transmitir datos al destino.

#### Recupera las direcciones de interfaz de la PC

Para esta práctica de laboratorio, deberás recuperar la dirección IP de la PC y la dirección física de la tarjeta de interfaz de red (NIC), que también se conoce como “dirección MAC”.

- Abre una ventana de intérprete de comandos de Windows.
  - En una ventana del símbolo del sistema, ingresa `ipconfig /all` para obtener la dirección IP de la interfaz de su PC, su descripción y su dirección MAC (física).
- Solicita a un miembro o a los miembros del equipo la dirección IP de su PC y proporcióneles la suya. En esta instancia, no proporcione su dirección MAC.
- Cierra un símbolo del sistema de Windows.

#### Inicia Wireshark y comienza a capturar datos

- Navega a Wireshark. Haz doble clic en la interfaz deseada para iniciar la captura de paquetes. Asegúrate de que la interfaz deseada tenga tráfico.
- La información comienza a desplazar hacia abajo la sección superior de Wireshark. Las líneas de datos aparecen en diferentes colores según el protocolo.
- Es posible desplazarse muy rápidamente por esta información según la comunicación que tiene lugar entre la PC y la LAN. Se puede aplicar un filtro para facilitar la vista y el trabajo con los datos que captura Wireshark.

- Para esta práctica de laboratorio, solo nos interesa mostrar las PDU de ICMP (ping). Escribe `icmp` en el cuadro Filter en la parte superior de Wireshark y presiona Enter, o haz clic en el botón Apply (signo de flecha) para ver sólo las PDU ICMP (ping).

- Este filtro hace que desaparezcan todos los datos de la ventana superior, pero se sigue capturando el tráfico en la interfaz. Navega a la ventana del símbolo del sistema y haz ping a la dirección IP que recibiste de un miembro de tu equipo.
Comenzarás a ver que aparecen datos en la ventana superior de Wireshark nuevamente.

- Detén la captura de datos haciendo clic en el ícono Stop Capture (Detener captura).

#### Examina los datos capturados

Examinamos los datos que se generaron mediante las solicitudes de ping de la PC del miembro del equipo. Los datos de Wireshark se muestran en tres secciones:

1. La sección superior muestra la lista de tramas de PDU capturadas con un resumen de la información de paquetes IP enumerada.
2. La sección media indica información de la PDU para la trama seleccionada en la parte superior de la pantalla y separa una trama de PDU capturada por las capas de protocolo.
3. La sección inferior muestra los datos sin procesar de cada capa. Los datos sin procesar se muestran en formatos hexadecimal y decimal.

- Haz clic en las primeras tramas de PDU de la solicitud de ICMP en la sección superior de Wireshark. Observa que la columna Source contiene la dirección IP de tu PC y la columna Destination contiene la dirección IP de la PC del compañero de equipo a la que hiciste ping.
- Con esta trama de PDU aún seleccionada en la sección superior, navega hasta la sección media. Haz clic en el signo más que está a la izquierda de la fila de Ethernet II para ver las direcciones MAC de origen y destino.

##### Preguntas:

1. ¿La dirección MAC de origen coincide con la interfaz de tu PC?
 - Escriba sus respuestas aquí.

2. ¿La dirección MAC de destino en Wireshark coincide con la dirección MAC del compañero de equipo?
 - Escriba sus respuestas aquí.

3. ¿De qué manera tu PC obtiene la dirección MAC de la PC a la que hiciste ping?
 - Escriba sus respuestas aquí.

#### 2. Captura y analiza datos ICMP remotos en Wireshark

En la parte 2, harás ping a los hosts remotos (hosts que no están en la LAN) y examinarás los datos generados a partir de esos pings. Luego, determinarás las diferencias entre estos datos y los datos examinados en la parte 1.

#### Comienza a capturar datos en la interfaz

- Vuelve a iniciar la captura de datos.
- Se abre una ventana que le solicita guardar los datos capturados anteriormente antes de comenzar otra captura. No es necesario guardar esos datos. Haz clic en Continue without Saving.
- Con la captura activa, haz ping a las siguientes tres URL de sitios web desde un símbolo del sistema de Windows:

- www.yahoo.com
- www.cisco.com
- www.google.com

##### Nota:

Cuando hagas ping a las URL enumeradas, observa que el Servidor de nombres de dominio (DNS) traduce la URL a una dirección IP. Observa la dirección IP recibida para cada URL.

- Puedes detener la captura de datos haciendo clic en el ícono Stop Capture.

#### Inspecciona y analiza los datos de los hosts remotos

Revise los datos capturados en Wireshark y examine las direcciones IP y MAC de las tres ubicaciones a las que hiciste ping. Indique las direcciones IP y MAC de destino para las tres ubicaciones en el espacio proporcionado.

##### Preguntas:

- Dirección IP de www.yahoo.com:
- Escriba sus respuestas aquí.

- Dirección MAC para www.yahoo.com:
- Escriba sus respuestas aquí.

- Dirección IP para www.cisco.com:
- Escriba sus respuestas aquí.

- Dirección MAC para www.cisco.com:
- Escriba sus respuestas aquí.

- Dirección IP de www.google.com:
- Escriba sus respuestas aquí.

- Dirección MAC para www.google.com:
¿Qué es importante sobre esta información?
- Escriba sus respuestas aquí.

- ¿En qué se diferencia esta información de la información de ping local que recibiste en la parte Pregunta
- Escriba sus respuestas aquí.

- ¿Por qué Wireshark muestra la dirección MAC vigente de los hosts locales, pero no la dirección MAC vigente de los hosts remotos?
- Escriba sus respuestas aquí.

## Apéndice A: Permitir el tráfico ICMP a través de un firewall

Si los miembros del equipo no pueden hacer ping a su PC, es posible que el firewall esté bloqueando esas solicitudes. En este apéndice, se describe cómo crear una regla en el firewall para permitir las solicitudes de ping. También se describe cómo deshabilitar la nueva regla ICMP después de haber completado la práctica de laboratorio.

### Crear una nueva regla de entrada que permita el tráfico ICMP a través del firewall

- Navega hasta el Control Panel y haz clic en la opción System and Security en la categoría view.
- En la ventana System and Security, haz clic en Windows Defender Firewall o Windows Firewall.
- En el panel izquierdo de la ventana Windows Defender Firewall o Windows Firewall haz clic en Advanced settings.
- En la ventana de Advanced Security haz clic en la opción Inbound Rules en la barra lateral izquierda y luego haz clic en New Rule… en la barra lateral derecha.
- Se inicia el asistente New Inbound Rule. En la pantalla Rule Type haz clic en el boton Custom y haz clic en Next.
- En el panel izquierdo, haz clic en la opción Protocol and Ports y, en el menú desplegable Protocol Type, selecciona ICMPv4; luego, haz clic en Next.
- Comprueba que se ha seleccionado Cualquier dirección IP para las direcciones IP locales y remotas. Haz clic en Next para continuar.
- Selecciona Allow the connection. Haz clic en Next para continuar.
- De forma predeterminada, esta regla se aplica a todos los perfiles. Haz clic en Next para continuar.
- Nombre la regla con Allow ICMP Requests. Haz clic en Finish para continuar. Esta nueva regla debe permitir que los miembros del equipo reciban respuestas de ping de su PC.

### Deshabilitar o eliminar la nueva regla ICMP.

Una vez completada la práctica de laboratorio, es posible que desees deshabilitar o incluso eliminar la nueva regla que creaste en el paso 1. La opción Disable Rule te permite volver a habilitar la regla en una fecha posterior. Al eliminar la regla, esta se elimina permanentemente de la lista de reglas de entrada.

- En la ventana de Advanced Security, haz clic en Inbound Rules en el panel izquierdo y luego ubica la regla que creaste anteriormente.
- Haz clic con el botón derecho en la regla ICMP y selecciona Disable Rule si así lo deseas. También puede seleccionar Delete si deseas eliminarla permanentemente. Si eliges esta opción, deberás volver a crear la regla para permitir las respuestas de ICMP.

