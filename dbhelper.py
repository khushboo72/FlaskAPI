import mysql.connector

#establishing the connection
global __mydb
def server_connection():
    __mydb = None
    if __mydb is None:
        __mydb = mysql.connector.connect(
            host='localhost',
            user='root', #enter your username here 
            password='sql_123Aqt' #enter your password here 
        )
    return __mydb


#function to create database if it does not exists 
def create_database(connection1):    
    cursor=connection1.cursor()
    query="CREATE DATABASE IF NOT EXISTS studentrecord"
    cursor.execute(query)
    connection1.commit()


#connecting to the database "studentrecord"
def get_sql_connection():
    connection1=server_connection()
    create_database(connection1)
    __mydb=None

    if __mydb is None:
        __mydb = mysql.connector.connect(
            host='localhost',
            user='root', #enter your username here 
            password='sql_123Aqt', #enter your password here 
            database='studentrecord'
            )
    return __mydb

#function to create table in database 
def create_table(connection):
    cursor = connection.cursor()
    create_studentdata=('''CREATE TABLE IF NOT EXISTS studentdata(student_id INT PRIMARY KEY AUTO_INCREMENT,studentname VARCHAR(50) NOT NULL,
            studentcity VARCHAR(50) NOT NULL,studentcontact BIGINT NOT NULL)''')
    cursor.execute(create_studentdata)
    connection.commit()
    
if __name__ == '__main__':
    connection1= server_connection()
    connection = get_sql_connection()

 