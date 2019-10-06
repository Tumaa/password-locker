import random 
import string

class User:
    '''
    class that will generate new instances of users.
    '''
    user_list = []
    def __init__(self,lastname ,password):
        
        '''
        init method that gives the blueprint of the object instantiated
        '''
        self.lastname = lastname
        self.password = password
        
    def save_user (self):
        '''
        amethod  to save uset object to user_list
        '''
        User.user_list.append(self)
        
class Credential:
    '''
    class that defines the credential behaviours
    '''
    Credential_list = []
    user_credential_list = []
    
    @classmethod
    def confirm_login (cls,lastname, password):
        '''
        method for login the user
        '''
        for user in User.user_list:
            if user.lastname == lastname and user.password == password:
                current_user =user.lastname
        return current_user
    def __init__(self, account_name, username, password):
        '''
        method to define the properties for user object
        '''
        self.account_name = account_name
        self.username = username
        self. password = password
        
    def save_credential (self):
        '''
        amethod  to save uset object to user_list
        '''
        Credential.Credential_list.append(self)
        
    @classmethod
    def display_credential(cls, username):
        '''
        function to diplay saved account
        '''
        user_credential_list = []
        for  credential in cls.Credential_list:
            if credential.username == username:
                user_credential_list.append(credential)
        return user_credential_list   
        
        
    def generate_password (self,size=5, char=string.ascii_lowercase+string.ascii_uppercase+string.digits):
            '''
            function to generate random password
            
            '''
            password_generate = "".join(random.choice(char) for _ in range(size))
            return password_generate