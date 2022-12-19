import socket
import threading

FORMAT = 'utf-8'
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # IPv4 address here
ADDR = (SERVER, PORT)
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # to connect with ip address family
server.bind(ADDR)  # bound socket with address


# To handle communication in parallel for each
def handle_client(conn, addr):
    # message format ::: "5"
    #                    "Hello"
    print(f"{addr} Connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)   # To know the length of incoming msg
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)  # To get actual message
            if msg == DISCONNECT_MSG:
                connected = False
                conn.send(f"Form server::DISCONNECTED".encode(FORMAT))
                print(f"{addr} :: DISCONNECTED")
                break
            print(f"{addr} :: {msg}")
            conn.send(f"Form server::Message received {msg}".encode(FORMAT))
    # To handle connection
    conn.close()


def start():
    server.listen()  # to listen to connections
    print(f"Listening on {SERVER}, Port {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # To use call handle client in other thread
        thread.start()
        print(f"Active connections::: {threading.activeCount() -1}")


print("Server is starting")
start()