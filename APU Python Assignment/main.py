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
    clear()

    # First Landing page (Role Selection page)
    print("You are logging in as: ", end='\n')
    print("[1] Administrator")
    print("[2] Customer", end='\n\n')
    print("[X] Exit")
    user_choice = (input("Please select one option (A number): "))

    # User is an Administrator
    if user_choice == '1':
        clear()

        # Administrator Login/Register Option screen
        role = 'administrator'
        print("MAIN MENU")
        print("---------")
        print("[1] Login")
        print("[2] Register", end='\n\n')
        print("[X] Return to previous page")
        admin_input = input("Please select your option: ")

        # Selected Login
        if admin_input == '1':
            if login(role, 'admin_login_credentials'):
                granted_for_access(role)

        # Selected Register
        elif admin_input == '2': 
            register(role, 'admin_login_credentials')
            if login(role, 'admin_login_credentials'):
                granted_for_access(role)

        # Selected Exit Program
        elif admin_input.lower() == 'x': 
            exit()

        # Provided wrong input
        else:
            print('Invalid input. Please try again.')
            admin_input = input("Please select your option: ")

    # User is a Customer
    elif user_choice == '2':
        clear()
        role = 'customer'
        print("MAIN MENU")
        print("---------")
        print("[1] Login")
        print("[2] Register", end='\n\n')
        print("[X] Return to previous page")
        customer_input = input("Please select your option: ")
            
        # Selected Login
        if customer_input == '1':
            if login(role, 'customer_login_credentials'):
                granted_for_access(role)

        # Selected Register
        elif customer_input == '2':
            register(role, 'customer_login_credentials')
            if login(role, 'customer_login_credentials'):
                granted_for_access(role)

        # Selected Exit Program
        elif customer_input.lower() == 'x':
            exit()

        # Provided wrong input
        else:
            print("Invalid Input. Please try again.")
            customer_input = input("Please select your option: ")
    
    # Exit program
    elif user_choice == 'x':
        exit()

    else:
        print("Invalid input. Please try again.")
        user_choice = input("Plesae select your option")

def login(role, selected_file): 

    '''
    Login function

    Arguments:
        file: The respective file to check with, either admin or customer

    Output:
        No output

    Exceptions:
        No exceptions
    '''
    global username
    clear()
    print('LOGIN')
    print('-----')
    print()

    # Accepting input from user
    while True:
        username = input("Please provide your username: ")
        password = getpass("Please provide your password: ")
        
        if username != '' and password != '':
            break
        else:
            print("Username and/or password cannot be blank.")
            continue
    
    user_details = []
    username_password = {}

    # Adding all input from text file to a list
    with open(selected_file, 'r') as fp:
        user_details = [line.strip().split(', ') for line in fp]
    
    # Adding (username: password) key value pairs into a dictionary
    if len(user_details) == 0:
        print("You are not registered yet.")

    for item in user_details:
        username_password[item[0]] = item[2]
    
    while True:
        if username in username_password.keys():         # Checking whether the username given exists or not
            if hash_password(password) == username_password[username]:  # Checking whether the given password matches or not
                return True
                
            else:
                print("Wrong password")
                password = input("Please provide your password: ")
        else:
            print("Wrong username")
            username = input("Please provide your username: ")
            password = getpass("Please provide your password: ")

