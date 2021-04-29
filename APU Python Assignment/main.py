from stdiomask import getpass
import hashlib
import os
import datetime

clear = lambda: os.system('cls')

def main():
    '''
    The main program

    Arguments:
        Does not contain any functions

    Output:
        The user can select their role, then login/register and carry out the available task
    '''


    
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

def login():
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