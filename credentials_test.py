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

    def test_multiple_account(self):
        self.new_account.save_account()
        test_account = Credentials ("Facebook", "test", "test@gmail.com")
        test_account.save_account()
        self.assertEqual(len(Credentials.account_info), 2)


    def test_delete_account(self):
        self.new_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Credentials.account_info), 0)



if __name__ == '__main__':
    unittest.main()