def register(role, file):
    '''
    Register function

    Arguments:
        file: The location where the user credentials to append into

    Output:
        Writes to the specified file

    Exceptions:
        If "password" and "confirm password" section are different, the user is not able to register. The system will prompt the user once more to re-enter his/her password in both sections. 
    '''
    clear()
    user_details = []

    print("REGISTER")
    print("--------")

    # Registering new username
    while True: 
        username = input("Please provide your username: ")

        if username != '':
            user_details.append(username)
            break
        else:
            print("Username cannot be blank!")
            continue

    # Resgistering new email
    while True: 
        email = input("Please provide your email: ")

        if email != '':
            user_details.append(email)
            break
        else:
            print("Email cannot be blank!")
            continue

    # Registering new password
    while True: 
        password = getpass("Please type in your password: ")

        if password != '' and len(password) >= 10:
            break
        elif password == '':
            print("Password cannot be blank!")
            continue
        elif len(password) < 10:
            print("Password length needs to be more than 10")
        else:
            print("Please provide a password.")

    # Confirming new password
    while True:
        confirmPassword = getpass("Please confirm your password: ")
        
        if confirmPassword == password:
            user_details.append(hash_password(password))
            break
        else:
            print("Password do not match. Please try again.")
            continue
    
    print("\n\n")
    print("Personal Details")
    print("----------------")
    print("Please provide the correct details in the following sections.")
        
    # Registering Customer's full name
    while True:
        full_name = input("Please enter your full name: ").title()

        if full_name != "":
            user_details.append(full_name)
            break
        else:
            print("Name cannot be blank!")
            continue
            
    while True:
        identification = input("Please provide your IC or Passport number: ")
            
        if identification != "":
            user_details.append(identification)
            break
        else:
            print("IC/Passport number cannot be blank!")
            continue

    if userAlreadyExists(full_name, identification, file):
        print("You are already registered. You will now be redirected to login.")
        login(role, file)
        
    else:
        # Registering user's age
        while True:
            age = int(input("Please provide your age: "))

            if age > 0 or age != '':
                user_details.append(age)
                break
            else:
                print("Age cannot be blank or 0")
                continue
        
        # Registering user's contact number
        while True:
            phone = (input("Please provide your contact number: "))

            if phone != '':
                user_details.append(phone)
                break
            else:
                print("Contact number cannot be blank.")
                continue

        # Registeringk user's address
        while True:
            address = input("Please provide your address: ")

            if address != "":
                user_details.append(address)
                break
            else:
                print("Address cannot be blank!")
                continue

        # If role is administrator, record down his given admin ID       
        if role.lower() == "administrator":
            while True:
                admin_id = input("Please provide your give Admin ID: ")

                if admin_id != "":
                    user_details.append(admin_id)
                    break
                else:
                    print("Admin ID cannot be blank.")
                    continue
        
        # Open the respective file and append all the details into it.
        with open(file, 'a') as fp:
            for detail in user_details:
                fp.write(str(detail) + ', ')
            fp.write('\n')

def userAlreadyExists(fullname=None, identification=None, file=None):
    '''
    Function that checks whether the user is registered or not

    Arguments:
        fullname: Checks for the Full Name of the user
        identification: Checks for the IC/Passport Number of the user
        file: Specifies which file to look for the previous arguments

    Output:
        Bool
    '''
    check_for_duplicate = {}
    with open(file, 'r') as fp:
        user_details = [line.strip().split(', ') for line in fp]

    if len(user_details) != 0:
        for item in user_details:
            check_for_duplicate[item[3]] = item[4]

        if fullname in check_for_duplicate.keys():
            if identification == check_for_duplicate[fullname]:
                return True
            else:
                return False
        else:
            return False

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def granted_for_access(role):
    '''
    Grants acccess for the users based on their roles

    Arguments:
        role: Checks whether the user is an Administrator or Customer

    Output:
        Bool
    '''
    if role.lower() == 'administrator':
        print(f"WELCOME, ADMINISTRATOR {username}")
        print("----------------------------------")
        print("Please select what you would like to do:")
        print("[1] Add Cars to be rented out")
        print("[2] Modify Car Details")
        print("[3] Display all records")
        print("[4] Display specific records")
        print("[5] Return Rented Car", end='\n\n')
        print("[X] Return to Login/Register screen")
        option = input("Please select an option [a number]: ")
        admin_access(option)
    
    else:
        print("You are granted access permissions of a customer.")

def admin_access(option):
    pass

def customer_access(option):
    pass

main()
