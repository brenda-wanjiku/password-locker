class User : 
    user_list = [] 
    def __init__(self, first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_user(self): 
        User.user_list.append(self)


    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def password_correct(cls, password):
        for user in cls.user_list:
            return user.password == password
              



    