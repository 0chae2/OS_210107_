import socket 
import pickle # python json serialize custom object!!!

HEADER = 64 #server recieved byte
PORT = 5050 # process numbering logic unit for example 8080 or 8000 is web site
SERVER = "127.0.1.1" #automatic get adress
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE ='!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("hi")
send_ind = str(input())
print(type(send_ind))
send(send_ind)
send(DISCONNECT_MESSAGE)