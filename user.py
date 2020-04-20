class User : 
    '''
    Class that generates new instance of the user, with their login informations to the application
    
    '''
    user_list = [] 
    def __init__(self, first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

        '''
        __init__ method that helps to define properties for our objects
        '''

    def save_user(self): 
        User.user_list.append(self)

        '''
        Method to save user to the application
        '''


    def delete_user(self):
        User.user_list.remove(self)
        '''
        Method to delete user from the application
        '''

    @classmethod
    def password_correct(cls, password):
        for user in cls.user_list:
            return (user.password == password)
        ''' 
        Method to confirm whether password entered is correct
        '''
              

    @classmethod
    def name_exists(cls, first_name, last_name):
        for user in cls.user_list:
            return (user.first_name == first_name and user.last_name == last_name)
        ''' 
        Method to confirm whether username entered exists 
        '''


    