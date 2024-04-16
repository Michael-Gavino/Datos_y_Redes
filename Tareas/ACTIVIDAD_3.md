Actividad 3: Identificación de direcciones MAC y direcciones IP 
 
Objetivos 
Parte 1: Recopilar información de PDU para la comunicación de red local 
Parte 2: Recopilar información de PDU para la comunicación de red remota 
 
Concepto importante 
En el contexto de redes, PDU significa "Unidad de Datos del Protocolo" (Protocol Data Unit, por sus siglas en inglés). Es un término general que se refiere a la forma en que se encapsulan los datos en las diferentes capas del Modelo OSI (Open Systems Interconnection) o del Modelo TCP/IP para la transmisión a través de la red. Cada capa del modelo OSI utiliza una PDU específica para realizar su función: 
•	Capa de Aplicación, Presentación y Sesión: Utilizan los datos de aplicación. 
•	Capa de Transporte: Utiliza segmentos (en TCP) o datagramas (en UDP) como su PDU. 
•	Capa de Red: Utiliza paquetes o datagramas como su PDU. 
•	Capa de Enlace de Datos: Utiliza tramas como su PDU. 
•	Capa Física: Utiliza bits como su PDU. 
Aspectos básicos 
Esta actividad está optimizada para la visualización de PDU . Los dispositivos ya están configurados. Reunirá información de PDU en el modo de simulación y responderá una serie de preguntas sobre los datos que obtenga. 
Instrucciones Recopila información del PDU para la comunicación de red local 
 
1.	Recopila información de la PDU a medida que un paquete viaja de 172.16.31.5 a 172.16.31.2. 
a.	Haz clic en 172.16.31.5 y abra el Command Prompt. 
b.	Introduce el comando ping 172.16.31.2. 
 
c.	Cambia al modo de simulación y repita el comando ping 172.16.31.2. Aparece una PDU junto a 172.16.31.5. 
 
d.	Haz clic en la PDU y observa la siguiente información de las pestañas Modelo OSI l y Capa de PDU saliente:  o Destination MAC Address: 000C:85CC:1DA7 
  
o Source MAC Address: 00D0:D311:C788 o Source IP Address:172.16.31.5 o Destination IP Address: 172.16.31.2 o At Device: 172.16.31.5 
 
e.	Haz clic en Capture / Forward (la flecha derecha seguida de una barra vertical) para mover la PDU al siguiente dispositivo. Reúna la misma información del paso 1d. Repite este proceso hasta que la PDU llegue al destino. Registra la información que reunió de la PDU en una hoja de cálculo con un formato como el de la tabla que se muestra a continuación: Formato de hoja de cálculo de ejemplo 
En dispositivo 	MAC de destino 	MAC de origen 	IPv4 de origen 	IPv4 de destino 
172.16.31.5 	000C:85CC:1DA7 	00D0:D311:C788 	172.16.31.5 	172.16.31.2 
Switch1 	000C:85CC:1DA7 	00D0:D311:C788 	No corresponde 	No corresponde 
Concentrador 	No corresponde 	No corresponde 	No corresponde 	No corresponde 
172.16.31.2 	00D0:D311:C788 	000C:85CC:1DA7 	172.16.31.2 	172.16.31.5 
2.	Reunir información adicional de la PDU de otros ping. 
Repite el proceso del paso 1 y reúna información para las siguientes pruebas: 
-	Ping de 172.16.31.2 a 172.16.31.3 

 




En dispositivo 	MAC de destino 	MAC de origen 	IPv4 de origen 	IPv4 de destino 
172.16.31.2	0060:7036:2849	000C:85CC:1DA7	172.16.31.2 	172.16.31.3 
Concentrador 	No corresponde 	No corresponde 	No corresponde 	No corresponde 
172.16.31.3	000C:85CC:1DA7	0060:7036:2849	172.16.31.3 	172.16.31.2

. Ping de 172.16.31.4 a 172.16.31.5 Vuelva al modo Realtime. 
 
En dispositivo 	MAC de destino 	MAC de origen 	IPv4 de origen 	IPv4 de destino 
172.16.31.4 	00D0.D311.C788	000C.CF0B. BC80	172.16.31.4 	172.16.31.5
Switch1 	000C.CF0B. BC80	00D0.D311.C788	No corresponde 	No corresponde 
172.16.31.5 	000C.CF0B. BC80	00D0.D311.C788	172.16.31.5 	172.16.31.4





2.	Recopila información del PDU para la comunicación de red remota 
Para comunicarse con redes remotas, es necesario un dispositivo de puerta de enlace. Estudia el proceso que tiene lugar para comunicarse con los dispositivos de la red remota. Presta mucha atención a las direcciones MAC utilizadas. 
 
Recopila información de la PDU a medida que un paquete viaja de 172.16.31.5 a 10.10.10.2. 
 
a.	Haz click en 172.16.31.5 y abra el Command Prompt.  
b.	Introduce el comando ping 10.10.10.2. 



 

c.	Cambia al modo de simulación y repita el comando ping 10.10.10.2. Aparece una PDU junto a 172.16.31.5. 

 



