################################################################################################
# Python authorisation

# Write a program that asks the user for a username and password. (7 marks) 
# ->    The program keeps asking for the username and password until the correct username and
#       password have been entered.   
# ->    The username should be admin and the password 1234abc.  
# ->    Once you have logged in (i.e. entered the correct username and password), the program 
#       should respond with a message like (“Hello, <username>. You have successfully logged in”) 
################################################################################################
## Made by Oliver Parry
##
## 14/04/2021
################################################################################################

logins = {
    # 'username': 'password'
    'admin': '1234abc'
}

# Authorise user
username = None # Define username in the global scope so it can be changed both inside and out of a deeper scope
# Repeat authorisation loop until broken
while True:
    # User input
    username = input('Username: ')
    password = input('Password: ')

    # Validation
    if username in logins and logins[username] == password:
        # Break the authorisation loop once the correct credentials have been provided
        break
    else:
        print('Your username or password was incorrect. Try again.')

# Executed when logged in
print('Hello, %s. You have successfully logged in.' % (username))