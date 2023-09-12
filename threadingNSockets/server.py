import socket


def main():
    HOST = '127.0.0.1'
    PORT = 12345
    MEMORY = 1024

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((HOST, PORT))
    my_socket.listen()
    print(f"Server started listening on host : {HOST} and port: {PORT}")

    while True:

        conn, addr = my_socket.accept()
        print(f"connected by {addr}")
        data = conn.recv(MEMORY).decode('utf-8')

        if(data == "Stop"):
            break
        
        if(data):
            print(f"received {str(data)}")
            conn.sendall(bytes(data.upper().encode('utf-8')))
            my_socket.listen()


    my_socket.close()


if __name__ == "__main__":
    main()
