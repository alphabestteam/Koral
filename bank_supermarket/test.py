import os
def main():
    os.makedirs(os.path.join("./costumers"),exist_ok=True)
    print(len([name for name in os.listdir('./costumers/')]))
    
if __name__ == "__main__":
    main()