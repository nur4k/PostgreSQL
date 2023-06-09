import psycopg2

from config import host, db_name, user, password


try:
    connection = psycopg2.connect(
        host=host, 
        database=db_name,
        user=user, 
        password=password
    )

    connection.autocommit = True #autocommit
    # check connection
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version()"
        )
        print(f"SELECT version:", cursor.fetchone())
    # create table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
            id serial PRIMARY KEY,
            name varchar(50) NOT NULL,
            nickname varchar(50) NOT NULL);"""
        )
        print(f"Table created")
    # insert data 
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users(
            name,nickname) 
            values('Malika', 'HustleGirl');"""
        )
        print(f"Table inserted")
    # select row
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM users;"""
        )
        print(cursor.fetchall())
    # drop database
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP DATABASE users;"""
        )
        print("[INFO] DATABASE was deleted")
except Exception as e:
    print("[INFO] Error while working with PostgresSQL", e)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgresSQL closed")