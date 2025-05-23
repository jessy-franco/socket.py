import socket
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("127.0.0.1", 7777))

while True:
    mensaje = str(input(">> "))
    if mensaje.lower() == "salir":
        break 

    socket_cliente.send(mensaje.encode("utf-8"))

    recibido = socket_cliente.recv(1024)
    print ("Recibido: ", recibido.decode())
    

print("adios")
socket_cliente.close()