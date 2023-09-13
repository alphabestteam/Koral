import socket

def main():
    HOST = '127.0.0.1'
    PORT = 12345
    MEMORY = 1024
    
    while True:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((HOST, PORT))
        message = input("Please enter your desired message: ")
        my_socket.sendall(bytes(message, 'utf-8'))
        data = my_socket.recv(MEMORY).decode('utf-8')
        print(f"Received {str(data)}")

if __name__ == "__main__":
    main()