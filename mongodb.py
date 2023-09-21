import pymongo          


def main():
    connection_string = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(connection_string)
    mydb = client["Aviv's_People"]
    army = mydb["Army"]
    friends = mydb["Friends"]
    family = mydb["Family"]

    """
    Method 1: 
    insert using _id
    """

    person = {"_id": 10000, "name": "Aviv", "age": 20, "role" : "Backend"} 
    #army.insert_one(person )

    """
    Method 2:
    insert using insert_one()
    """

    # army.insert_one({"_id": 10001, "name": "Lihi" , "age": 21 , "role": "QA"})
    
    """
    Method 3:
    insert using insert_many()
    """
    """
    army.insert_many([
        {"_id": 10002, "name": "Gabi" , "age": 22 , "role":"DevOps"},
        {"_id": 10003, "name": "Ori", "age": 23, "role":"Front-end"},
        {"_id": 10004, "name": "Ido", "age": 22, "role":"Developer"},
        {"_id": 10005, "name": "Yarden", "age": 24, "role":"DevOps"}
    ]) 

    friends.insert_many([
        {"name": "Amit", "age": 20, "role": "waiter"},
        {"name": "Yonatan", "age": 24, "role": "doctor"},
        {"name": "Noa", "age": 22, "role": "student"},
        {"name": "Michal", "age": 21, "role": "baker"}
    ])

    family.insert_many([
        {"place in family": "mother" , "age": 45, "role": "teacher"},
        {"place in family": "father", "age": 46, "role": "engineer"},
        {"place in family": "brother", "age": 12, "role": "schoo"},
        {"place in family": "sister", "age": 24, "role": "student"},
    ])

    """
    """
    Printing the data of each collection
    """

    print("Army collection: \n")

    for x in army.find():
        print(x)

    print("\nFriends collection: \n")

    for x in friends.find():
        print(x)

    print("\nFamily collection: \n")

    for x in family.find():
        print(x)


    army.delete_one({"_id": 11, "name": "Lihi" , "age": 21 , "role": "QA"})


if __name__ == "__main__":
    main()