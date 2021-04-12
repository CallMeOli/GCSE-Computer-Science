logins = {
    # 'username': 'password'
    'admin': '1234abc'
}

# Authorise user
username = None # Define username in the global scope so it can be changed both inside and out of a deeper scope
while True:
    # User input
    username = input('Username: ')
    password = input('Password: ')

    # Validation
    if logins[username] == password:
        break
    else:
        print('Your username or password was incorrect. Try again.')

# Executed when logged in
print('Hello, %s. You have successfully logged in.' % (username))