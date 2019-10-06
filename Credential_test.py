import unittest
from Credential import User, Credential




class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        this is setup method to run before each testcase
        '''
        self.new_user = User("tumaa", "1234ali")
        
    def tearDown(self):
        User.user_list = []
        
    def test__init__(self):
        '''
        method to test if object is well initialized 
        '''
        self.assertEqual(self.new_user.lastname,"tumaa")
        self.assertEqual(self.new_user.password,"1234ali")
    
    def test_save_user(self):
        '''
        method to test if the user object is saved into the user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
class TestCredential(unittest.TestCase):
        '''
        test class to test credential object
        '''
    
def test_confirm_login(self):
        '''
        Method to test login functionality.
        '''
        self.new_user = User('tumaa','1234ali')
        self.new_user.save_user()
        user2 = User('fatuma', '1234ali')
        user2.save_user()
        for user in User.user_list:
            if user.lastname == user2.lastname and user.password == user2.password:
                current_user = user.lastname
        return current_user
        self.assertEqual(current_user, Credential.confirm_login(user2.password, user2.lastname))
        
def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credential('facebook','tumaa','1234ali')
        
          
def test__init__(self):
        '''
        test__init__ test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name,'facebook')
        self.assertEqual(self.new_credential.username,'tumaa')
        self.assertEqual(self.new_credential.password,'1234ali')
def test_save_credentials(self):
        '''
        Test to confirm if the new credential is saved to the credentials list
        '''
        self.new_credential.save_credential()
        instagram = Credential('Instagram','tumaa','12345ali')
        instagram.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []
        User.user_list = []
        
        
if __name__ == "__main__":
    unittest.main()
    
        