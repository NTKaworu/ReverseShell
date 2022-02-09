import socket, sys
IP = "192.168.1.100"
PORT = 6060
s = socket.socket()


def comunication(s):
    while True:
        command = input("--> ")
        if command == "ESC":
            s.close()
            sys.exit()
        else:
            s.send(command.encode())
            print("messaggio mandato")
            data = s.recv()
            print(str(data, "utf-8"))


def connectToServer(server_ip):
    try:
        s.connect(server_ip)
        print(f"connection established with: {server_ip}")

    except socket.error as error:
        print(f"Couldn't connect to server: {server_ip}'")
        print(error)
        print("----------------------------------------------------------------")
        print("try again? (yes/no)")
        r = input().lower()
        if r == "yes":
            connectToServer(server_ip)
        sys.exit(1)
    comunication(s)

if __name__ == "__main__":
    connectToServer((IP, PORT))