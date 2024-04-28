# Problema 2: Implementación de un protocolo de red personalizado sobre TCP

## Contexto

Diseñar un protocolo de aplicación personalizado para un sistema de archivos distribuido que se ejecutará sobre TCP, utilizando técnicas como multiplexación y control de flujo.

## Requisitos

- Definir el formato del mensaje, incluyendo cabeceras y extensiones de cabecera.
- Desarrollar un esquema de control de flujo que gestione eficazmente la transferencia de archivos grandes a través de redes con alta latencia.
- Escribir un pseudocódigo para las funciones de conexión, como el handshake de tres vías de TCP, y cómo se manejará la retransmisión.
- Evaluar el uso de NAT y su impacto en las conexiones de red en este protocolo, particularmente cuando se utilizan direcciones IP dinámicas.

## Objetivos

1. **Diseño del protocolo**: Definir el formato del mensaje, incluidas las cabeceras y las extensiones de cabecera para manejar funcionalidades específicas como control de flujo y recuperación de errores.
2. **Implementación de control de flujo**: Desarrollar un esquema de control de flujo para manejar eficazmente la transferencia de datos sobre TCP.
3. **Simulación con Python**: Simular el protocolo utilizando Python para evaluar su rendimiento y robustez en escenarios de red simulados.

## Paso 1: Diseño del protocolo

Vamos a definir un protocolo simple que incluya operaciones básicas como PUT, GET y DELETE para interactuar con archivos en el sistema distribuido.

### Ejemplo de Especificación del Protocolo

- **PUT**: Enviar un archivo al sistema.
- **GET**: Recuperar un archivo del sistema.
- **DELETE**: Eliminar un archivo del sistema.

Cada mensaje tendrá una cabecera que incluye el tipo de operación, el tamaño del mensaje, y un número de secuencia para el control de flujo y la recuperación de errores.

| Tipo de operación | Tamaño del mensaje | Secuencia de pseudocódigo | Evaluación NAT |
|-------------------|--------------------|-----------------------------------|----------------|
|PUT | GET |  DELETE | DATOS |
|Enviar un archivo | Recuperar un archivo | Eliminar un archivo del sistema |  Verificar la conexion entre el cliente y el servidor  |



## Paso 2: Implementación de control de flujo

Usaremos un mecanismo de control de flujo basado en ventana deslizante para asegurar la entrega fiable y eficiente de los archivos, especialmente en redes con alta latencia.

### Código Python para simulación del protocolo

```python
import socket
import struct

def send_message(sock, msg_type, seq_num, data):
    header = struct.pack('!I I', msg_type, seq_num)
    message = header + data.encode()
    sock.sendall(message)

def receive_message(sock):
    header = sock.recv(8)
    msg_type, seq_num = struct.unpack('!I I', header)
    data = sock.recv(1024)  # ajustar según el tamaño esperado del mensaje
    return msg_type, seq_num, data.decode()

def main():
    host = 'localhost'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print("Server listening on port", port)

    client_sock, addr = server.accept()
    print("Connected by", addr)

    # Simulación de recepción de un mensaje
    msg_type, seq_num, data = receive_message(client_sock)
    print("Received:", msg_type, seq_num, data)

    # Envío de una respuesta
    send_message(client_sock, 1, seq_num + 1, "Ack")

    client_sock.close()
    server.close()

if __name__ == '__main__':
    main()

