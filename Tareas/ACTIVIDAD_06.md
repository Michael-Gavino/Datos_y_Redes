## Actividad 6: Crear una red con un switch y un router - Modo Físico

### Topología

#### Tabla de asignación de direcciones

| Dispositivo | Interfaz | Dirección IP / Prefijo | Puerta de enlace predeterminada |
|-------------|----------|------------------------|---------------------------------|
| R1          | G0/0/0   | 192.168.0.1 /24        | N/D                             |
| R1          | G0/0/0   | 2001:db8:acad: :1/64   | N/D                             |
| R1          | G0/0/0   | fe80::1                | N/D                             |
| R1          | G0/0/1   | 192.168.1.1 /24        | N/D                             |
| R1          | G0/0/1   | 2001:db8:acad:1: :1/64 | N/D                             |
| R1          | G0/0/1   | fe80::1                | N/A                             |
| S1          | VLAN 1   | 192.168.1.2 /24        | 192.168.1.1                     |
| PC-A        | NIC      | 192.168.1.3 /24        | 192.168.1.1                     |
| PC-A        | NIC      | 2001:db8:acad:1: :3/64 | fe80::1                         |
| PC-B        | NIC      | 192.168.0.3 /24        | 192.168.0.1                     |
| PC-B        | NIC      | 2001:db8:acad: :3/64   | fe80::1                         |

### Objetivos

- Parte 1: Configurar la topología
- Parte 2: Configurar los dispositivos y verificar la conectividad
- Parte 3: Mostrar información del dispositivo

## Aspectos básicos/situación

En esta actividad de Packet Tracer Modo Físico, conectará el equipo tal como se muestra en el diagrama de topología. Luego, configurará los dispositivos según la tabla de direccionamiento. Cuando se haya guardado la configuración, la verificará probando la conectividad de red.

Una vez que los dispositivos estén configurados y que se haya verificado la conectividad de red, utilizará los comandos del IOS para recuperar la información de los dispositivos y responder preguntas sobre los equipos de red. Esta actividad brinda la ayuda mínima con los comandos que se necesitan para configurar el router.

### Instrucciones

1. **Configurar la topología de red**
   - Mueva el router y el switch requeridos del Estante al Rack.
   - Mueva los PCs requeridos del Estante a la Mesa.
   - Conecta los dispositivos como se muestra en la Topologia y en la Tabla de asignación de direcciones.
   - Encienda todos los dispositivos.

2. **Configurar los dispositivos y verificar la conectividad**
   - En esta parte deberá configurar la topología de la red y los parámetros básicos, como las direcciones IP de las interfaces, el acceso de los dispositivos y las contraseñas. Consulte la Topología y la Tabla de asignación de direcciones que se encuentran al inicio de esta actividad para conocer los nombres de los dispositivos y la información de las direcciones.
   - **Asignar información de IP estática a las interfaces de la PC**
     - Configura la dirección IP, la máscara de subred y los parámetros del gateway predeterminado en la PC-A.
     - Configura la dirección IP, la máscara de subred y los parámetros del gateway predeterminado en la PC-B.
     - En una ventana con el símbolo del sistema en la PC-A, haga ping a la PC-B.

   **Pregunta:** ¿Por qué los pings no fueron correctos?

   **Configurar el router**
   - Acceda al router mediante el puerto de consola y habilite el modo EXEC con privilegios.
   - Ingresa al modo de configuración.
   - Asigna el nombre de dispositivo al router.
   - Asigna `class` como la contraseña cifrada del modo EXEC privilegiado.
   - Asigna `cisco` como la contraseña de la consola y habilite el inicio de sesión.
   - Asigne `cisco` como la contraseña de vty y habilite el inicio de sesión.
   - Encripta las contraseñas de texto sin formato.
   - Crea un aviso que advierta a todo el que acceda al dispositivo que el acceso no autorizado está prohibido.
   - Configura y activa las dos interfaces en el router.
   - Configura una descripción de interfaz para cada interfaz e indique qué dispositivo está conectado.
   - Para habilitar el enrutamiento IPv6, ingrese el comando `ipv6 unicast-routing`.
   - Guarda la configuración en ejecución en el archivo de configuración de inicio.
   - Configura el reloj en el router. (Utiliza el signo de interrogación `?` para determinar la secuencia correcta de parámetros necesarios para ejecutar este comando).
   - En una ventana con el símbolo del sistema en la PC-A, haga ping a la PC-B. (Si los pings no son correctos, es posible que debas desactivar el Firewall).

   **Pregunta:** ¿Fueron correctos los pings? Explique.

   **Configurar el switch**
   - En este paso, configure el nombre de host, la interfaz de VLAN 1 y su puerta de enlace predeterminada.
     - Acceda al switch mediante el puerto de consola y habilite al modo EXEC con privilegios.
     - Ingresa al modo de configuración.
     - Asigna un nombre de dispositivo al switch.
     - Configura y activa la interfaz VLAN en el switch S1.
     - Configura la puerta de enlace predeterminada para el switch S1.
     - Guarda la configuración en ejecución en el archivo de configuración de inicio.

   **Verificar la conectividad de extremo a extremo.**
   - Desde la PC-A, haga ping a la PC-B.
   - Desde S1, ping PC-B. Todos los pings deben tener éxito.

3. **Muestra la información del dispositivo**
   - En esta parte, utilizará los comandos show para recuperar información del router y del switch.

   **Muestra la tabla de routing en el router.**
   - Utiliza el comando `show ip route` en R1 para responder las siguientes preguntas:
     - ¿Qué código se utiliza en la tabla de enrutamiento para indicar una red conectada directamente?
     - ¿Cuántas entradas de ruta están codificadas con un código C en la tabla de enrutamiento?
     - ¿Qué tipos de interfaces están asociadas a las rutas con código C?
   - Usa el comando `show ipv6 route` en R1 para ver las rutas de IPv6.

   **Muestra la información de la interfaz en el R1.**
   - Utiliza el comando `show interface g0/0/1` para responder las siguientes preguntas:
     - ¿Cuál es el estado operativo de la interfaz G0/0/1?
     - ¿Cuál es la dirección de control de acceso a los medios (MAC) de la interfaz G0/0/1?
     - ¿Cómo se muestra la dirección de Internet en este comando?
   - Para obtener información sobre IPv6, escribe el comando `show ipv6 interface interface`.

   **Muestra una lista de resumen de las interfaces del router y del switch**
   - Existen varios comandos que se pueden utilizar para verificar la configuración de interfaz. Uno de los más útiles es el comando `show ip interface brief`. El resultado del comando muestra una lista resumida de las interfaces en el dispositivo y brinda información inmediata sobre el estado de cada interfaz.
     - Ingresa el comando `show ip interface brief` en R1.
     - Ingresa el comando `show ipv6 interface brief` en R1 para ver información de IPv6 de las interfaces.
     - Ingresa el comando `show ip interface brief` en S1.

### Preguntas

1. Si la interfaz G0/0/1 se mostrará administratively down, ¿qué comando de configuración de interfaz usaría para activar la interfaz?
2. ¿Qué ocurriría si hubiera configurado incorrectamente la interfaz G0/0/



