import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
direccion_servidor=("localhost",5000)



while True:
    mensaje=input("Ingrese el mensaje o 0 para salir: ")
    client_socket.sendto(mensaje.encode(),direccion_servidor)
    data, direccion=client_socket.recvfrom(1024)
    
    if(mensaje=="0"):
        break
    






