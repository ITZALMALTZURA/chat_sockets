import socket
BUFFER_SIZE = 4096
host = "127.0.0.1"
port = 9000

sock = socket.socket()

sock.connect((host, port))

datos = sock.recv(BUFFER_SIZE)
print (datos.decode('utf-8'))



while True:


  message = input("-->")
  sock.send(message.encode('utf-8'))
  

	

  if message == "salir":
    print("Desconectado")
    break
    
    sock.close()
