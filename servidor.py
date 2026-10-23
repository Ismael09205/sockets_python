import socket
import threading 

socket_servidor=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_servidor.bind(("localhost",5000))
print("Servidor corriendo :D")

def tarea (data,direccion):
    mensaje=data.decode()
    print(mensaje,"de",direccion)
    mensaje2="Hola soy el servidor muajajaja"
    socket_servidor.sendto(mensaje2.encode(),direccion)
    

while True:
    data, direccion=socket_servidor.recvfrom(1024)
    hilo=threading.Thread(target=tarea,args=(data,direccion))
    hilo.start()








