from stdiomask import getpass
import hashlib
import os
import time

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
            if login('customer_login_credentials'):
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

def sanitize_detail(detail):
    detail = '-'.join(detail.split(", "))
    return detail

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
            user_details.append(sanitize_detail(username))
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

        else:
            amount_paid = 0
            amount_due = 0
            bookings = 0
            purchase_history = []
            rental_duration = 0
            user_details.append(amount_paid)
            user_details.append(amount_due)
            user_details.append(bookings)
            user_details.append(rental_duration)
            user_details.append(purchase_history)
            
        user_details.append(sanitize_detail(address))
        
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
    '''
    Function that determines the admin's access privileges

    Arguments:
        option: (From granted_for_access) Determines what the admin will do

    Output:
        Mostly writing to text files (customer_login_credentials & Car_Records.txt)
    '''
    role = 'administrator'

    # Adding information of new cars into Car_Records.txt
    if option == '1':
        clear()
        print("ADDING INFORMATION OF NEW CARS")
        print("------------------------------")
        # New car information
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
        # Saving all the above information into a list
        car_details = [car_name, car_brand, plate_number, owner, status, duration, short_desc, seats, fuel_type, price]
        
        # Opening Car_Records.txt
        with open("Car_Records.txt", "a") as fp:
            line = ''
            # Writing all the items in the list above into a string, and then writing the line of string to the text file
            for item in car_details:
                line += str(item) + ', '
            fp.write(line)
            fp.write('\n')

        # Returns to the admin's main menu screen
        granted_for_access(role)
    
    # Modifying car details
    elif option == '2':
        # Opening Car_Records.txt and saving all details into a list
        with open("Car_Records.txt", "r") as fp:
            car_list = [line.split(', ') for line in fp] # First item of the list contains all information about the first car, second item contains all information of the second car and so on.
        
        car_number = {}
        # Iterating through all items in the car_list
        for item in car_list: 
            if len(item) != 0:
                # Adding Car_Name: Plate_Number key-value pairs into the dicitionary above
                car_number[item[0]] = item[2]

        clear()
        print("AVAILABLE CARS")
        print("--------------")
        for plate_number in car_number.values():
            print(plate_number)  # Printing out all the cars saved in the text file
        
        # Initializing necessary variables
        searched_car = input("Which car's detail do you wish to modify? ")
        new_list = []
        new_lines = ""

        with open('Car_Records.txt', "r+") as inputfile:
            file = inputfile.read()  # Reading each line in the file

            if(file.find(str(searched_car))) != -1:  # Searches through the file for "searched_car", returns "-1" if false
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

                        unlisted = (", ").join([line])  # Joining all the details into a list named "unlisted"
                        for item in unlisted.split(", "):
                            new_list.append(item)  # Creating a new list for the specific one car [Car_Name, Car_OWner, ...]

                        detail_index = int(input("Please select one of the details that you wish to modify: "))    
                        if detail_index == 5:  # If the modified data is the status of the car, modify the rental duration as well
                            status = input("New status: ")
                            duration = float(input("Rental duration (days): "))
                            # Changing the data inside the list
                            new_list[detail_index-1] = status
                            new_list[detail_index] = str(duration)
                            # Joining the list into a line of string
                            new_lines += ", ".join(new_list) + '\n'
                        else: 
                            # Changing the data inside the list
                            modified_detail = input("New data: ")
                            new_list[detail_index-1] = modified_detail
                            # Joining the list into a line of string
                            new_lines += ", ".join(new_list) + '\n'

                    else:
                        new_lines += line + '\n'

            # Updating the file by writing the new line into it. 
            with open('Car_Records.txt', 'w') as updatedFile:
                updatedFile.writelines(new_lines)

        granted_for_access(role)

    # Display records
    elif option == '3':
        clear()
        print("DISPLAY RECORDS OF:")
        print("[1] Rented cars")
        print("[2] Available cars")
        print("[3] Customer Bookings")
        print("[4] Customer Payments", end='\n\n')
        print("[R] Return to previous screen")
        print("[X] Exit program")
        user_option = input("Please select an option: ")

        # Display records of cars
        if user_option == '1' or user_option == '2':
            clear()
            with open("Car_Records.txt", "r") as fp:
                car_details = [line.split(", ") for line in fp] 
            for item in car_details:
                # Display "Rented" cars
                if user_option == '1' and item[4].lower() == 'rented':
                    print(f"Car: {item[0]}, Plate Number: {item[2]}, Rental Duration: {item[5]}")   
                # Display "Available" cars
                elif user_option == '2' and item[4].lower() == 'available':
                    print(f"Car: {item[0]}, Plate Number: {item[2]}")

        elif user_option == '3' or user_option == '4':
            clear()
            with open("customer_login_credentials", "r") as fp:
                customer_details = [line.split(", ") for line in fp]
            for item in customer_details:
                # Display customer bookings
                if user_option == '3':
                    print(f"{item[3]}'s number of bookings: {item[11]}") # item[3] is the customer name, item[11] is the customer's bookings
                # Display customer payments
                else:
                    # item[3] is the customer name, item[8] is the amount paid, item[9] is the amount due
                    print(f"{item[3]}'s payments: \nAmount Paid -- {item[8]} \nAmount Due -- {item[9]}\n") 

        # Returns to the admin's main menu page
        elif user_option.lower() == 'r':
            granted_for_access(role)

        # Exits the program
        elif user_option.lower() == 'x':
            exit()

        # If user provides wrong input, the system will prompt them to retry
        else:
            print("Invalid option. Please try again.")
            time.sleep(1.5)  # The program waits for a while so that the user can read the print statement above
            admin_access('3')

        # Asks user whether he/she wants to check other records
        user_option = input("\n\nDo you want to return to the previous screen? [y/n] ")
        if user_option[0].lower() == 'y':
            admin_access('3')
        else: 
            granted_for_access(role)

    # Display a specific record
    elif option == '4':
        clear()
        print("CHOOSE WHAT TO SEARCH FOR:")
        print("[1] Customer bookings")
        print("[2] Customer payments", end='\n\n')
        print("[R] Return to previous screen")
        print("[X] Exit")
        user_option = input("Please select one of the options: ")

        # Opening customer_login_credentials that store customer information
        with open("customer_login_credentials", "r") as fp:
            customer_details = [line.split(", ") for line in fp]

        # Initiates a dictionary that will store customer information depending what is selected
        displayed_information = {}
        if user_option == '1':
            clear()
            # Stores customer name (item[3]) and customer bookings (item[10]) into the dictionary above
            for item in customer_details:
                displayed_information[item[3]] = item[10]

            print("CUSTOMER BOOKINGS")
            print("-----------------")
            for name, booking in displayed_information.items():
                print(name + ": " + booking)
        
        elif user_option == '2':
            clear()           
            # Stores customer name (item[3]) and customer payments (item[8]) into the dictionary above
            for item in customer_details:
                displayed_information[item[3]] = item[8]

            print("CUSTOMER PAYMENTS")
            print("-----------------")
            for name, payment in displayed_information.items():
                print(name + ": " + payment)
        
        # Returns to the admin's main menu page
        elif user_option.lower() == 'r':
            granted_for_access(role)

        # Exits the program
        elif user_option.lower() == 'x':
            exit()

        # Prompts the user to try again if he/she provides invalid input
        else:
            clear()
            print("Invalid option. Please try again")
            time.sleep(1.5) # Allow the system to wait for a while before the prompt, so that the user can read the print statement above this line
            admin_access('4')

        user_option = input("\n\nDo you want to return to the previous screen? [y/n] ")
        if user_option[0].lower() == 'y':
            admin_access('4')
        else: 
            granted_for_access(role)

    # Returning a rented car
    elif option == '5':
        # Opening Car_Records.txt and saving all details into a list
        with open("Car_Records.txt", "r") as fp:
            car_list = [line.split(', ') for line in fp] # The list where all the details are saved
        
        car_number = {}
        for item in car_list: 
            if len(item) != 0 and item[4].lower() == 'rented':
                car_number[item[0]] = item[2] # Saves the details needed into a dictionary

        clear()
        print("RENTED CARS")
        print("--------------")
        for plate_number in car_number.values():
            print(plate_number)  # Prints out the plate number of "Rented" cars only
        print()

        # Initializes the necessary variables
        returned_car = input("Please provide the plate number of the returned car: ")
        new_list = []
        new_lines = ""

        with open('Car_Records.txt', "r+") as inputfile:
            file = inputfile.read()

            if(file.find(str(returned_car))) != -1:
                for line in file.splitlines():
                    if (line.find(str(returned_car))) != -1: # Checks for the returned car's plate number
                        unlisted = (", ").join([line])
                        for item in unlisted.split(", "):
                            new_list.append(item)    
                        if new_list[4].lower() == 'rented':  # Checking whether is it really rented
                            new_list[4] = 'Available'  # Changes the status from "Rented" to "Available"
                            new_list[5] = '0'          # Changes the rental duration to 0
                            new_lines += ", ".join(new_list) + '\n'  # Joins everything into a string
                        else:
                            print("Car is already available")
                    else:
                        new_lines += line + '\n'

            with open('Car_Records.txt', 'w') as updatedFile:
                updatedFile.writelines(new_lines)

        # Ask the user whether he/she wants to return more cars
        user_option = input("\n\nDo you want to return to the previous screen? [y/n] ")
        if user_option[0].lower() == 'y':
            admin_access('4')
        else: 
            granted_for_access(role)
        
    # Returns to the Login/Register screen
    elif option.lower() == 'r':
        main()
    
    # Exits the program
    elif option.lower() == 'x':
        exit()

    # Prompts the user for input again if invalid input is given
    else:
        print("Invalid input. Please try again.")
        granted_for_access(role)

def customer_access(option):
    pass

main()