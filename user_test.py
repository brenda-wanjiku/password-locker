import unittest  
from user import User 


class TestUser( unittest.TestCase):

    def setUp(self):
        self.new_user = User("Brenda", "Wanjiku","wanjiku@gmail.com","@bw21#!&")

    def tearDown(self):
        User.user_list = []

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Brenda")
        self.assertEqual(self.new_user.last_name, "Wanjiku")
        self.assertEqual(self.new_user.email, "wanjiku@gmail.com")
        self.assertEqual(self.new_user.password, "@bw21#!&")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_delete_user(self):
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 0)
     



if __name__ == '__main__':

    unittest.main()
