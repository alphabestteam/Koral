from Point1 import Point

def main():
    obj1 = Point(4, 8)
    obj2 = Point(4, 8)

    print(obj1 == obj2) ## checks if the memory address is the same
    
    print(obj1) ## prints the memory address
    
    print(obj2) ## prints the memory address
    
    print(obj1 + obj2) # TypeError Exception , can't compare 2 objects



if __name__ == "__main__":
    main()