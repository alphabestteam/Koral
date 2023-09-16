import socket

HOST = '127.0.0.1'
PORT = 12347
MEMORY = 2048

class Api:

    def create_account(self, account_name, account_balance):
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            my_socket.connect((HOST, PORT))
            my_socket.recv(MEMORY)
            my_socket.sendall(bytes("1".encode()))
            my_socket.recv(MEMORY)
            my_socket.sendall(bytes(account_name.encode()))
            my_socket.recv(MEMORY)
            my_socket.sendall(bytes(account_balance.encode()))


    def deposit_money(self, account_name, account_number, amount_of_money_to_deposit):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((HOST, PORT))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes("2".encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes("deposit".encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(account_name.encode()))            
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(account_number.encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(amount_of_money_to_deposit.encode()))

    
    def withdraw_money(self, account_name, account_number, amount_of_money_to_deposit):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((HOST, PORT))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes("2".encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes("withdraw".encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(account_name.encode()))            
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(account_number.encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(amount_of_money_to_deposit.encode()))


    def transfer_money(self, account_name, account_number, amount_of_money_to_deposit, other_account_name, other_account_number):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((HOST, PORT))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes("3".encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(account_name.encode()))            
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(account_number.encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(amount_of_money_to_deposit.encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(other_account_name.encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(other_account_number.encode()))
