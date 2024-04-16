## Actividad 3: Identificación de direcciones MAC y direccionesIPObjetivos

Parte 1: Recopilar información de PDU para la comunicación de red localParte 

2: Recopilar información de PDU para la comunicación de red remotaConcepto importanteEn el contexto de redes, PDU significa "Unidad de Datos del Protocolo" (Protocol Data Unit, porsus siglas en inglés). Es un término general que se refiere a la forma en que se encapsulan losdatos en las diferentes capas del Modelo OSI (Open Systems Interconnection) o del ModeloTCP/IP para la transmisión a través de la red. 

Cada capa del modelo OSI utiliza una PDUespecífica para realizar su función:• Capa de Aplicación, Presentación y Sesión: Utilizan los datos de aplicación.• Capa de Transporte: Utiliza segmentos (en TCP) o datagramas (en UDP) como su PDU.•

Capa de Red: Utiliza paquetes o datagramas como su PDU.• 

Capa de Enlace de Datos: Utiliza tramas como su PDU.• Capa Física: Utiliza bits como su PDU.Aspectos básicosEsta actividad está optimizada para la visualización de PDU1. Los dispositivos ya estánconfigurados. 

Reunirá información de PDU en el modo de simulación y responderá una serie depreguntas sobre los datos que obtenga.InstruccionesRecopila información del PDU para la comunicación de red local1. Recopila información de la PDU a medida que un paquete viaja de 172.16.31.5 a172.16.31.2.a. 

Haz clic en 172.16.31.5 y abra el Command Prompt.b. Introduce el comando ping 172.16.31.2.c. Cambia al modo de simulación y repita el comando ping 172.16.31.2. 

Aparece una PDUjunto a 172.16.31.5.d. Haz clic en la PDU y observa la siguiente información de las pestañas Modelo OSI l y Capade PDU saliente:o Destination MAC Address: 000C:85CC:1DA71 https://es.wikipedia.org/wiki/Unidad_de_datos_de_protocolo
o Source MAC Address: 00D0:D311:C788o Source IP Address:172.16.31.5o Destination IP Address: 172.16.31.2o At Device: 172.16.31.5e. Haz clic en Capture / Forward (la flecha derecha seguida de una barra vertical) paramover la PDU al siguiente dispositivo.

Reúna la misma información del paso 1d. Repite esteproceso hasta que la PDU llegue al destino.

Registra la información que reunió de la PDU enuna hoja de cálculo con un formato como el de la tabla que se muestra a continuación:Formato de hoja de cálculo de ejemploEn dispositivo MAC de destino MAC de origen IPv4 de origen IPv4 de destino172.16.31.5 000C:85CC:1DA7 00D0:D311:C788 172.16.31.5 172.16.31.2Switch1 000C:85CC:1DA7 00D0:D311:C788 No corresponde No correspondeConcentrador No corresponde No corresponde No corresponde No corresponde172.16.31.2 00D0:D311:C788 000C:85CC:1DA7 172.16.31.2 172.16.31.52. 

Reunir información adicional de la PDU de otros ping.Repite el proceso del paso 1 y reúna información para las siguientes pruebas:- Ping de 172.16.31.2 a 172.16.31.3- Ping de 172.16.31.4 a 172.16.31.5Vuelva al modo Realtime.2. Recopila información del PDU para la comunicación de red remotaPara comunicarse con redes remotas, es necesario un dispositivo de puerta de enlace. 

Estudia elproceso que tiene lugar para comunicarse con los dispositivos de la red remota. Presta muchaatención a las direcciones MAC utilizadas.Recopila información de la PDU a medida que un paquete viaja de 172.16.31.5 a10.10.10.2.a. Haz click en 172.16.31.5 y abra el Command Prompt.b. 

Introduce el comando ping 10.10.10.2.c. Cambia al modo de simulación y repita el comando ping 10.10.10.2. 

Aparece una PDU juntoa 172.16.31.5.d. Haz clic en la PDU y observe la siguiente información en la ficha Outbound PDU Layer(Capa de PDU saliente):Destination MAC Address: 00D0:BA8E:741ASource MAC Address: 00D0:D311:C788Source IP Address: 172.16.31.5Destination IP Address: 10.10.10.2At Device: 172.16.31.5Pregunta:¿Qué dispositivo tiene el MAC de destino que se muestra?Escriba sus respuestas aquí.

e. Haz clic en Capture / Forward (la flecha derecha seguida de una barra vertical) paramover la PDU al siguiente dispositivo. Reúne la misma información del paso 1d. 

Repite esteproceso hasta que la PDU llegue al destino. Registra la información de la PDU que recopilódel ping 172.16.31.5 a 10.10.10.2 en una hoja de cálculo utilizando un formato como la tablade muestra que se muestra a continuación:En dispositivo MAC de destino MAC de origen IPv4 de origen IPv4 de destino172.16.31.5 00D0:BA8E:741A 00D0:D311:C788 172.16.31.5 10.10.10.2Switch1 00D0:BA8E:741A 00D0:D311:C788 No corresponde No correspondeRouter 0060:2 F 84:4 AB6 00D0:588C:2401 172.16.31.5 10.10.10.2Switch0 0060:2F84:4AB6 00D0:588C:2401 No corresponde No correspondePunto de acceso No corresponde No corresponde No corresponde No corresponde10.10.10.2 00D0:588C:2401 0060:2 F 84:4 AB6 10.10.10.2 172.16.31.5PreguntasResponde las siguientes preguntas relacionadas con los datos capturados:1. ¿Se utilizaron diferentes tipos de cables / medios para conectar dispositivos?Escriba sus respuestas aquí.2.

¿Los cables cambiaron el manejo de la PDU de alguna manera?
Escriba sus respuestas aquí.

3. ¿El hub perdió parte de la información que recibió?Escriba sus respuestas aquí.
4.  ¿Qué hace el hub con las direcciones MAC y las direcciones IP?Escriba sus respuestas aquí.
5.  ¿El punto de acceso inalámbrico hizo algo con la información que se le entregó?Escriba sus respuestas aquí.
6.  ¿Se perdió alguna dirección MAC o IP durante la transferencia inalámbrica?Escriba sus respuestas aquí.
7. ¿Cuál fue la capa OSI más alta que utilizaron el hub y el punto de acceso?Escriba sus respuestas aquí.
8. ¿El hub o el punto de acceso reprodujeron en algún momento una PDU rechazada con una “X”de color rojo?Escriba sus respuestas aquí.9
9. Al examinar la ficha PDU Details (Detalles de PDU), ¿qué dirección MAC aparecía primero, lade origen o la de destino?Escriba sus respuestas aquí.
10. ¿Por qué las direcciones MAC aparecen en este orden?Escriba sus respuestas aquí.11. ¿Había un patrón para el direccionamiento MAC en la simulación?Escriba sus respuestas aquí.

