# Actividad 11: Conceptos de introducción a las redes

## Objetivos

### Fundamentos de redes:
1. Comprender los conceptos básicos de ARPANET y su importancia histórica en el desarrollo de Internet.
2. Identificar el papel de un backbone en una red de computadoras y su función en el enrutamiento de datos.
3. Describir las características principales de la tecnología Bluetooth y su aplicación en redes inalámbricas de corto alcance.
4. Explicar el concepto de broadcast en redes de computadoras y su uso para la difusión de datos a múltiples destinatarios.
5. Entender el funcionamiento y la importancia de la memoria caché en la optimización del rendimiento de las redes.
6. Explicar el propósito y el proceso de la comprobación de integridad mediante checksum en la transferencia de datos.
7. Comprender la diferencia entre un cliente y un servidor en un entorno de red cliente-servidor y cómo interactúan entre sí.
8. Identificar los principios básicos de encriptación y descifrado, así como la importancia de la gestión de claves de cifrado.
9. Describir cómo se implementa la seguridad de red mediante firewalls y el papel que desempeñan en la protección de la red contra amenazas externas.
10. Analizar el protocolo TCP/IP y su papel en la comunicación de datos en Internet, incluida la diferencia entre TCP y UDP.
11. Identificar los componentes básicos de una red Ethernet, como los hubs, switches y routers, y entender su función en la conectividad de red.
12. Describir la topología de una red de área local (LAN) y compararla con una red de área amplia (WAN) en términos de alcance y tecnologías utilizadas.
13. Explicar el concepto de direccionamiento MAC y su importancia en la comunicación de datos a nivel de enlace de datos.
14. Comprender el papel de los dispositivos de red como los repetidores y los routers en la interconexión de redes y el enrutamiento de datos.
15. Analizar el modelo OSI y su estructura de capas para entender cómo se lleva a cabo la comunicación de datos en una red.
16. Explorar el concepto de conmutación de paquetes y su importancia en la transferencia eficiente de datos en redes de computadoras.
17. Identificar los diferentes tipos de redes, como las redes peer-to-peer y las redes cliente-servidor, y comprender sus características y aplicaciones.
18. Entender los principios básicos de la comunicación unicast, multicast y broadcast en una red y cómo se utilizan en diferentes escenarios.
19. Describir la función de los protocolos de enrutamiento como el protocolo de enrutamiento por vectores de distancia (RIPv2) y el protocolo de enrutamiento por estado de enlace (OSPF) en la determinación de rutas de red.
20. Analizar la importancia de los estándares de comunicación como los RFC en la interoperabilidad y el desarrollo de tecnologías de red.

## Conceptos dados en clase

- ARPANET
- Backbone
- Bluetooth
- Broadcast
- Cache memory
- Checksum
- Client
- Client–server network
- Computer network
- CRC
- DDN
- Encryption and decryption
- Encryption key
- Ethernet
- Firewall
- Frame Relay
- Gateway
- Hub
- Internet
- LAN
- MAC address
- MODEM
- Multicast
- Network cache
- Network device
- NIC
- Nonce value
- OSI model
- Packet switching
- Peer-to-peer network
- Private key
- Protocol
- Protocol stack
- Public key
- Repeater
- RFC
- Router
- Server
- Switch
- TCP/IP
- Topology
- Unicast
- WAN

# Problema 1: Diseño de red segura

## Escenario
Una empresa necesita diseñar una red segura que conecte tres sucursales ubicadas en diferentes ciudades utilizando tecnología WAN y LAN. La empresa maneja datos confidenciales y requiere que la comunicación entre sucursales sea cifrada.

### Preguntas
1. ¿Qué tipo de tecnología de WAN utilizarías para conectar las sucursales y por qué? (Considera opciones como Frame Relay, MPLS, etc.)
2. Describe cómo implementarías el cifrado en la red. ¿Qué tipos de claves y protocolos utilizarías?
3. Dibuja una topología de red que incluya dispositivos como routers, switches y firewalls. Explica la función de cada dispositivo en tu diseño. Puedes utilizar Packet Tracer.
4. ¿Cómo garantizarías la integridad y autenticidad de los datos transmitidos entre las sucursales? Detalla el uso de checksums o CRC.

## Requisitos
1. Conexión WAN Segura: Utilizar VPNs para asegurar todas las comunicaciones entre sucursales.
2. Cifrado: Implementar cifrado de extremo a extremo.
3. Topología de Red: Incluir dispositivos de red como routers, switches y firewalls.
4. Automatización: Usar Python para configurar aspectos de la red automáticamente.

### Parte 1: Diseño de topología de red

#### Preguntas
1. Dibuja una topología de red para este escenario que incluya los dispositivos de red necesarios en cada sucursal.
2. Explica cómo cada dispositivo contribuye a la seguridad y eficiencia de la red.

### Parte 2: Configuración de VPN con Python

Utilizando la biblioteca paramiko de Python, escribe un script que configure una VPN en los routers de cada sucursal. Supondremos que los routers son dispositivos Cisco y que el script debe configurar automáticamente la VPN utilizando IPsec.

```python
import paramiko

def connect_to_router(hostname, username, password):
    """
    Establece una conexión SSH con el router utilizando Paramiko.

    Args:
    - hostname (str): Dirección IP del router.
    - username (str): Nombre de usuario para autenticación SSH.
    - password (str): Contraseña para autenticación SSH.

    Returns:
    - client (paramiko.SSHClient): Cliente SSH conectado al router.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    return client

def configure_ipsec_vpn(client, peer_ip, local_network, remote_network):
    """
    Configura una VPN IPsec en el router utilizando comandos de Cisco IOS.

    Args:
    - client (paramiko.SSHClient): Cliente SSH conectado al router.
    - peer_ip (str): Dirección IP del extremo remoto de la VPN.
    - local_network (str): Red local a proteger por la VPN en formato 'ip máscara'.
    - remote_network (str): Red remota a través de la VPN en formato 'ip máscara'.

    Returns:
    - None
    """
    commands = [
        'crypto isakmp policy 10',
        'encr aes 256',
        'authentication pre-share',
        'group 5',
        'crypto isakmp key mysharedsecret address ' + peer_ip,
        'crypto ipsec transform-set myset esp-aes 256 esp-sha-hmac',
        'crypto map mymap 10 ipsec-isakmp',
        'set peer ' + peer_ip,
        'set transform-set myset',
        'match address 100',
        'access-list 100 permit ip ' + local_network + ' ' + remote_network,
        'interface g0/0',
        'crypto map mymap',
        'end'
    ]
    for command in commands:
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read().decode())
    client.close()

# Ejemplo de uso
hostname = '192.168.1.1'
username = 'admin'
password = 'password'
client = connect_to_router(hostname, username, password)
configure_ipsec_vpn(client, '192.168.2.1', '192.168.1.0 255.255.255.0', '192.168.3.0 255.255.255.0')
```

