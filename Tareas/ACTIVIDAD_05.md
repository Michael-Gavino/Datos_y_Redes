# Actividad 5: Identificación de direcciones MAC y direcciones IP

## Objetivos

- Parte 1: Recopilar información de PDU para la comunicación de red local
- Parte 2: Recopilar información de PDU para la comunicación de red remota

## Aspectos básicos

Esta actividad está optimizada para la visualización de PDU[^1]. Los dispositivos ya están configurados. Reunirá información de PDU en el modo de simulación y responderá una serie de preguntas sobre los datos que obtenga.

## Instrucciones

### Recopila información del PDU para la comunicación de red local

#### 1. Recopila información de la PDU a medida que un paquete viaja de 172.16.31.5 a 172.16.31.2.
   a. Haz clic en **172.16.31.5** y abra el **Command Prompt**.
   
   b. Introduce el comando `ping 172.16.31.2`.
   
   c. Cambia al modo de simulación y repite el comando `ping 172.16.31.2`. Aparece una PDU junto a 172.16.31.5.
   
   d. Haz clic en la PDU y observa la siguiente información de las pestañas Modelo OSI y Capa de PDU saliente.
   - Destination MAC Address: 000C:85CC:1DA7
- Source MAC Address: 00D0:D311:C788
- Source IP Address: 172.16.31.5
- Destination IP Address: 172.16.31.2
- At Device: 172.16.31.5

e. Haz clic en `Capture / Forward` (la flecha derecha seguida de una barra vertical) para mover la PDU al siguiente dispositivo. Reúna la misma información del paso 1d. Repite este proceso hasta que la PDU llegue al destino. Registra la información que reunió de la PDU en una hoja de cálculo con un formato como el de la tabla que se muestra a continuación:

| En dispositivo  | MAC de destino | MAC de origen | IPv4 de origen | IPv4 de destino |
|-----------------|----------------|---------------|----------------|-----------------|
| 172.16.31.5     | 000C:85CC:1DA7| 00D0:D311:C788| 172.16.31.5    | 172.16.31.2     |
| Switch1         | 000C:85CC:1DA7| 00D0:D311:C788| No corresponde| No corresponde  |
| Concentrador    | No corresponde| No corresponde| No corresponde| No corresponde  |
| 172.16.31.2     | 00D0:D311:C788| 000C:85CC:1DA7| 172.16.31.2    | 172.16.31.5     |

#### 2. Reunir información adicional de la PDU de otros pings.
   - Repite el proceso del paso 1 y reúna información para las siguientes pruebas:
     - Ping de 172.16.31.2 a 172.16.31.3
     - Ping de 172.16.31.4 a 172.16.31.5
   - Vuelve al modo Realtime.

### Recopila información del PDU para la comunicación de red remota

Para comunicarse con redes remotas, es necesario un dispositivo de puerta de enlace. Estudia el proceso que tiene lugar para comunicarse con los dispositivos de la red remota. Presta mucha atención a las direcciones MAC utilizadas.

#### . Recopila información de la PDU a medida que un paquete viaja de 172.16.31.5 a 10.10.10.2.
   - Haz clic en 172.16.31.5 y abra el Command Prompt.
   - Introduce el comando `ping 10.10.10.2`.
   - Cambia al modo de simulación y repite el comando `ping 10.10.10.2`. Aparece una PDU junto a 172.16.31.5.
   - Haz clic en la PDU y observa la siguiente información en la ficha `Outbound PDU Layer` (Capa de PDU saliente):

     - Destination MAC Address: 00D0:BA8E:741A
     - Source MAC Address: 00D0:D311:C788
     - Source IP Address: 172.16.31.5
     - Destination IP Address: 10.10.10.2
     - At Device: 172.16.31.5

**Pregunta:** ¿Qué dispositivo tiene el MAC de destino que se muestra?
El enrutador


e. Haz clic en `Capture / Forward` (la flecha derecha seguida de una barra vertical) para mover la PDU al siguiente dispositivo. Reúne la misma información del paso 1d. Repite este proceso hasta que la PDU llegue al destino. Registra la información de la PDU que recopiló del ping 172.16.31.5 a 10.10.10.2 en una hoja de cálculo utilizando un formato como la tabla de muestra que se muestra a continuación:

