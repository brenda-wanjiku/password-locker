class Credentials:
    account_info = []
    def __init__ (self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

    def save_account(self):
        Credentials.account_info.append(self)


    def delete_account(self):
        Credentials.account_info.remove(self)

    @classmethod
    def display_accounts(cls):
        return cls.account_info

    @classmethod
    def account_exist(cls, account):
        for account_details in cls.account_info:
            if account_details.account == account:
                return True
            return False

    
