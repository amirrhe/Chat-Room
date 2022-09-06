import socket
from threading import Thread

host = '127.0.0.1'
port = 1023
clients = {}
addresses = {}
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))

def handle_client(conn,address):
    name = conn.recv(1024).decode()
    welcome ="welcome"+name+"you can type #quit if you want to leave"
    conn.send(bytes(welcome,"utf8"))
    msg =name  +"has recently join chat room "
    boardcast(bytes(msg,"utf8"))
    clients[conn]=name
    
    while True:
        msg = conn.recv(1024)
        if msg != bytes("#quit",'utf8'):
            boardcast(msg,name+":")
        else:
            conn.send(bytes("#quit",'utf8'))
            conn.close()
            del clients[conn]
            boardcast(bytes(name+"has left chatroom",'utf8'))
            

def accept_client_connection():
    while True:
        client_conn,client_address =sock.accept()
        print(client_address,"has connected")
        client_conn.send("welcome to chat room , type your name".encode('utf-8'))
        addresses[client_conn] = client_address
        Thread(target=handle_client,args=(client_conn,client_address))
        
def boardcast(msg,prefix=""):
    for x in clients:
        x.send(bytes(prefix,'utf8')+msg)
    
    
    
if __name__ == '__main__':
    sock.listen(5)
    print("server is runnig and listening to client requests")
    t1 = Thread(target=accept_client_connection)
    t1.start()
    t1.join()
    
    







