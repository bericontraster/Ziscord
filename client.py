# Importing libs
import socket

# Configuration
PORT = 8005
IP_ADDR = '38.180.4.98'
FORMAT = 'utf-8'
LENGTH = 1024

# Variables
connection = True
connected = True

# Creating tunnel
client_instance = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
try:
    client_instance.connect((IP_ADDR, PORT))
except:
    print(f"Server is not reachable.")
    connection = False

while connection:
    # Receiving greeting from server.
    data_receive = client_instance.recv(LENGTH)

    print(f"CONNECTED TO [{IP_ADDR, PORT}]")
    print(data_receive.decode(FORMAT))

    while connected:
        client_response = input("# ")
        client_instance.send(client_response.encode(FORMAT))
        data_receive = client_instance.recv(LENGTH)

        # Disconnecting from the server
        if data_receive.decode(FORMAT) == "leaving":
            connected = False
        elif client_response == "leave":
            connected = False
        else:
            if "+" in data_receive.decode(FORMAT):
                data_receive = data_receive.decode(FORMAT)
                details = []
                details = data_receive.split('=')
                print(f"[ZI$CORD] 200+OK\n[REGION] - {details[0]}\n[POPULATION] - {details[1]}\n[CURRENCY] - {details[2]}")
                print(f"[CAPITAL] - {details[3]}\n[TIMEZONE] - {details[4]}\n[WIKI] - {details[5]}")

            else:
                print("[ZI$CORD]",data_receive.decode(FORMAT))

    connection = False
