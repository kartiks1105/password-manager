from password_hasher import password
from connection import storing, password_search, find_email
import subprocess

def menu():
    print('~'*40)
    print(('~'*20)+'Menu'+('~'*20))
    print('1. Add a new password')
    print('2. Find a password')
    print('3. Find an account')
    print('4. Exit')
    print('~'*40)
    return input(': ')


def add_password():
    print('What app/website do you want to add a password for? ')
    app_name = input()
    print('Provide a password: ')
    plaintext = input()
    pword = password(plaintext, app_name, 12)
    #subprocess.run('xclip', universal_newlines = True, input = pword)
    print('~'*40)
    print('')
    print('New password has been created')
    print('')
    print('~'*40)
    email = input('Provide your email: ')
    username = input('Provide your username: ')
    if username == None:
        username = ''
    link = input('Please paste the link: ')
    storing(pword, email, username, link, app_name)


def find_password():
    print('Provide the name of the app for which you want the password: ')
    app_name = input()
    password_search(app_name)


def find_account():
    print('Provide the email for which you want to find accounts: ')
    email = input()
    find_email(email)