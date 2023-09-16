import socket
import os
import random
import json

class Bank:

    os.makedirs(os.path.join("./costumers"), exist_ok=True)

    def __init__(self) -> None:
        self.costumers_list = []

        if self.check_how_many_costumers_list_files() >= 1: # if there is a costumer
            for i in range(self.check_how_many_costumers_list_files()):

                costumer_path = f"./costumers/costumer{i + 1}.json"
                with open(costumer_path, "r") as fd:
                    Costumer(costumer_path)
                    self.costumers_list.append(Costumer(costumer_path))


                    # the name of the file of the costumers_list will be costumer + number of file 
        
    def check_how_many_costumers_list_files(self):
        # The function will return how many costumer files are in the costumers_list file
        return(len([name for name in os.listdir('./costumers/')]))


    def generate_account_number(self) -> int:
        return random.randint(111111111, 999999999)
    

    def withdraw_or_deposit(self, name_account: str, account_number: int, amount_money: float, action: str, other_account_name = 0, other_account_number = 0) -> None:
        enough_money = False 
        account_exists = False
        if action.lower() == "deposit" or action.lower() == "withdraw":
            for i in range(self.check_how_many_costumers_list_files()):
                with open(f"./costumers/costumer{i + 1}.json", "r") as fdd:
                    json_open = json.load(fdd)
                with open(f"./costumers/costumer{i + 1}.json", "w") as fd2:


                    if json_open["name"] == name_account and json_open["account number"] == account_number:
                        if action.lower() == "withdraw":

                            if json_open["balance"] > amount_money:
                                print(f"{amount_money} NIS Withdrawn successfully!")
                                json_open["balance"] -= int(amount_money)
                                json.dump(json_open, fd2)
                                self.costumers_list[i].balance -= int(amount_money)
                                break

                            else:
                                print("Can't Withdraw! Wrote More Money Then The Current Balance!")
                                        

                        elif action.lower() == "deposit":
                            print()
                            json_open["balance"] += int(amount_money)
                            json.dump(json_open, fd2)
                            self.costumers_list[i].balance += int(amount_money)
                            print(f"{amount_money} NIS deposited successfully!")
                            break

            else: 
                print("Wrong Input! Name Or Account Number Is Wrong!")
                            

        elif action.lower() == "send money":

            for i in range(self.check_how_many_costumers_list_files()):
                with open(f"./costumers/costumer{i + 1}.json", "r") as fd3:
                    json_open = json.load(fd3)
                with open(f"./costumers/costumer{i + 1}.json", "a") as fd4:
                    if json_open["name"] == name_account and json_open["account number"] == account_number:
                        if json_open["balance"] > amount_money:
                            print("here")
                            enough_money = True
                            main_account_path = f"./costumers/costumer{i + 1}.json"
                            main_index = i + 1
                    
                    if json_open["name"] == other_account_name and json_open["account number"] == other_account_number:
                            print("here2")
                            account_exists = True
                            other_account_path = f"./costumers/costumer{i + 1}.json"
                            other_index = i + 1
            
            if not (account_exists and enough_money):
                print("Wrong Input! Name Or Account Number Is Wrong!")
                


            if account_exists and enough_money:
                print(main_index)
                print(other_index)

                with open(main_account_path, "r") as fdd1:
                    json_open = json.load(fdd1)

                with open(main_account_path, "w") as fd3:
                    json_open["balance"] -= amount_money
                    self.costumers_list[main_index - 1].balance -= amount_money
                    json.dump(json_open, fd3,indent=4)

                with open(other_account_path, "r") as fdd2:
                    json_open = json.load(fdd2)

                with open(other_account_path, "w") as fd4:
                    json_open["balance"] += amount_money
                    self.costumers_list[other_index - 1].balance += amount_money
                    json.dump(json_open, fd4,indent=4)


        else:
            print("Wrong Action Name!")
   


    def start_listen(self):
        HOST = '127.0.0.1'
        PORT = 12347
        MEMORY = 2048

        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.bind((HOST, PORT))
        my_socket.listen()
        while True:
            conn, addr = my_socket.accept()
            conn.sendall(bytes("Please Enter The Number Of Your Desired Action : \n 1 - Create Account \n 2 - Withdraw / Deposit money \n 3 - Send Money To Other Accounts\n 'stop' to exit the menu".encode('utf-8')))
            data = conn.recv(MEMORY).decode('utf-8')


            if data == '1':

                conn.sendall(bytes("Please Enter Your Name:".encode('utf-8')))
                data_name = conn.recv(MEMORY).decode('utf-8')
                conn.sendall(bytes("Please Enter The Starting Balance:\n".encode('utf-8')))
                data_balance = conn.recv(MEMORY).decode('utf-8')
                account_number = self.generate_account_number()

                with open(f"./costumers/costumer{self.check_how_many_costumers_list_files() + 1}.json", "w") as fd1: ## adding the costumer to a file
                    costumer_info = {
                        "name" : data_name,
                        "balance" : int(data_balance),
                        "account number" : int(account_number)
                    }
                    fd1.write(json.dumps(costumer_info, indent=4))
                
                new_costumer = Costumer(f"./costumers/costumer{self.check_how_many_costumers_list_files()}.json")
                self.costumers_list.append(new_costumer)


            elif data == '2':
                conn.sendall(bytes("Please Enter The Action:\n Withdraw / Deposit:\n".encode('utf-8')))
                data_action = conn.recv(MEMORY).decode('utf-8')
                conn.sendall(bytes("Please Enter The Name Of The Account: ".encode('utf-8')))
                data_name_account = conn.recv(MEMORY).decode('utf-8')
                conn.sendall(bytes("Please Enter The Account Number: ".encode('utf-8')))
                data_account_number = conn.recv(MEMORY).decode('utf-8')
                conn.sendall(bytes(f"Please Enter The Amount Of Money That You Want To {data_action}: ".encode('utf-8')))
                data_amount_money = conn.recv(MEMORY).decode('utf-8')

                self.withdraw_or_deposit(data_name_account, int(data_account_number), int(data_amount_money), data_action)                                       

                
            elif data == '3':

                conn.sendall(bytes("Please Enter The Name Of Your Account: ".encode('utf-8')))
                data_name_account = conn.recv(MEMORY).decode('utf-8')
                conn.sendall(bytes("Please Enter Your Account Number: ".encode('utf-8')))
                data_account_number = conn.recv(MEMORY).decode('utf-8')
                conn.sendall(bytes(f"Please Enter The Amount Of Money".encode('utf-8')))
                data_amount_money = conn.recv(MEMORY).decode('utf-8')
                conn.sendall(bytes("Please Enter The Name Of The Account You Want To Transfer Money To: ".encode('utf-8')))
                data_name_other_account = conn.recv(MEMORY).decode('utf-8')
                conn.sendall(bytes("Please Enter The Account Number Of The Account You Want To Transfer Money To: ".encode('utf-8')))
                data_account_other_number = conn.recv(MEMORY).decode('utf-8')

                self.withdraw_or_deposit(data_name_account, int(data_account_number), int(data_amount_money), "send money", data_name_other_account, int(data_account_other_number))

            else: 
                print("Wrong Input! Try Again!")
                break

            if(data == "Stop"):
                break

        my_socket.close()


class Costumer:
    def __init__(self, path: str) -> None:
        self.path = path

        with open(path, "r") as fd5:

            json_open = json.load(fd5)
            self.name = json_open["name"]
            self.balance = json_open["balance"]
            self.account_number = json_open["account number"]
