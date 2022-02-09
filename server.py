from asyncio.subprocess import STDOUT
import socket, subprocess

PORT = 6060
s = socket.socket()


def comunication(conn):
    while True:
        #print("4")
        #data = conn.recv(4096)
        #print("1")
        #command = subprocess.run(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #print("2")
        #command_to_send = command.stdout + command.stderr
        #print("3")
        #conn.send(command_to_send)

        data = conn.recv(4096)
        if data.decode() == "test":
            conn.send(data)



def server(address, backlog=1):
    try:
        s.bind(address)
        s.listen(backlog)
        print(f"Server initialized, listening on: {backlog}")

    except socket.error as error:
        print(f"Couldn't initialize connection...")
        print(error)
        print("----------------------------------------------------------------")
        print("reinitializing connection...")
        server(address, backlog=1)

    conn, client_addr = s.accept()
    print("----------------------------------------------------------------")
    print(f"Connection established with host: {client_addr}")
    print("----------------------------------------------------------------")
    comunication(conn)


if __name__ == "__main__":
    server(("", PORT))