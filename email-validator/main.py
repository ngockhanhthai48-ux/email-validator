from validator import is_valid_email

email = input('Enter email: ')

if is_valid_email(email):
    print('Valid email address')
else:
    print('Invalid email address')
