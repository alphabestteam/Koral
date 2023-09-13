import os
def main():
    os.makedirs(os.path.join("./costumers"),exist_ok=True)
    print(len([name for name in os.listdir('./costumers') if os.path.isfile(name)]))
    with open("./costumers/sdf.txt", "r") as fd:
        print(fd.read())
if __name__ == "__main__":
    main()