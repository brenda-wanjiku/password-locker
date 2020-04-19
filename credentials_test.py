import unittest
from credentials import Credentials

class TestCredentials (unittest.TestCase):

    def setUp(self):
        self.new_account = Credentials ("Twitter", "Bre", "bw@38479")
    
    def tearDown(self):
        Credentials.account_info = []

    def test_new_account(self):
        self.new_account.save_account()

if __name__ == '__main__':
    unittest.main()
