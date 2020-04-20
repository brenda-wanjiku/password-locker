#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


############## User functions #######################

def create_user(first_name, last_name, email, password):
    new_user = User(first_name,last_name,email,password)
    return new_user

def save_user(user):
    user.save_user()

def name_exists(first_name, last_name):
    return Credentials.name_exists(first_name,last_name)

###########   Credentials functions  #################
def create_account(account,username,email,password):
     new_account = Credentials(account,username,email, password)
     return new_account

def save_account(account_info):
    account_info.save_account()

def delete_account(account):
    Credentials.delete_by_account(account)

def display_accounts():
    return Credentials.account_exist(account)

def find_by_account(account):
    return Credentials.find_by_account(account)



############### Main program #####################
def main ():
    print ("WELCOME TO YOUR PASSWORD MANAGER")
    while True:
        print("Use these short codes: cu - create a new user")

        short_code = input().lower()

        if short_code == "cu":
            print ("New Contact")
            print("-"*10)

            print ("First name.....")
            f_name = input()

            print("Last name .....")
            l_name = input()

            print ("Phone number .....")
            e_address = input()

            save_user(create_user(f_name, l_name, e_address,))
            print('\n')
            print(f"New Contact {f_name}  {l_name} created")
            print('\n')

    break


if __name__ == '__main__':

    main()