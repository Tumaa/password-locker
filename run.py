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

