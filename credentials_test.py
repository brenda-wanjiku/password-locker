import unittest
from credentials import Credentials

class TestCredentials (unittest.TestCase):
      '''
    Test class that defines test cases for the Credentials class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
      '''

    def setUp(self):
        self.new_account = Credentials ("Twitter", "Bre", "bw@38479")

        '''
        Setup method to run before each test cases.
        '''

    def tearDown(self):
        Credentials.account_info = []
        '''
        TearDown method that does clean up after each test case has run.
        '''

    
    def test_init(self):
        self.assertEqual(self.new_account.account, "Twitter")
        self.assertEqual(self.new_account.username, "Bre")
        self.assertEqual(self.new_account.password, "bw@38479")

        '''
        Test to check if the object is initialized properly
        '''

    def test_new_account(self):
        self.new_account.save_account()
        '''
        Test to determine if account credentials can be saved
        '''
        

    def test_multiple_accounts(self):
        self.new_account.save_account()
        test_account = Credentials ("Facebook", "test", "test@gmail.com")
        test_account.save_account()
        self.assertEqual(len(Credentials.account_info), 2)
        '''
        Test to determine if user can add credentials for multiple accounts
        '''


    def test_delete_account(self):
        self.new_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.account_info), 0)
        '''
        Test_delete_credentials to test if we can remove a credentials from our credentials list
        '''

    def test_display_accounts(self):
      self.assertEqual(Credentials.display_accounts(), Credentials.account_info)
        '''
        Test to see if all accounts can display
        '''

    def test_account_exists(self):
      self.new_account.save_account() 
      test_account = Credentials ("Facebook", "test", "test@gmail.com")
      test_account.save_account()
      account_exists = Credentials.account_exist("Twitter")
      self.assertTrue(account_exists)

    def test_find_by_account(self):
      self.new_account.save_account() 
      find_account = Credentials.find_by_account("Twitter")
      self.assertTrue(find_account, self.new_account.account)


    def test_delete_account(self):
      self.new_account.save_account() 
      test_account = Credentials ("Facebook", "test", "test@gmail.com")
      test_account.save_account()
      account_exists = Credentials.account_exist("Twitter")
      Credentials.delete_by_account("Twitter")
      self.assertEqual(len(Credentials.account_info), 1)
        '''
        Test_delete_credentials to test if we can remove a credentials from our credentials list
        '''

if __name__ == '__main__':
    unittest.main()
