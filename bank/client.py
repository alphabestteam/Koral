import socket
from api import Api
def main():
    HOST = '127.0.0.1'
    PORT = 12347
    MEMORY = 2048
    
    while True:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((HOST, PORT))
        my_socket.recv(MEMORY)
        data = input()
        
        if bytes(data.encode()) == 1 : 
            my_socket.recv(MEMORY)
            account_name = input()
            my_socket.recv(MEMORY)
            account_balance = input()
            Api.create_account(account_name, account_balance)

        elif bytes(data.encode()) == 2:
            
            my_socket.recv(MEMORY)
            action = input()
            my_socket.recv(MEMORY)
            account_name = input()
            my_socket.recv(MEMORY)
            account_number = input()
            my_socket.recv(MEMORY)
            amount_money = input()

            if action == "deposit":
                Api.deposit_money(account_name, account_number, amount_money)

            elif action == "withdraw":
                Api.withdraw_money(account_name, account_number, amount_money)

        elif bytes(data.encode()) == 3:
            my_socket.recv(MEMORY)
            account_name = input()
            my_socket.recv(MEMORY)
            account_number = input()
            my_socket.recv(MEMORY)
            amount_money = input()
            my_socket.recv(MEMORY)
            other_account_name = input()
            my_socket.recv(MEMORY)
            other_account_number = input()
            Api.transfer_money(account_name, account_number, amount_money, other_account_name, other_account_number)

    
if __name__ == "__main__":
    main()