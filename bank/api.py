import socket

HOST = '127.0.0.1'
PORT = 12347
MEMORY = 1024

class Api:

    def create_account(self):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((HOST, PORT))
        my_socket.sendall(bytes("1".encode()))
        data = my_socket.recv(MEMORY)

        


def main():
    x = Api()
    x.create_account()


if __name__ == "__main__":
    main()