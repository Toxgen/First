import mysql.connector
from mysql.connector import Error

__pw = "5qnwpjhr027frfhrmm"

def create_server_connection(host_name, user_name, user_password):
    __connection = None
    try:
        __connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return __connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
       print("Error: database already exists")


def create_db_connection(host_name, user_name, user_password, db_name):
    __connection = None
    try:
        __connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return __connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


if __name__ == "__main__":

    __connection = create_server_connection(host_name="localhost", 
                                     user_name="root", 
                                     user_password=__pw)

    #execute = input(">> ").lower()
    #if execute in ["y", "yes"]:
    #    create_database(connection=__connection, 
    #                    query="""CREATE DATABASE stats""")
    
    __connection = create_db_connection(host_name="localhost",
                         user_name="root", 
                         user_password=__pw,
                         db_name="rpg_stats")

    #execute = input(">> ").lower()
    #if execute in ["y", "yes"]:
    #    execute_query(connection=__connection, query="""CREATE TABLE stats (
    #                client_id INT PRIMARY KEY
    #                );""") 