| En dispositivo | MAC de destino | MAC de origen | IPv4 de origen | IPv4 de destino |
|----------------|-----------------|---------------|----------------|-----------------|
| 172.16.31.5    | 00D0:BA8E:741A | 00D0:D311:C788| 172.16.31.5    | 10.10.10.2      |
| Switch1        | 00D0:BA8E:741A | 00D0:D311:C788| No corresponde| No corresponde  |
| Router         | 0060:2F84:4AB6 | 00D0:588C:2401| 172.16.31.5    | 10.10.10.2      |
| Switch0        | 0060:2F84:4AB6 | 00D0:588C:2401| No corresponde| No corresponde  |
| Punto de acceso| No corresponde | No corresponde| No corresponde| No corresponde  |
| 10.10.10.2     | 00D0:588C:2401 | 0060:2F84:4AB6| 10.10.10.2     | 172.16.31.5     |

## Preguntas

Responde las siguientes preguntas relacionadas con los datos capturados:

**1. ¿Se utilizaron diferentes tipos de cables/medios para conectar dispositivos?** 
   - Sí, se usaron los dos medios existentes: alambrico e inalámbrico.

**2. ¿Los cables cambiaron el manejo de la PDU de alguna manera?** 
   -  los cables solo transportan datos y paquetes de datos.

**3. ¿El Hub perdió parte de la información que recibió?** 
   -  Normalmente el hub no pierde datos y una vez recibido lo rrenvia a todos los dispositivos conectados.

**4. ¿Qué hace el hub con las direcciones MAC y las direcciones IP?** 
   -  En ambos casos el hub solo envia información a los puertos.

**5. ¿El punto de acceso inalámbrico hizo algo con la información que se le entregó**?
   -  No, la informacion se mantiene y solo se envia a diferente direccion IP.

**6. ¿Se perdió alguna dirección MAC o IP durante la transferencia inalámbrica?**
   -  No, la transferencia fue correcta.

**7. ¿Cuál fue la capa OSI más alta que utilizaron el hub y el punto de acceso ?**
   - Fue la capa 1.

**8. ¿El hub o el punto de acceso reprodujeron en algún momento una PDU rechazada con una “X” de color rojo?**
   -  Sí hubo rechazo, ya que no se enviaron correctamente los datos.
     
**9. Al examinar la ficha PDU Details, ¿qué dirección MAC apareció primero, la de origen o la de destino?**
   -  Lo primero que aparecio fue la dirección MAC.

**10. ¿Por qué las direcciones MAC aparecen en este orden?**
   -  Para enviar los datos correctamente se necesita conocer la direccion al cual se debe enviar. 

**11. ¿Había un patrón para el direccionamiento MAC en la simulación?**
   - si.

**12. ¿Los interruptores reprodujeron en algún momento una PDU rechazada con una “X” de color rojo?**
   -  No,los interruptores pueden identificar la dirección MAC de destino y realizar el envio correcto.

**13. ¿Dónde ocurrió el cambio repentino en las direcciones MAC?**
   -  En el enrutador, este es el encargado de ver las direcciones.

**14. ¿Qué dispositivo usa direcciones MAC que comienzan con 00D0: BA?**
   -  El enrutador.

**15. ¿A qué dispositivos pertenecen las otras direcciones MAC?**
   -  las direecciones pertenecen a los que envia y reciben los datos.

**16. ¿Las direcciones IPv4 de envío y recepción cambiaron los campos en alguna de las PDU?**
   -  Sí., se envian a estas PDU.

**17. ¿Se observó un cambio en las direcciones IPv4 durante el seguimiento de la respuesta a un ping?**
   -  Sí hubo cambios

**18. ¿Cuál es el patrón para el direccionamiento IPv4 utilizado en esta simulación?**
   - Cada puerto tienen sus direciones del enrutador.

**19. ¿Por qué es necesario asignar diferentes redes IP a los diferentes puertos de un router?**
   -  Cada puerto tiene su direccion para que puedan d+recibir los paquetes de datos.

**20. Si esta simulación se configura con IPv6 en lugar de IPv4, ¿cuál sería la diferencia?**
   -  Los datos se enviarían más rápido, ya que IPv6 tiene mayor ancho de banda.

