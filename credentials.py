import random
import string
class Credentials:
    '''
    Class that generates new instance of the account credentials, with the account details to the application
    '''
    account_info = []
    def __init__ (self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

        '''
        __init__ method that helps to define properties for our objects
        '''

    def save_account(self):
        Credentials.account_info.append(self)
        '''
        Method to save new account credentials input by user
        '''
        

    def delete_account(self):
        Credentials.account_info.remove(self)

    @classmethod
    def display_accounts(cls):
        return cls.account_info
        '''
        Method to display accounts
        '''

    @classmethod
    def account_exist(cls, account):
        for account_details in cls.account_info:
            if account_details.account == account:
                return  "Account name:" + account_details.account + "\nUsername: " + account_details.username + "\nPassword: " + account_details.password
        '''
        Method to check if an account exists
        Args:
            account_name: Name of the account which you seek display its credentials
        '''
    @classmethod
    def find_by_account(cls, account):
        for account_details in cls.account_info:
            if account_details.account == account:
                return  "Account name:" + account_details.account + "\nUsername: " + account_details.username + "\nPassword: " + account_details.password

        '''
        Method to display an account's credentials on entering account name
        Args:
            account_name: Name of the account which you seek display its credentials
        '''

    @classmethod
    def delete_by_account(cls, account):
         for account_details in cls.account_info:
             cls.account_info.pop()

         '''
        Method to display an account's credentials on entering account name
        Args:
            account_name: Name of the account which you seek display its credentials
        '''
    @classmethod
    def password_generator(cls,password_length = 8):
        password_chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_chars) for i in range (password_length))
        '''
        Method for generating random passwords with lower-case, upper-case, digits and special characters
        Args:
            password_length: The number of characters in the password to be generated
        '''
   
    
