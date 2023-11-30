import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv


app = Flask(__name__)


load_dotenv() # to load the .env file 


def connect_to_db(): #to connect to db
    try:
        connection = mysql.connector.connect(host=os.getenv("MYSQL_HOST"), database=os.getenv("MYSQL_DB"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), port=3306)
        if connection.is_connected():
            return connection

    except Error as error:
        print("Couldn't connect to db", error)


def add_db(): #checks if the db is exists, if not , create a new one
    connection = connect_to_db()
    with connection.cursor(dictionary=True) as cursor: # open a cursor
        cursor.execute(f"SHOW TABLES LIKE 'users'")
        is_table = cursor.fetchone() # fetch all data

        if not is_table: # if the table is not exists, create a new one named "users" 
            cursor.execute(f"CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")


@app.route("/users", methods = ["POST"])
def add_user():
    connection = connect_to_db()
    add_db()
    data = request.json
    try:
        name = data.get("name")
        query = f"INSERT INTO users (name) VALUES ('{name}')"
        with connection.cursor(dictionary=True) as cursor: # open a cursor
            cursor.execute(query)
            connection.commit()
            id = cursor.lastrowid # to get the id of that user

        cursor.close()
        connection.close()
        return (f"User {name} was successfully added to the database with the id: {id}")

    except Error as error:
        return jsonify({error})


@app.route("/users", methods = ["GET"])
def get_users():
    connection = connect_to_db()
    add_db()
    try:
        query = f"SELECT * FROM users;"
        with connection.cursor(dictionary=True) as cursor: # open a cursor
            cursor.execute(query)
            users = cursor.fetchall() # fetch all data
        cursor.close()
        connection.close()
        return jsonify(users)

    except Error as error:
        return jsonify({error})
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)