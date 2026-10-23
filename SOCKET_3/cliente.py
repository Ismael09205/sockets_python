import socket
import json
import time
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

usuarios={}

def estructuraUsuarios(cedula:str, correo: str,telefono: str,nombre: str,preferencial: bool,saldo:int):
    return{
        "cedula":cedula,
        "correo":correo,
        "telefono":telefono,
        "nombre":nombre,
        "preferencial":preferencial,
        "saldo":saldo
    }
def pedirDatos():
    cedula=input("Ingrese su cedula: ")
    correo=input("Ingrese su correo: ")
    telefono=input("Ingrese su telefono: ")
    nombre=input("Ingrese su nombre: ")
    preferencial=input("Ingrese su preferencial: ")
    saldo=input("Ingrese su saldo: ")
    return estructuraUsuarios(cedula,correo,telefono,nombre,preferencial,saldo)

def agregarUsuarios(diccionario_usuarios):
    nuevo_id = len(diccionario_usuarios) + 1
    diccionario_usuarios[nuevo_id] = pedirDatos()
   
def opcionesMenu ():
    print("----------------------------------------------")
    print("MENU DE OPCIONES")
    print("1. Agregar Usuario")
    print("2. Consultar Usuario")
    print("3. Recargar Saldo")
    print("---------------------------------------------")
    opcion=input("Seleccione la operacion a realizar: ")
    if (opcion=="1"):
        agregarUsuarios(usuarios)
        mensaje_json = json.dumps(usuarios)
        
        print("Enviando usuarios al servidor...")
        client_socket.sendto(mensaje_json.encode("utf-8"), direccion_servidor)
        
        data, direccion = client_socket.recvfrom(1024)
        respuesta = data.decode("utf-8")
        print("Respuesta del servidor: ",respuesta)
        
        
            
    if(opcion=="2"):
        print("Pendiente")
    if(opcion=="3"):
        print("Pendiente")

direccion_servidor=("localhost",5000)

while True:
    print("\n--- Agregue los datos de la persona ---")
    opcionesMenu()
    opcion = input("\nDesea agregar otro usuario? (s/n): ").strip().lower()
    if opcion != "s":
        break
    






