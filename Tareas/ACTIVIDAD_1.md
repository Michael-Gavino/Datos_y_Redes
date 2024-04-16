
## Actividad 1:
Creación de una red simplePara completar este laboratorio vamos a utilizar Cisco Packet TracerTopología Tabla de direccionamiento Dispositivo Interface Dirección IP Máscara de subredPC-A
NIC 192.168.1.10 255.255.255.0PC-B NIC 192.168.1.11 255.255.255.

# Objetivos
Parte 1: Configuración de la topología de la red- Identificar los dispositivos de red y construir una red simple con Packet Tracer.

- Realizar el cableado de una topología de red.Parte 2: Configuración de hosts en las PC- Introducir la información de dirección IP estática en la interfaz LAN de los hosts.

- Verificar que las PC puedan comunicarse por medio de la utilidad ping.Información básica/situaciónLas redes están formadas por tres componentes principales: hosts, switches y routers. 

En estelaboratorio, armará una red simple con dos hosts y un switch. En esta práctica de laboratorio, aplicarála asignación de direcciones IP a las PC para habilitar la comunicación entre estos dos dispositivos.

Use la utilidad ping para verificar la conectividad.Nota: Los switches que se usan son Cisco Catalyst 2960 con Cisco IOS Release 15.0(2) (imagenlanbasek9).Se pueden utilizar otros switches y otras versiones de Cisco IOS.Recursos necesarios

- 1 switch (Cisco 2960 con Cisco IOS versión 15.0(2), imagen lanbasek9 o similar)- 2 PC (Windows 10)- cables Ethernet como se muestra en la topología.Paso 1: Construye la red simple configurando cada uno de los dispositivos dados.

a. En la interfaz de Packet Tracer selecciona los dispositivos dados: Switch 2960.b. Click en el dispositivo y en la pestaña Config, Display Name, Hostname Cambia el nombre aS1.c. 

Realiza el mismo procedimiento para los otros dispositivos. 

Llamalos PC-A, PC-Brespectivamented. Selecciona el ícono Rayo de conexiones y escoge Copper Straight-Through.e.

Conecte un extremo de un cable Ethernet al puerto de NIC en PC-A. Conecte el otro extremodel cable a F0/6 en S1. 

Después de conectar la PC al switch, la luz de F0/6 debería tornarseámbar y luego verde, lo que indica que la PC-A se conectó correctamente.f. 

Conecte un extremo de un cable Ethernet al puerto de NIC en PC-B. Conecte el otro extremodel cable a F0/1 en S1. 

Después de conectar la PC al switch, la luz de F0/1 debería tornarseámbar y luego verde, lo que indica que la PC-B se conectó correctamente.Paso 2: Verifique la configuración y la conectividad de la PC.

Use la línea de comandos para verificar la configuración de la PC y la conectividad.a.

Desde PC-A,
haga clic y Desktop seleccione Command Prompt.b.

En la ventana de comandos de packet tracer, puedes introducir comandos directamente en laPC y ver los resultados de esos comandos. 

Verifique la configuración de la PC mediante elcomando ipconfig /all. 

Este comando muestra información sobre el nombre del host de laPC y la dirección IPv4.c. 

Escriba ping 192.168.1.11 y presione Intro.¿Fueron correctos los resultados del ping? ______________________d.

Repite los pasos anteriores para PC-B¿Fueron correctos los resultados del ping? ______________________Nota: Si no obtuvo una respuesta de PC-B, intente hacer ping a PC-B nuevamente.

Si siguesin obtener respuesta de PC-B, intente enviar un comando ping a PC-A desde PC-B

