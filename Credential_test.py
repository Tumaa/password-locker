import unittest
from Credential import User


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
        
        
        
        
if __name__ == "__main__":
    unittest.main()
    
        