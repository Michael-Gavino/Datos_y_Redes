Actividad 2: Implementación de una conectividad básicaPara completar este laboratorio vamos a utilizar Cisco Packet Tracer.

Este ejercicio es grupal de a lo más 3 estudiantes, y debe terminarse hasta el sábado 30 demarzo a las 8:00 AM.Presenta un vídeo de a lo más 10 minutos mostrando los pasos de resolución de losejercicios.Tabla de asignación de direccionesDispositivo Interfaz Dirección IP Máscara de subredS1 VLAN 1 192.168.1.253 255.255.255.0S2 VLAN 1 192.168.1.254 255.255.255.0PC1 NIC 192.168.1.1 255.255.255.0PC2 NIC 192.168.1.2 255.255.255.0ObjetivosParte 1: Realizar una configuración básica en S1 y S2

Paso 2: Configurar las PCParte 3: Configurar la interfaz de administración de switchesAspectos básicosEn esta actividad, primero creará una configuración básica de conmutador. A continuación,implementará conectividad básica mediante la configuración de la asignación de direcciones IP enswitches y PC.

Cuando se complete la configuración de direccionamiento IP, usarás varios comandosshow para verificar la configuración y usará el comando ping para verificar la conectividad básicaentre dispositivos.Instrucciones1. 

Realiza una configuración básica en el S1 y el S2Complete los siguientes pasos en el S1 y el S2.Configura un nombre de host en el S1.a. Haz clic en S1 y luego en la ficha CLI.b. 

Introduce el comando correcto para configurar el nombre de host S1.Configura la consola y las contraseñas cifradas de modo EXEC privilegiado.a. Usa checha como la contraseña de la consola.

Departamento Académico de IngenieríaC8280 -Comunicación de Datos y RedesComunicación de Datos y Redesb. Usa jeka para la contraseña del modo EXEC privilegiado.

Verifica la configuración de contraseñas para el S1.Pregunta:¿Cómo puedes verificar que ambas contraseñas se hayan configurado correctamente?Configura un aviso de MOTD.Utiliza un texto de aviso adecuado para advertir contra el acceso no autorizado. El siguiente texto esun ejemplo:Acceso autorizado únicamente. 

Los infractores se procesarán en la medida en que lopermita la ley.Guarda el archivo de configuración en la NVRAM.Pregunta:¿Qué comando emite para realizar este paso?2. Repita los pasos 1 a 5 para el S2.Configurar las PCConfigura la PC1 y la PC2 con direcciones IP.Configura ambas PC con direcciones IP.a. Haz clic en PC1 y luego en la ficha Escritorio.b.

Haz clic en Configuración de IP. En la tabla de direccionamiento anterior, puede ver que ladirección IP para la PC1 es 192.168.1.1 y la máscara de subred es 255.255.255.0.Introduzca esta información para la PC1 en la ventana Configuración de IP.c. Repite los pasos 1a y 1b para la PC2.

Prueba la conectividad a los switches.d. Haz clic en PC1. Cierre la ventana Configuración de IP si todavía está abierta. En la fichaEscritorio, haga clic en Símbolo del sistema.e. 

Escribe el comando ping y la dirección IP para S1 y presione Enter.Packet Tracer PC Línea de comandos 1.0PC> ping 192.168.1.253Pregunta:¿Tuviste éxito? 

Explica.3. Configura la interfaz de administración de switchesConfigura el S1 y el S2 con una dirección IP.Configura el S1 con una dirección IP.Los switches pueden usarse como dispositivos plug-and-play. Esto significa que no necesitanconfigurarse para que funcionen. 

Los switches reenvían información desde un puerto hacia otrosobre la base de direcciones de control de acceso al medio (MAC).Pregunta:Si este es el caso, ¿por qué lo configuraremos con una dirección IP?Usa los siguientes comandos para configurar el S1 con una dirección IP.S1# configure terminalEnter configuration commands, one per line. Finalice con CNTL/Z.
(config)# interface vlan 1S1(config-if)# ip address 192.168.1.253 255.255.255.0S1(config-if)# no shutdown%LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed stateto upS1(config-if)#S1(config-if)# exitS1#

Pregunta:¿Por qué debe introducir el comando no shutdown?

Configura el S2 con una dirección IP.Usa la información de la tabla de direccionamiento para configurar el S2 con una dirección IP.Verifica la configuración de direcciones IP en el S1 y el S2.

Usa el comando show ip interface brief para ver la dirección IP y el estado de todos los puertos ylas interfaces del switch. También puede utilizar el comando show running-config.Guarda la configuración para el S1 y el S2 en la NVRAM.Pregunta:¿Qué comando se utiliza para guardar en la NVRAM el archivo de configuración que se encuentra enla RAM?Verifica la conectividad de la red.Puedes verificar la conectividad de la red mediante el comando ping. 

Es muy importante que hayaconectividad en toda la red. Se deben tomar medidas correctivas si se produce una falla. Desde laPC1 y la PC2, haga ping al S1 y S2.a.

Haga clic en PC1 y luego en la ficha Escritorio.b. Haga clic en Símbolo del sistema.c. Haga ping a la dirección IP de la PC2.d. 

Haga ping a la dirección IP del S1.e. Haga ping a la dirección IP del S2.Nota: También usa el ping en la CLI del switch y en la PC2.Todos los ping deben tener éxito. 

Si el resultado del primer ping es 80%, inténtelo otra vez. 

Ahoradebería ser 100%. Más adelante, aprenderá por qué es posible que un ping falle la primera vez. Si nopuede hacer ping a ninguno de los dispositivos, vuelva a revisar la configuración para detectarerrores