d.	Haz clic en la PDU y observe la siguiente información en la ficha Outbound PDU Layer (Capa de PDU saliente): 
Destination MAC Address: 00D0:BA8E:741A 
Source MAC Address: 00D0:D311:C788 
Source IP Address: 172.16.31.5 
Destination IP Address: 10.10.10.2 
At Device: 172.16.31.5 

 

Pregunta: 
¿Qué dispositivo tiene el MAC de destino que se muestra? 
El laptop 10.10.10.2. 
e.	Haz clic en Capture / Forward (la flecha derecha seguida de una barra vertical) para mover la PDU al siguiente dispositivo. Reúne la misma información del paso 1d. Repite este proceso hasta que la PDU llegue al destino. Registra la información de la PDU que recopiló del ping 172.16.31.5 a 10.10.10.2 en una hoja de cálculo utilizando un formato como la tabla de muestra que se muestra a continuación: 
En dispositivo 	MAC de destino 	MAC de origen 	IPv4 de origen 	IPv4 de destino 
172.16.31.5 	00D0:BA8E:741A 	00D0:D311:C788 	172.16.31.5 	10.10.10.2 
Switch1 	00D0:BA8E:741A 	00D0:D311:C788 	No corresponde 	No corresponde 
Router 	0060:2 F 84:4 AB6 	00D0:588C:2401 	172.16.31.5 	10.10.10.2 
Switch0 	0060:2F84:4AB6 	00D0:588C:2401 	No corresponde 	No corresponde 
Punto de acceso 	No corresponde 	No corresponde 	No corresponde 	No corresponde 
10.10.10.2 	00D0:588C:2401 	0060:2 F 84:4 AB6 	10.10.10.2 	172.16.31.5 
Preguntas 
Responde las siguientes preguntas relacionadas con los datos capturados: 
1.	¿Se utilizaron diferentes tipos de cables / medios para conectar dispositivos? 
Si, tenemos tres tipos, medio inalámbrico, cobre y fibra 
Escriba sus respuestas aquí. 
2.	¿Los cables cambiaron el manejo de la PDU de alguna manera? 
No, ya que los cables solo trabajan en capa 1
Escriba sus respuestas aquí. 
3.	¿El hub perdió parte de la información que recibió? 
No
Escriba sus respuestas aquí. 
4.	¿Qué hace el hub con las direcciones MAC y las direcciones IP? 
No hace nada, solo reenvía hacia todos sus puertos
Escriba sus respuestas aquí. 
5.	¿El punto de acceso inalámbrico hizo algo con la información que se le entregó? 
Si, vuelve a empaquetar la trama para que viaje por ese medio 
Escriba sus respuestas aquí. 
6.	¿Se perdió alguna dirección MAC o IP durante la transferencia inalámbrica? 
No 
Escriba sus respuestas aquí. 
7.	¿Cuál fue la capa OSI más alta que utilizaron el hub y el punto de acceso? 
Solamente trabaja en capa 1
Escriba sus respuestas aquí. 
8.	¿El hub o el punto de acceso reprodujeron en algún momento una PDU rechazada con una “X” de color rojo? 
Si, ya que al reenviar a todos los puertos solo es uno el destino y los demás los rechaza, esto ocurrió con el pc 172.56.31.4
Escriba sus respuestas aquí. 
9.	Al examinar la ficha PDU Details (Detalles de PDU), ¿qué dirección MAC aparecía primero, la de origen o la de destino? 
La de destino
Escriba sus respuestas aquí. 
10.	¿Por qué las direcciones MAC aparecen en este orden? 
Ya que, si se conoce la dirección, va a llevar el mensaje más rápido
Escriba sus respuestas aquí. 
11.	¿Había un patrón para el direccionamiento MAC en la simulación? 
no
Escriba sus respuestas aquí. 
12.	¿Los switches reprodujeron en algún momento una PDU rechazada con una “X” de color rojo? 
No, porque solo renvían la traba al destino requerido 
13.	Cada vez que se enviaba la PDU entre las redes 10 y 172, había un punto donde las direcciones MAC cambiaban repentinamente.  ¿Dónde ocurrió eso? 
Si, ocurre en el router

14.	¿Qué dispositivo usa direcciones MAC que comienzan con 00D0: BA? 
Es la del router

15.	¿A qué dispositivos pertenecían las otras direcciones MAC? 
Pertenecían a direcciones emisores y receptores
Escriba sus respuestas aquí. 
16.	¿Las direcciones IPv4 de envío y recepción cambiaron los campos en alguna de las PDU? 
No

17.	Cuando sigue la respuesta a un ping, a veces llamado pong, ¿ve el cambio de envío y recepción de direcciones IPv4? 
Si

18.	¿Cuál es el patrón para el direccionamiento IPv4 utilizado en esta simulación? 
que cada dirección en el router no se pueda repetir en la misma dirección 

19.	¿Por qué es necesario asignar diferentes redes IP a los diferentes puertos de un router? 
Para poder interconectar redes

20.	Si esta simulación se configura con IPv6 en lugar de IPv4, ¿cuál sería la diferencia? 
Lo único que cambiaría sería el formato

