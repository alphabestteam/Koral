import socket
import os
import random
import json

class Bank:

    os.makedirs(os.path.join("./costumers"), exist_ok=True)

    def __init__(self) -> None:
        self.costumers_list = []

        if self.check_how_many_costumers_files() >= 1: # if there is a costumer
            for i in range(self.check_how_many_costumers_files()):

                costumer_path = f"./costumers/costumer{i + 1}.json"
                with open(costumer_path, "r") as fd:
                    Costumer(costumer_path)
                    self.costumers_list.append(Costumer(costumer_path))


                    # the name of the file of the costumers will be costumer + number of file 
        
    def check_how_many_costumers_files(self):
        # The function will return how many costumer files are in the costumers file

        return(len([name for name in os.listdir('./costumers') if os.path.isfile(name)]))


    def generate_account_number(self) -> int:
        return random.randint(111111111, 999999999)
    

    def withdraw_or_deposit(self, name_account:str, account_number: int, amount_money: float, action: str, other_account_name = 0, other_account_number = 0) -> None:
        enough_money = False 
        account_exists = False

        if action.lower() == "deposit" or action.lower() == "withdraw":
            for i in range(self.check_how_many_costumers_files()):
                with open(f"./costumers/costumer{i + 1}.json", "a") as fd2:
                    json_open = json.load(fd2)
                    if json_open["name"] == name_account and json_open["account number"] == account_number:
                        if action.lower() == "withdraw":

                            if json_open["balance"] > amount_money:
                                print(f"{amount_money} Withdrawn successfully!")
                                json_open["balance"] -= amount_money 
                                self.costumers[i]["balance"] -= amount_money

                            else:
                                print("Can't Withdraw! Wrote More Money Then The Current Balance!")
                                        

                        elif action.lower() == "deposit":
                            json_open["balance"] += amount_money
                            self.costumers[i]["balance"] += amount_money
                            print(f"{amount_money} deposited successfully")

            else: 
                print("Wrong Input!, Name Or Account Number Is Wrong!")
                            

        elif action.lower() == "send money":

            for i in range(self.check_how_many_costumers_files()):
                with open(f"./costumers/costumer{i + 1}.json", "a") as fd3:
                    json_open = json.load(fd3)

                    if json_open["name"] == name_account and json_open["account number"] == account_number:

                        if json_open["balance"] > amount_money:

                            enough_money = True
                            main_account_path = f"./costumers/costumer{i + 1}.json"
                            main_index = i + 1

                    if json_open["name"] == other_account_name and json_open["account number"] == other_account_number and enough_money:
                            
                            account_exists = True
                            other_account_path = f"./costumers/costumer{i + 1}.json"
                            other_index = i + 1
            
            else:
                print("Wrong Input!, Name Or Account Number Is Wrong!")
                


            if account_exists and enough_money:

                with open(main_account_path, "a") as fd3:
                    json_open = json.load(fd3)
                    json_open["balance"] -= amount_money 
                    self.costumers[main_index]["balance"] -= amount_money
                with open(other_account_path, "a") as fd4:
                    json_open = json.load(fd4)
                    json_open["balance"] -= amount_money 
                    self.costumers[other_index]["balance"] += amount_money          

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

                with open(f"./costumers/costumer{self.check_how_many_costumers_files() + 1}.json", "w") as fd1: ## adding the costumer to a file
                    costumer_info = {
                        "name" : data_name,
                        "balance" : data_balance,
                        "account number" : account_number
                    }
                    fd1.write(json.dumps(costumer_info, indent=4))
                
                new_costumer = Costumer(f"./costumers/costumer{self.check_how_many_costumers_files() + 1}.json")
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

                self.withdraw_or_deposit(data_name_account, account_number, data_amount_money, data_action)                                       

                
            elif data == '3':

                while True:
                    conn.sendall(bytes("Please Enter The Name Of Your Account: ".encode('utf-8')))
                    data_name_account = conn.recv(MEMORY).decode('utf-8')
                    conn.sendall(bytes("Please Enter Tour Account Number: ".encode('utf-8')))
                    data_account_number = conn.recv(MEMORY).decode('utf-8')
                    conn.sendall(bytes(f"Please Enter The Amount Of Money That You Want To {data_action}: ".encode('utf-8')))
                    data_amount_money = conn.recv(MEMORY).decode('utf-8')
                    conn.sendall(bytes("Please Enter The Name Of The Account You Want To Transfer Money To: ".encode('utf-8')))
                    data_name_other_account = conn.recv(MEMORY).decode('utf-8')
                    conn.sendall(bytes("Please Enter The Account Number Of The Account You Want To Transfer Money To: ".encode('utf-8')))
                    data_account_other_number = conn.recv(MEMORY).decode('utf-8')

                    self.withdraw_or_deposit(data_name_account, data_account_number, data_amount_money, "send money", data_name_other_account, data_account_other_number)

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
            self.account_number = json_open["account number"]
            self.balance = json_open["balance"]




def main():
    banka_de_espania = Bank()
    banka_de_espania.start_listen()

if __name__ == "__main__":
    main()