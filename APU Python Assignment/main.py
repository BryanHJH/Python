from stdiomask import getpass
import hashlib
import os
import datetime

clear = lambda: os.system('cls')

def main():
    '''
    The main program

    Arguments:
        Does not contain any arguments

    Output:
        The user can select their role, then login/register and carry out the available task
    '''

    # First Landing page (Role Selection page)
    print("You are logging in as: ", end='\n')
    print("[1] Administrator")
    print("[2] Customer", end='\n\n')
    customer_choice = int(input("Please select one option (A number): "))

    if customer_choice == 1:
        file = open('admin_login_credentials', 'r')
        login('administrator', file)  # Logging in as an administrator

    else:
        file = open('customer_login_credentials', 'r')
        login('customer', file)  # Logging in as a customer
    
    pass

def validate_user(username, password, file):
    '''
    Validates the information input from Login()

    Arguments:
        username: str, the user's username for logging in
        password: str, the user's password for logging in, needs to be decrypted/insert encrypted version of password

    Output:
        Bool

    Exceptions:
        Raises excpetion if "username" and "password" from user does not match the credentials in text file, it would raise an exception where the user is not able to login. 
    '''
    pass

def login(role, file):
    '''
    Login function

    Arguments:
        file: The respective file to check with, either admin or customer

    Output:
        No output

    Exceptions:
        No exceptions
    '''
    pass

def register(file):
    '''
    Register function

    Arguments:
        file: The location where the user credentials to append into

    Output:
        Writes to the specified file

    Exceptions:
        If "password" and "confirm password" section are different, the user is not able to register. The system will prompt the user once more to re-enter his/her password in both sections. 
    '''
    pass

main()