import socket

MEMORY = 2048
class Api:

    def connect_to_server(self, ip: int, port: int, action: str, account_name, account_balance = "0", account_number = "0" , amount_of_money_to_deposit = "0", other_account_name = "0", other_account_number = "0"):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((ip, port))

        if action == "create_account":
            self.create_account(my_socket, account_name, account_balance)

        elif action == "deposit_money":
            self.deposit_money(my_socket, account_name, account_number, amount_of_money_to_deposit)

        elif action == "withdraw_money":
            self.withdraw_money(my_socket, account_name, account_number, amount_of_money_to_deposit)
            
        elif action == "transfer_money":
            self.transfer_money(my_socket, account_name, account_number, amount_of_money_to_deposit, other_account_name, other_account_number)

    def create_account(self, my_socket, account_name, account_balance):

        my_socket.recv(MEMORY)
        my_socket.sendall(bytes("1".encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(account_name.encode()))
        my_socket.recv(MEMORY)
        my_socket.sendall(bytes(account_balance.encode()))
        my_socket.detach()


    def deposit_money(self, my_socket, account_name, account_number, amount_of_money_to_deposit):

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
        my_socket.detach()

    
    def withdraw_money(self, my_socket, account_name, account_number, amount_of_money_to_deposit):

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
        my_socket.detach()



    def transfer_money(self, my_socket, account_name, account_number, amount_of_money_to_deposit, other_account_name, other_account_number):

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
        my_socket.detach()
