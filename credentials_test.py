import unittest
from credentials import Credentials

class TestCredentials (unittest.TestCase):

    def setUp(self):
        self.new_account = Credentials ("Twitter", "Bre", "bw@38479")

    def tearDown(self):
        Credentials.account_info = []
    
    def test_init(self):
        self.assertEqual(self.new_account.account, "Twitter")
        self.assertEqual(self.new_account.username, "Bre")
        self.assertEqual(self.new_account.password, "bw@38479")

    def test_new_account(self):
        self.new_account.save_account()

    def test_multiple_accounts(self):
        self.new_account.save_account()
        test_account = Credentials ("Facebook", "test", "test@gmail.com")
        test_account.save_account()
        self.assertEqual(len(Credentials.account_info), 2)


    def test_delete_account(self):
        self.new_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.account_info), 0)

    def test_display_accounts(self):
      self.assertEqual(Credentials.display_accounts(), Credentials.account_info)

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

if __name__ == '__main__':
    unittest.main()
