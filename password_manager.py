#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


############## User functions #######################

def create_user(first_name, last_name, email, password):
    new_user = User(first_name, last_name, email, password)
    return new_user


def save_user(user):
    user.save_user()


def name_exists(first_name, last_name):
    return Credentials.name_exists(first_name, last_name)

###########   Credentials functions  #################


def create_account(account, username, password):
    new_account = Credentials(account, username, password)
    return new_account


def save_account(account_info):
    account_info.save_account()


def delete_account(account):
   return Credentials.delete_by_account(account)

def exisiting_account(account):
    return Credentials.account_exist(account)


def display_accounts():
    return Credentials.display_accounts()



def find_by_account(account):
    return Credentials.find_by_account(account)


############### Main program #####################
def main():

    print("WELCOME TO YOUR PASSWORD MANAGER")
    while True:
        print("Use these short codes: cu - create a new user")

        short_code = input().lower()

        if short_code == "cu":
            print("New Contact")
            print("-"*10)

            print("First name.....")
            f_name = input()

            print("Last name .....")
            l_name = input()

            print("Phone number .....")
            e_address = input()

            while True:
                print("Password...")
                password1 = input()

                print("Confirm password ...")
                password2 = input()

                if password1 == password2:
                    password = password1
                    save_user(create_user(f_name, l_name, e_address, password))
                    print('\n')
                    print(
                        f"{f_name}  {l_name} you have successfully signed up for an account")
                    print('\n')


######## Account Section #######
                while True:
                    print(
                        "Use these short codes: sc - Save exisiting account credentials, ca - Create new account credentials, da - Display existing accounts")
                    print("Input shortcode: ")
                    short_code = input().lower()
                    if short_code == "sc":
                        print("Save an Existing Account")
                        print("-"*10)

                        print("Account name.....")
                        account_name = input()

                        print("Account Username...")
                        user_name = input()

                        print("Account Password")
                        account_password = input()
                        save_account(create_account(
                            account_name, user_name, account_password))
                        print('/n')
                        print(
                            f"Thank you {f_name}, your account credentials for {account_name} have been successfully saved")
                        print('/n')

                    elif short_code == "ca":
                        print("Create a new account")
                        print("-"*10)

                        print("Account name....")
                        account_name = input()

                        print("Account Username...")
                        user_name = input()

                        print("Account Password")
                        account_password = input()
                        save_account(create_account(account_name, user_name, account_password))
                        print('/')
                        print(f"{f_name}. {account_name} has been successfully saved")
                    
                    elif short_code == "da":
                        if display_accounts():
                            print ("Here is a list of the existing accounts")
                            print('\n')

                            for account in display_accounts():
                                print(f" {account.account}  {account.username} {account.password} ")
                        else: 
                            print(" You currently have nothing saved")
                    

            


                    elif short_code == "del":
                        print ("Enter the name of the account you wish to delete")
                        account_name = input()
                        if account_exist(account_name):
                            delete_account(account_name)
                            print (f"{account_name} has succesfully been deleted.")
                        else:
                            print("The account you entered does not exist")














if __name__ == '__main__':

    main()
