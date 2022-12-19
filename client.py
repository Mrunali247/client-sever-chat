import socket
import threading

FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = "IPv4 address here"
ADDR = (SERVER, PORT)
DISCONNECT_MSG = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # to connect with ip address family
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))  # To send length in encoded format
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


print("Press 0 Disconnect")
while True:
    m = input("Enter message::")
    if m == "0":
        send(DISCONNECT_MSG)
        break
    send(m)
