import pymongo          


def main():
    connection_string = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(connection_string)
    mydb = client["Aviv's_People"]
    army = mydb["Army"]
    friends = mydb["Friends"]
    family = mydb["Family"]

    """
    Ex 1: 
    """
    under_23 = army.find_one({"age": {"$lt" : 23}, "role": "DevOps"})

    """
    Ex 2:
    """
    
    age_under_23 = under_23["age"]
    role_under_23 = under_23["role"]

    friend_of_under_23 = army.find_one({"age" : age_under_23, "role": {"$ne" : role_under_23}})    

    role_friend_of_under_23 = friend_of_under_23["role"]

    army.update_one({"age": age_under_23, "role": role_under_23}, {"$set": {"role" : role_friend_of_under_23}})
    

    """
    Ex 3:
    """

    mydb.army.aggregate(
        [
            { "$sort" : {'age' : 1}}
        ]
    )


    for x in army.find():
        if x["age"] > 23:
            friends.insert_one(x)
            army.delete_one(x)


if __name__ == "__main__":
    main()