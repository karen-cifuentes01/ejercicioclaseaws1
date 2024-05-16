import pymysql

db_host = 'db-awscourse.ch2mia4mgchf.us-east-1.rds.amazonaws.com'
db_user = 'admin'
db_passw = 'awsCurso1'
db_name = 'db_users'

def connectionSQL():
    try:
        connection = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_passw,
            database = db_name
            )
        print("succesfull connection")
        return connection
    except Exception as err:
        print("failed connection", err)
        return None

def insert_records(id, name, lastname, birthday):
    query="INSERT INTO users (Id, Name, LastName, BirthDay) VALUES ("+id+",'"+name+"','"+lastname+"', '"+birthday+"')"
    try:
        connection = connectionSQL()
        if connection != None:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print("User added!!")
            return True
        else:
            print("Error in the connection")
            return False
    except Exception as err:
        print("Error creating the user", err)
        return False


def consult_records(id):
    query = "SELECT * FROM users WHERE id = " + id
    try:
        connection = connectionSQL()
        if connection != None:
            cursor = connection.cursor()
            cursor.execute(query)
            result= cursor.fetchall()
            print("resultado!!!",result)
            return result
        else:
            print("Error in the connection")
            return None
    except Exception as err:
        print("Error consulting the user", err)
        return None


