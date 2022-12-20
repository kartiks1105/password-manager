
from choices import menu, add_password, find_password, find_account


masterPass = 'test'

pword = input('Enter the master password: ')

if pword == masterPass:
    print('Welcome')

else:
    print('Sorry, incorrect master password')
    exit()

select = menu()
while select != '4':
    if select == '1':
        add_password()
    if select == '2':
        find_password()
    if select == '3':
        find_account()
    else:
        select = menu()

exit()
