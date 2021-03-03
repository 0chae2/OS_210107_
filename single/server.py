import socket 
import threading
#import time

#time.sleep(1)
#print("hi")
HEADER = 64 #server recieved byte
PORT = 5050 # process numbering logic unit for example 8080 or 8000 is web site
#SERVER = "10.42.0.237"
SERVER = socket.gethostbyname(socket.gethostname()) #automatic get adress
ADDR = (SERVER, PORT)
print(SERVER)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE ='!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(family.type, standard option)inet type / streaming data
server.bind(ADDR) #

#listening and print
def handle_client(conn, addr): #connetion, address
    print(f"[New connection] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("msg received".encode(FORMAT))
    conn.close()

    pass
def start():
    server.listen()
    print("[listening] server is listening {SERVER}")
    while True:
        conn, addr = server.accept() #new connection 
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[active connections]{threading.activeCount() - 1}")
    pass
print("starting server is")
start()

# ctrl + [ or ] : indent move
