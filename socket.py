import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 7777))
s.listen(1)

print("Servidor de chat\n")

while True:
    print("Esperando conexión del cliente...")
    sc, addr = s.accept()
    print("Cliente conectado desde: ", addr)

    while True:
        recibido = sc.recv(1024)
        mensaje = recibido.decode()
        if  mensaje == "quit":
            print("El cliente finalizo la conexión")
            break
        print("Recibido: ", mensaje)

        nuestra_respuesta = "Hola cliente, yo soy el servidor"
        sc.send(nuestra_respuesta.encode('utf-8'))
    break

print("Adios")
sc.close()
s.close()