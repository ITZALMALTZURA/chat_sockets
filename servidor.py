import socket
import threading
BUFFER_SIZE = 4096

host = "127.0.0.1"
port = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Conexion Creada")
sock.bind((host, port))
print ("Conexion aceptada")
sock.listen(10)
print ("welcome to my jungle")


def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('Conexion con {}.'.format(addr))
        conn.send("Cliente conectado".encode('UTF-8'))
        while True:
            datos = conn.recv(BUFFER_SIZE)
            if datos:
                print('Recibido: {}'.format(datos.decode('utf-8')))
                
            else:
                print("Cliente desconectado")              
                break
    finally:
        conn.close()
        	
while 1:
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr)).start()
