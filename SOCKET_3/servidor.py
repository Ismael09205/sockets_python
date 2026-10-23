import json
import socket
import threading

socketP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
direccion = ("localhost", 5000)
socketP.bind(direccion)

registros = {}


def tarea(data, direccion):
    
        usuarios = json.loads(data.decode("utf-8"))

        registros[direccion] = usuarios

        print("\n==============================")
        print("DATOS RECIBIDOS DESDE CLIENTE")
        print("===============================")

    
        if isinstance(usuarios, dict):
            for user_id, datos in usuarios.items():
                print(f"ID Usuario: {user_id}")
                print(f"- Cedula: {datos.get('cedula')}")
                print(f"- Nombre: {datos.get('nombre')}")
                print(f"- Correo: {datos.get('correo')}")
                print(f"- Telefono: {datos.get('telefono')}")
                print(f"- Preferencial: {datos.get('preferencial')}")
                print(f"- Saldo: ${datos.get('saldo')}")
                print("-" * 30)

        mensaje_respuesta = "Servidor: Datos de usuarios recibidos y registrados correctamente."
        socketP.sendto(mensaje_respuesta.encode("utf-8"), direccion)

print("Servidor UDP levantado")

while True:
    data, direccion_cliente = socketP.recvfrom(1024)

    hilo = threading.Thread(target=tarea, args=(data, direccion_cliente))
    hilo.start()