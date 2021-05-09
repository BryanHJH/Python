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
        print("[R] Return to previous page")
        admin_input = input("Please select your option: ")

        # Selected Login
        if admin_input == '1':
            if login('admin_login_credentials'):
                granted_for_access(role)

        # Selected Register
        elif admin_input == '2': 
            register(role, 'admin_login_credentials')
            if result:
                granted_for_access(role)

        # Selected Exit Program
        elif admin_input.lower() == 'r': 
            main()

        # Provided wrong input
        else:
            print('Invalid input. Please try again.')
            main()

    # User is a Customer
    elif user_choice == '2':
        clear()
        role = 'customer'
        print("MAIN MENU")
        print("---------")
        print("[1] Login")
        print("[2] Register")
        print("[3] Skip", end='\n\n')
        print("[R] Return to previous page")
        customer_input = input("Please select your option: ")
            
        # Selected Login
        if customer_input == '1':
            if login('customer_login_credentials'):
                status = 'registered'
                granted_for_access(role, status)

        # Selected Register
        elif customer_input == '2':
            register(role, 'customer_login_credentials')
            if result:
                status = 'registered'
                granted_for_access(role, status)

        elif customer_input == '3':
            status = 'unregistered'
            granted_for_access(role, status)

        # Selected Exit Program
        elif customer_input.lower() == 'r':
            main()

        # Provided wrong input
        else:
            print("Invalid Input. Please try again.")
            main()
    
    # Exit program
    elif user_choice == 'x':
        exit()

    else:
        print("Invalid input. Please try again.")
        main()

def login(selected_file): 

    '''
    Login function

    Arguments:
        file: The respective file to check with, either admin or customer

    Output:
        LOGIN SUCCESSFUL: Returns a Boolean (TRUE)
        LOGIN FAILURE: Prints out a statement informing the user of the failure and restarting the process

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
    
    # Checking credentials
    while True:
        if username in username_password.keys():         # Checking whether the username given exists or not
            if hash_password(password) == username_password[username]:  # Checking whether the given password matches or not
                return True
                
            else:  # Return values for LOGIN FAILURE
                print("Wrong password")
                password = getpass("Please provide your password: ")
        else:  # Return values for LOGIN FAILURE
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
    global result
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
    
    # Checking whether user already exists
    if userAlreadyExists(full_name, identification, file):
        print("You are already registered. You will now be redirected to login.")
        result = login(file)
        
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

        # Registering user's address
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

def granted_for_access(role, status=None):
    '''
    Grants acccess for the users based on their roles

    Arguments:
        role: Checks whether the user is an Administrator or Customer

    Output:
        None
    '''
    clear()
    if role.lower() == 'administrator':
        print(f"WELCOME, ADMINISTRATOR {username}")
        print("----------------------------------")
        print("Please select what you would like to do:")
        print("[1] Add Cars to be rented out")
        print("[2] Modify Car Details")
        print("[3] Display all records")
        print("[4] Display specific records")
        print("[5] Return Rented Car", end='\n\n')
        print("[R] Return to Login/Register screen")
        print("[X] Exit program")
        option = input("Please select an option [a number]: ")
        admin_access(option)
    
    else:
        if status == 'registered':
            print(f"WELCOME, {username}!")
            print("--------------------")
            print("Please select what you would like to do:")
            print("[1] View catalog")
            print("[2] Modify personal details")
            print("[3] View personal details")
            print("[4] View car details")
            print("[5] Rent a car", end='\n\n')
            print("[R] Return to Login/Register screen")
            print("[X] Exit program")
            option = input("Please select an option: ")
            customer_access(option)

        else:
            print("WELCOME, CUSTOMER!")
            print("------------------")
            print("Please select what you would like to do:")
            print("[1] View catalog")
            print("[2] Register", end='\n\n')
            print("[R] Return to Login screen")
            print("[X] Exit program")
            option = input("Please select what you would like to do:")
            customer_access(option)

def admin_access(option):
    if option == '1':
        clear()
        print("ADDING INFORMATION OF NEW CARS")
        print("------------------------------")
        car_name = input("Car Name\nPlease provide the name of the car: ")
        car_brand = input("\nCar Model\nPlease provide the model of the car: ")
        plate_number = input("\nPlate Number\nPlease provide the plate number of the car: ")
        owner =  input("\nOwner\nPlease provide the name of the car's owner: ")
        status = 'available'
        duration = 0
        seats = int(input("\nSeats\nHow many seats are there in the car (provide a number): "))
        fuel_type = input("\nFuel\nWhat type of fuel does the car use: ")
        short_desc = input("\nDescription\nPlease provide a short description for the vehicle: ")
        rental_rate = int(input("\nRental\nPlease provide rental rate of the car: "))
        price = "RM" + str(rental_rate)
        car_details = [car_name, car_brand, plate_number, owner, status, duration, short_desc, seats, fuel_type, price]
        
        with open("Car_Records.txt", "a") as fp:
            line = ''
            for item in car_details:
                line += str(item) + ', '
            fp.write(line)
    
    elif option == '2':
        searched_car = input("Which car's detail do you wish to modify? ")
        new_list = []
        with open('Car_Records.txt', "r+") as inputfile:
            file = inputfile.read()

            if(file.find(str(searched_car))) != -1:
                for line in file.splitlines():
                    if (line.find(str(searched_car))) != -1: # After this line, ask user what to change
                        print("Which detail do you wish to modify?")
                        print("[1] Car Name")
                        print("[2] Car Model")
                        print("[3] Plate Number")
                        print("[4] Car's Owner")
                        print("[5] Status")
                        print("[6] Duration")
                        print("[7] Short Description")
                        print("[8] Seats")
                        print("[9] Fuel Type")
                        print("[10] Rental rates")
                        detail_index = int(input("Please select one of the details that you wish to modify: "))
                        modified_detail = input("New data: ")
                        unlisted = (", ").join([line])
                        for item in unlisted.split(", "):
                            new_list.append(item)
                        new_list[detail_index-1] = modified_detail
                        print(new_list)
            #         else:
            #             new_lines += line + '\n'

            # with open('text.txt', 'w') as updatedFile:
            #     updatedFile.writelines(new_lines)

    elif option.lower() == 'r':
        main()
    
    elif option.lower() == 'x':
        exit()

def customer_access(option):
    pass

main()
