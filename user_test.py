import unittest  
from user import User 


class TestUser( unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        self.new_user = User("Brenda", "Wanjiku","wanjiku@gmail.com","@bw21#!&")
        
        '''
        Setup method to run before each test cases.
        '''

    def tearDown(self):
        User.user_list = []
        
        '''
        tearDown method that does clean up after each test case has run
        '''

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Brenda")
        self.assertEqual(self.new_user.last_name, "Wanjiku")
        self.assertEqual(self.new_user.email, "wanjiku@gmail.com")
        self.assertEqual(self.new_user.password, "@bw21#!&")

        '''
        Test to check if the object is initialized properly
        '''


    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

        '''
        Test to check if new user can be saved
        '''

    def test_delete_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 0)

        '''
        Test to check if a user can be deleted
        '''

    def test_user_password(self):
        self.new_user.save_user()
        password_entered = User.password_correct("@bw21#!&")
        self.assertTrue(password_entered)

        '''
        Test to determine whether input password is correct
        '''
     
    def test_user_exist(self):
        self.new_user.save_user()
        name_entered = User.name_exists("Brenda", "Wanjiku")
        self.assertIs(name_entered,True)

        '''
        Test to confirm whether if user exists false will be returned
        '''



if __name__ == '__main__':

    unittest.main()
