import psycopg2
from psycopg2._psycopg import connection

def connect_to_db():
    try:
        conn = psycopg2.connect(host="localhost", port="5432", database="passwordmanager", user="kartik", password="testPass")
        return conn

    except (Exception, psycopg2.Error) as error:
        print("Could not connect", error)


def storing(password, email, username, link, app_name):
    try:
        conn = psycopg2.connect(host="localhost", port="5432", database="passwordmanager", user="kartik", password="testPass")
        cursor = conn.cursor()
        query_to_insert = "INSERT INTO accounts (password, email, username, link, app_name) VALUES (%s, %s, %s, %s, %s)"
        info_to_insert = (password, email, username, link, app_name)
        cursor.execute(query_to_insert, info_to_insert)
        conn.commit()

    except (Exception, psycopg2.Error) as error:
        print(error)



def password_search(app_name):
    try:
        conn = psycopg2.connect(host="localhost", port="5432", database="passwordmanager", user="kartik", password="testPass")
        cursor = conn.cursor()
        query_to_search = """ SELECT password FROM accounts WHERE app_name = '""" + app_name + "'"
        cursor.execute(query_to_search)
        conn.commit()
        requested_password = cursor.fetchone()
        print("The requested password is: " + requested_password[0])

    except (Exception, psycopg2.Error) as error:
        print(error)


def find_email(email):
    info = ('Password: ', 'Email: ','Username: ', 'Link: ','App Name: ')
    try:
        conn = psycopg2.connect(host="localhost", port="5432", database="passwordmanager", user="kartik", password="testPass")
        cursor = conn.connect()
        find_email_query = """ SELECT * FROM accounts WHERE email = '""" + email + "'"
        cursor.execute(find_email_query)
        conn.commit()
        emails_found = cursor.fetchall()
        print('')
        print('List of apps')
        print('')
        for row in emails_found:
            for a in range(0, len(row)-1):
                print(info[i] + row[i])
        print('')
        print('~'*40)
    
    except (Exception, psycopg2.Error) as error:
        print(error)