#!/usr/bin/env python3.6
from Credential import User,Credential

def create_user(lastname,password):
    '''
    Function to create a new user
    '''
    new_user = User(lastname, password)
    return new_user
def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def authenticate_user(lastname, password):
    '''
    Function to authenticate a user
    '''
    authenticated_user = Credential.confirm_login(lastname, password)
    return authenticated_user
def create_credential(account_name,username,password):
    '''
    Function to create a new credential object
    '''
    new_credential = Credential(account_name,username,password)
    return new_credential
def save_credential(credential):
    '''
    Function to save a created credential
    '''
    Credential.save_credential(credential)
def generate_password():
    '''
    Function to randomly generate password
    '''
    password_generate = Credential.generate_password
    return password_generate
def display_credentials(username):
    '''
    Function to display credentials
    '''
    return Credential.display_credential(username)
def copy_credential(account_name):
    '''
    Function to copy a credential to the clipboard
    '''
    return Credential.copy_credential(account_name)

def main():
   print(' ')
   print('Welcome to Password Locker.')
   while True:
       print(' ')
       print("-"*40)
       print('Use these short codes: A-Create Password-Locker account,  L-Login, X-Exit')
       short_code = input('Enter short code here: ').lower().strip()
       if short_code == 'ex':
           break
       elif short_code == 'A':
           print("-"*40)
           print(' ')
           print('To create a new account:')
           lastname = input('Choose a lastname - ').strip()
           password = input('Choose a password - ').strip()
           save_user(create_user(lastname,password))
           print(" ")
           print(f'Your Password-Locker account lastname is : {lastname}  and password is: {(password)}')

       elif short_code == 'L':
           print("-"*40)
           print(' ')
           print('To login:')
           lastname = input('Enter your Password-Locker username - ').strip()
           password = str(input('Enter your password - '))
           user_authenticated = authenticate_user(lastname,password)
           if user_authenticated == lastname:
               print(" ")
               print(f'Welcome {lastname}. You have successfully logged in. Choose short code to continue')
               print(' ')
               while True:
                   print("-"*40)
                   print('Your credentials short codes: C-Create credential, D-Display Credentials, F-delete credentials account, P-Copy Password, X-Exit')
                   short_code = input('Enter short code: ').lower().strip()
                   print("-"*40)
                   if short_code == 'X':
                       print(" ")
                       print(f'Goodbye {lastname}')
                       break
                   elif short_code == 'C':
                       print(' ')
                       print('Enter your credential account information:')
                       lastname = input('Enter the account name - ').strip()
                       password = input('Enter your username - ').strip()
                       while True:
                           print(' ')
                           print("-"*40)
                           print('Select option for entering a password:  E-Enter your own password, G-Generate a password ,X-Exit')
                           passwrd_select = input('Enter an option: ').lower().strip()
                           print("-"*40)
                           if passwrd_select == 'E':
                               print(" ")
                               password = input('Enter your password: ').strip()
                               break
                           elif passwrd_select == 'G':
                               password = generate_password()
                               break
                           elif passwrd_select == 'X':
                               break
                           
if __name__ == "__main__":
   main