#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


############## User functions #######################

def create_user(first_name, last_name, email, password):
    new_user = User(first_name, last_name, email, password)
    return new_user
    '''
    Function to create a new user
    '''


def save_user(user):
    user.save_user()
    '''
    Function to save a new user
    '''


def name_exists(first_name, last_name):
    return Credentials.name_exists(first_name, last_name)
    '''
    Function to check whether a user name exists
    '''

###########   Credentials functions  #################


def create_account(account, username, password):
    new_account = Credentials(account, username, password)
    return new_account
    '''
    Function to create a new account
    '''


def save_account(account_info):
    account_info.save_account()
    '''
    Function to create an account
    '''
    

def delete_account(account):
    return Credentials.delete_by_account(account)
    '''
    Function to delete an account
    '''


def exisiting_account(account):
    return Credentials.account_exist(account)
    '''
    Function to search for an existing account
    '''


def display_accounts():
    return Credentials.display_accounts()
    '''
    Function to display account
    '''



def find_by_account(account):
    return Credentials.find_by_account(account)
    '''
    Function to find account by account name 
    '''


def password_generator(password_length):
    return Credentials.password_generator(password_length)
    '''
        Function that auto generates password
    '''



############### Main program #####################
def main():
    print('\n')
    print("WELCOME TO YOUR PASSWORD MANAGER")
    print('\n')
    print("You HAVE to CREATE an account to use the app")
    while True:
        print("""Use these short codes:
            cn - create a new user 
            lg - log in 
            ex - exit password manager""")
        short_code = input().lower()


        if short_code == "cn":
            print("New Contact")
            print("-"*30)
            print('\n')


            print("First name... ")
            f_name = input()
            print('\n')

            print("Last name... ")
            l_name = input()
            print('\n')

            print("Phone number... ")
            e_address = input()
            print('\n')

            while True:
                print("Password... ")
                password1 = input()
                print('\n')
                print("Confirm password...")
                password2 = input()

                if password1 == password2:
                    password = password1
                    save_user(create_user(f_name, l_name, e_address, password))
                    print('\n')
                    print(
                        f"{f_name}  {l_name} you have successfully signed up for an account. Your password is {password}")
                    print('\n')  
                    print("Kindly LOG IN to explore the app :)")
                    print('\n')
                    break
                          
                else:
                    print('\n')
                    print("INCORRECT PASSWORD. Please try again")

        if short_code == "lg":
                    print('\n')
                    print("First Name")
                    log_f_name = input()   
                    print('\n')
                    print("Last Name")
                    log_l_name = input()
                    print('\n')
                    print("Password") 
                    logpassword = input()

                    if logpassword == password and log_f_name == f_name:
                        print(f"Successful log in {log_f_name}. You may proceed exploring the app.")
                    else:
                        print ("INVALID!! Enter correct details")
                        break



            ######## Account Section #######
                    while True:
                        print("Use these short codes:") 
                        print("""
                        sc - Save exisiting account credentials
                        cn - Create new account credentials
                        da - Display existing accounts, 
                        dc - Display existing credentials
                        del  - Delete existing accounts
                        ex - Exit application
                            """)
                        print('\n')
                        print("Input shortcode: ")
                        short_code = input().lower()


                        if short_code == "sc":
                            print("Save an Existing Account")
                            print("-"*60)
                            print('\n')
                            print("Account name.....")
                            account_name = input()

                            print('\n')
                            print("Username...")
                            user_name = input()

                            print('\n')
                            print("Account Password")
                            account_password = input()
                            save_account(create_account(
                                account_name, user_name, account_password))
                            print('/n')
                            print(
                                f"Thank you {f_name}, your account credentials for {account_name} have been successfully saved")
                            print('/n')




                        elif short_code == "cn":
                            print('\n')
                            print("Create a new account")
                            print("-"*60)

                            print("Account name....")
                            account_name = input()
                            print('\n')

                            print("Username...")
                            user_name = input()
                            print('\n')


                            print("Would you like us to GENERATE A SECURE PASSWORD for you or would you like to USE ONE OF YOUR OWN?")
                            print('\n')
                            print("Use these short codes:")
                            print(""" gen - for us to generate one for you ,  own - if you wish to input your own  
                                  """)
                            choice = input().lower()

                            if choice == 'own':
                                    print('\n')
                                    print("Enter desired password for this account...")
                                    account_password = input()
                                    save_account(create_account(account_name, user_name, account_password))
                                    print(f"Your password is {account_password}")
                                    print ('\n')
                                    print(f"Ok {f_name}, your account credentials for {account_name} have been successfully been saved")
                                    print ('\n')

                            elif choice == 'gen':
                                    print("Enter your desired password length...")
                                    password_length = int(input())
                                    account_password =  password_generator(password_length)
                                    print('\n')
                                    print(f"Your generated password is: {account_password}")
                                    print('\n')
                                    print('\n')
                                    save_account(create_account(account_name, user_name, account_password))
                                    print ('\n')
                                    print(f"Ok {f_name}, your account credentials for {account_name} have been successfully been saved")
                                    print ('\n')

                            else:
                                    print("Oops, that short code does not seem to march any of the prescribed shortcodes, please try again")





                        elif short_code == "da":
                            if display_accounts():
                                print(
                                    "Here is a list of the existing accounts")
                                print('\n')

                                for account in display_accounts():
                                    print('\n')
                                    print(
                                        f" {account.account} ")
                            else:
                                print('\n')
                                print(" You currently have nothing saved")
                                print('\n')



                        elif short_code == "dc":
                            if display_accounts():
                                print(
                                    "Here is a list of the existing accounts")
                                print('\n')

                                for account in display_accounts():
                                    print('\n')
                                    print(
                                        f" {account.account} {account.username} {account.password} ")
                                     print('\n')
                            else:
                                    print('\n')
                                    print("Sorry you have no credentials by that account name")
                                    print('\n')


                        elif short_code == "del":
                            print('\n')
                            print("Enter the name of the account you wish to delete")
                            account_name = input()
                            if exisiting_account(account_name):
                                delete_account(account_name)
                                print('\n')
                                print(
                                    f"{account_name} has succesfully been deleted.")
                                print('\n')
                            else:
                                print('\n')
                                print("The account you entered does not exist")
                                print('\n')
                        
                        elif short_code == "ex":
                            print('\n')
                            print("Thank you for stopping by. Have a good day")
                            break
                        
                        else: 
                            print('\n')
                            print("I didn't get that. Please use correct short codes")


        elif short_code == "ex":
            print("Have a good day...")
            break


        else:
            print("I didn't get that. Please use correct short codes")


if __name__ == '__main__':

    main()
