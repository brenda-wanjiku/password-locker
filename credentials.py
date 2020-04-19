class Credentials:
    account_info = []
    def __init__ (self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

    def save_account(self):
        Credentials.account_info.append(self)
