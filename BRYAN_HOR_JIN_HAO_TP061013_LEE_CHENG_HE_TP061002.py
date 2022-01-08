#BRYAN HOR JIN HAO
#TP061013
#LEE CHENG HE
#TP061002
from stdiomask import getpass
import hashlib
import os
import datetime

def clear():
    '''
    A function that runs os.system('cls')

    Parameters:
        None

    Output:
        None
    '''
    return os.system("cls")

# Formatting details before saving to the text files
def sanitize_detail(detail):
    '''
    A function that joins a line of string into a single string

    Argument:
        detail -- the string to join

    Output:
        A string that is separated by "-". E.g. "Bryan-Hor-Jin-Hao" instead of "Bryan Hor Jin Hao"
    '''
    detail = "-".join(detail.split(", "))
    return detail

# Encrypting passwords
def hash_password(password):
    '''
    A function the encrypts the password

    Arguments:
        password -- the user's password

    Output:
        An encrypted line
    '''
    return hashlib.sha256(str.encode(password)).hexdigest()

# Converting information in files to list
def search_file(file, searched_term):
    '''
    A function that searches a file for a specific term

    Arguments:
        file -- which file to search
        searched_term -- which term to search

    Output:
        Returns a list containing the line of the searched term
    '''
    try:
        with open(file, 'r+') as fp:
            for line in fp:
                if line.startswith(searched_term):
                    ls = line.split(", ")
        
        return ls

    except:
        return []

# Writing to files
def write_to_file(file, details):
    '''
    A function that writes lines into a specified text file

    Parameters:
        file - the destination file
        details - the details that will be written into the destination file

    Output: 
        None
    '''
    with open(file, "a") as fp:
        for detail in details:
            fp.write(str(detail) + ", ")
        fp.write("\n")

# Checking for the file for duplicate values
def check_for_duplicate(file, username):
    '''
    A function that searches for duplicate entries in a file

    Arguments:
        file -- the file to search through
        username -- the username to search for

    Output:
        If the username exists, a list named "duplicate" will be created. Therefore, if the len(duplicate) is 0, there was no existing record.
    '''
    duplicate = search_file(file, username)

    return duplicate == []

# Payment
def payment(method, amount):
    '''
    A function that detects the selected payment method and determines the next steps

    Parameters:
        method - the payment method (either via PayPal or credit/debit card)
        amount - the payment amount

    Output:
        A message indicating the amount paid through the method selected
    '''
    if method.lower() == "credit card":
        credit_card_number = input("Please provide your credit card mumber: ")
        credit_card_name = input("Please proovide the card user name: ")
        cvv = input("Please provide the CVV number on the card: ")
        expiry = input("Please provide the expiry date of your card: ")

        while True: 
            if (credit_card_name and credit_card_number and cvv and expiry) != '':
                break

            print("Please provide all required details.")
            credit_card_number = input("Please provide your credi card mumber: ")
            credit_card_name = input("Please proovide the card user name: ")
            cvv = input("Please provide the CVV number on the card: ")
            expiry = input("Please provide the expiry date of your card: ")

        print(f"RM{amount} was successfully charged to your credit car at Super Car Rental. Please call the number at the back of your card for any enquiry.")

    else:
        print("Please login to your Paypal account.")
        paypal_email = input("Email: ")
        paypal_password = getpass("Password: ")

        while True: 
            if (paypal_email and paypal_password) != '':
                break

            print("Please provide all required details.")
            paypal_email = input("Email: ")
            paypal_password = getpass("Password: ")

        print(f"RM{amount} was successfully charged to your paypal account at Super Car Rental. Please contact Paypal customer support for any enquiry.")

# First landing page: Role selection menu
def role_selection():
    '''
    Role selection function

    Arguments: 
        None

    Output:
        Role: which role that the user has selected (adminstrator/customer)
    '''
    clear()
    
    print("You are logging in as: ")
    print("[1] Administrator")
    print("[2] Customer", end="\n\n")
    print("[X] Exit")
    user_input = input("Please select an option: ")

    if user_input == "1":
        return "administrator"

    elif user_input == "2":
        return "customer"

    else:
        return "x"

# Second landing page: Login/Registration
def login_register_menu(role):
    '''
    Login/Register screen function

    Arguments:
        role -- Accepts a string and checks whether is it "adminstrator" or "customer"

    Output:
        1 for login, 2 for register, 3 for skip, r to return
    '''
    clear()

    if role.lower() == "administrator":
        print("MAIN MENU")
        print("---------")
        print("[1] Login")
        print("[2] Register", end="\n\n")
    else:
        print("MAIN MENU")
        print("---------")
        print("[1] Login")
        print("[2] Register")
        print("[3] Skip")

    print("[R] Return to previous page")
    return input("Please select an option: ")

# Third landing page - 1: Login
def login(role):
    '''
    Login function

    Arguments:
        role -- check which role the user belongs to

    Output:
        Boolean -- True if successful login or otherwise
        username -- the user's username for further usage
    '''
    clear()
    print("LOGIN")
    print("-----")
    username = input("Please provide your username: ")
    password = getpass("Please provide your password: ")

    while True:
        if (username and password) != "":
            break

        print("Username and/or password cannot be blank!")
        username = input("Please provide your username: ")
        password = getpass("Please provide your password: ")

    if role.lower() == 'administrator':
        login_pair = search_file("admin2.txt", username)
        status = None
        if len(login_pair) != 0 and login_pair[1] == hash_password(password):
            return True, username, status

        else:
            return False, username, status
    else:
        login_pair = search_file("customer2.txt", username)
        if len(login_pair) == 0 or login_pair[1] != hash_password(password):
            return False, username, "Unregistered"

        status = "Registered"
        return True, username, status

# Third landing page - 2: Register
def register(role):
    '''
    Register function

    Arguments:
        role -- checks which role the user is and writes to the correct file

    Outputs:
        Writes to either admin2.txt or customer2.txt
    '''
    clear()

    print("REGISTER")
    print("--------")

    # Getting the username and password
    while True: 
        username = input("Please provide your username: ")

        if username != "":
            break

        print("Username cannot be blank.")
        username = input("Please provide your username: ")

    while True: 
        password = getpass("Please provide your password: ")

        if password != "": 
            password = hash_password(password)
            break

        else:
            print("Password cannot be blank.")
            password = getpass("Please provide your password: ")


    # Checking for duplicate entries
    if role.lower() == "administrator":
        repeated = check_for_duplicate("admin2.txt", username)

    else:
        repeated = check_for_duplicate("customer2.txt", username)

    # Registering, meaning the user didn't exist before
    if repeated:
        while True:
            confirm_password = getpass("Please confirm your password: ")

            if hash_password(confirm_password) == password:
                break

            print("Passwords do not match. Please try again.")
            continue

        while True: 
            full_name = input("Please provide your full name: ")

            if full_name != "":
                break

            print("Full name cannot be blank.")
            continue

        while True: 
            identification = input("Please provide your IC/Passport number: ")

            if identification != "":
                break

            print("IC/Passport Number cannot be blank.")
            continue

        while True: 
            age = input("Please provide your age: ")

            if age != "" and int(age) > 18:
                break

            print("Age cannot be blank or your age must be more than 18.")
            continue

        while True: 
            phone = input("Please provide your contact number: ")

            if phone != "":
                break

            print("Contact number cannot be blank.")
            continue

        while True: 
            address = input("Please provide your address: ")

            if address != "":
                address = sanitize_detail(address)
                break

            else:
                print("Address cannot be blank.")
                continue

        if role.lower() == "administrator":
            while True: 
                admin_id = input("Please provide your Administrator ID: ")

                if admin_id != "":
                    break

                print("Administrator ID cannot be blank.")
                continue

            full_details = [username, password, full_name, identification, age, phone, address, admin_id]

            write_to_file("admin2.txt", full_details)

        else:
            amount_paid = ""
            amount_due = ""
            purchase_history = ""

            full_details = [username, password, full_name, identification, age, phone, address, amount_paid, amount_due, purchase_history]

            write_to_file("customer2.txt", full_details)

        print("You'll be redirected to login now.")

    else:
        print("You've registered previously. You will now be redirected to login.")

# Fourth landing page: Main user options
def granted_for_access(role, username, status="Unregistered"):
    '''
    A function that shows what the user can do after logging in

    Arguments:
        role -- either "Administrator" or "Customer"
        username -- to greet the user
        status -- (For customers only) depending on status, the user can do different things
    '''
    
    clear()
    if role.lower() == "administrator":
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
        return input("Please select an option [a number]: ")

    elif status.lower() == "registered":
        print(f"WELCOME, {username}!")
        print("--------------------")
        print("Please select what you would like to do:")
        print("[1] View catalog")
        print("[2] Modify personal details")
        print("[3] View purchase history")
        print("[4] View car details")
        print("[5] Rent a car", end='\n\n')
        print("[R] Return to Login/Register screen")
        print("[X] Exit program")
        return input("Please select an option: ")

    else:
        print(f"WELCOME, {username}!")
        print("------------------")
        print("Please select what you would like to do:")
        print("[1] View catalog")
        print("[2] Register", end='\n\n')
        print("[R] Return to Login screen")
        print("[X] Exit program")
        return input("Please select what you would like to do:")

# Fifth landing page: User selected actions
def access(role, status, option):
    '''
    A function that allows the user to carry out tasks that he/she selected

    Arguments:
        role -- either "Administrator" or "Customer"
        status -- (for Customers only) to check what the status is "Registered" or "Unregistered"
        option -- which action to take

    Outputs:
        depends on the option selected
    '''
    if role.lower() == "administrator":
        # Adding new cars into the system
        if option == "1":
            clear()
            print("ADDING INFORMATION OF NEW CARS")
            print("------------------------------")

            # New car information
            car_name = input("Car Name\nPlease provide the name of the car: ")
            car_brand = input("\nCar Model\nPlease provide the model of the car: ")
            plate_number = input("\nPlate Number\nPlease provide the plate number of the car: ")
            owner =  input("\nOwner\nPlease provide the name of the car's owner: ")
            car_status = 'available'
            duration = 0
            seats = int(input("\nSeats\nHow many seats are there in the car (provide a number): "))
            fuel_type = input("\nFuel\nWhat type of fuel does the car use: ")
            short_desc = input("\nDescription\nPlease provide a short description for the vehicle: ")
            rental_rate = int(input("\nRental\nPlease provide rental rate of the car: "))
            price = "RM" + str(rental_rate)

            car_details = [plate_number, car_name, car_brand, owner, car_status, duration, seats, fuel_type, short_desc, price]
            repeated = check_for_duplicate("car2.txt", car_details[0])

            if repeated: 
                write_to_file("car2.txt", car_details)

            else:
                print("Car already exists.")
                print()

            return input("Press 'r' to return to the previous screen or 'x' to exit.")

        elif option == "2":
            clear()
            try:
                with open("car2.txt", "r") as fp:
                    car_details = [line.split(", ") for line in fp]

            except:
                print("File cannot be opened.")
                return input("Press 'r' to return or 'x' to exit. ")

            plate_numbers = [car[0] for car in car_details]

            print("AVAILABLE CARS")
            print("--------------")
            print(*plate_numbers, sep="\n")
            user_input = input("Which car's detail do you want to modify [Press r to return]? ")

            if user_input.lower() == "r":
                return "r"
            else:
                selected_car = search_file("car2.txt", user_input)

            print("Which detail do you wish to modify?")
            print("-----------------------------------")
            print("[1] Plate Number")
            print("[2] Car Name")
            print("[3] Car Model")
            print("[4] Car's Owner")
            print("[5] Status")
            print("[6] Duration")
            print("[7] Seats")
            print("[8] Fuel Type")
            print("[9] Short Description")
            print("[10] Rental rates")
            detail_to_modify = input("Please select an option: ")

            if detail_to_modify != "5":
                new_detail = input("New data: ")
                selected_car[int(detail_to_modify)-1] = new_detail

            else:
                new_car_status = input("New status: ")
                rental_duration = input("New rental duration: ")
                selected_car[4] = new_car_status
                selected_car[5] = rental_duration

            new_line = ""
            try:
                with open("car2.txt", "r") as fp:
                    for line in fp:
                        new_line += line if selected_car[0] not in line else ", ".join(selected_car)
                with open("car2.txt", "w") as fp:
                    fp.writelines(new_line)

            except:
                print("File cannot be opened.")
                return input("Press 'r' to return or 'x' to exit. ")

            return input("Press 'r' to return to the previous screen or 'x' to exit.")

        elif option == "3":
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
            if user_option in ['1', '2']:
                clear()
                try:
                    with open("car2.txt", "r") as fp:
                        car_details = [line.split(", ") for line in fp]

                except:
                    print("File cannot be opened.")
                    return input("Press 'r' to return or 'x' to exit. ")

                for item in car_details:
                    # Display "Rented" cars
                    if user_option == '1' and item[4].lower() == 'rented':
                        print(f"Car: {item[1]}, Plate Number: {item[0]}, Rental Duration: {item[5]}")
                    # Display "Available" cars
                    elif user_option == '2' and item[4].lower() == 'available':
                        print(f"Car: {item[1]}, Plate Number: {item[0]}")
                return input("Press 'r' to return to previous page or 'x' to exit. ")

            elif user_option == '3' or user_option == '4':
                clear()

                try:
                    with open("customer2.txt", "r") as fp:
                        customer_details = [line.split(", ") for line in fp]

                except:
                    print("File cannot be opened.")
                    return input("Press 'r' to return or 'x' to exit. ")

                # Display customer bookings
                if user_option == '3':
                    for item in customer_details:
                        print(f"{item[2]}'s number of bookings: {', '.join(item[9].split('-'))}") # Come back to this later
                else:
                    print("Which month's records do you wish to view?")
                    count = 1
                    while count <= 12:
                        print(f"[{count}] {datetime.datetime.strptime(str(count), '%m').strftime('%B')}")
                        count += 1
                    selected_month = input("Please select an option: ")

                    for customer in customer_details: 

                        sum_of_payment = 0
                        date_payment = customer[7].split("; ")

                        for pair in date_payment:
                            if selected_month == pair.split('-')[0]:
                                sum_of_payment += int(pair.split('-')[1])
                        print(f"{customer[0]}: {sum_of_payment}")

                return input("Press 'r' to return to previous page or 'x' to exit. ")

            else:
                return "r"

        elif option == "4":
            clear()

            try:
                with open ("customer2.txt", "r") as fp:
                    user_details = [line.split(", ") for line in fp]
            except:
                print("File cannot be opened.")
                return input("Press 'r' to return or 'x' to exit. ")

            usernames = [user[0] for user in user_details]

            print("AVAILABLE USERS")
            print("---------------")
            print(*usernames, sep="\n")

            searched_user = input("Which user's data do you want to see? [Press r to return] ")

            if searched_user.lower() == "r":
                return "r"
            else:
                user_details = search_file("customer2.txt", searched_user)

            print("CHOOSE WHAT TO SEARCH FOR:")
            print("[1] Customer bookings")
            print("[2] Customer payments", end='\n\n')
            print("[R] Return to previous screen")
            print("[X] Exit")
            user_option = input("Please select one of the options: ")

            if user_option == "1":
                clear()
                print(f"{user_details[0]}'s bookings: {', '.join(user_details[9].split('-'))}")

            elif user_option == "2":
                clear()
                sum_of_payment = 0
                date_payment = user_details[7].split("; ")
                for pair in date_payment:
                    if len(pair) != 0:
                        sum_of_payment += int(pair.split("-")[1])
                print(f"{user_details[0]}'s paid amount: {sum_of_payment}")
                if user_details[8] != "":
                    print(f"{user_details[0]}'s amount due: {user_details[8]}")
                else:
                    print(f"{user_details[0]}'s amount due: 0")

            elif user_option == "r":
                return "r"

            elif user_option == "x":
                return "x"

            else:
                print("Invalid input!")
                return input("Press 'r' to try again. ")

            return input("Press 'r' to return to the previous screen or 'x' to exit. ")

        elif option == "5":
            clear()

            try:
                with open("car2.txt", "r") as fp:
                    car_list = [line.split(", ") for line in fp]
            except:
                print("File cannot be opened.")
                return input("Press 'r' to return or 'x' to exit. ")

            rented_cars = [car[0] for car in car_list if car[4].lower() == 'rented']

            print("RENTED CARS")
            print("-----------")
            print(*rented_cars, sep="\n")

            returned_car = input("Please provide the plate number of the returned car: ")

            try:
                returned_car_details = search_file("car2.txt", returned_car)
                returned_car_details[4] = "Available"
                returned_car_details[5] = "0"

                new_line = ""
                with open("car2.txt", "r") as fp:
                    for line in fp:
                        if returned_car_details[0] not in line:
                            new_line += line

                        else:
                            new_line += ", ".join(returned_car_details)

                with open("car2.txt", "w") as fp:
                    fp.writelines(new_line)

                return input("Press 'r' to return to the previous screen or 'x' to exit.")

            except:
                print("Invalid input")
                return input("Press 'r' to return or 'x' to exit. ")

        elif option.lower() == "r":
            return "r"

        elif option.lower() == "x":
            exit()

        else:
            print("Invalid input")
            return input("Press 'r' to return or 'x' to exit. ")

    else:
        # Viewing the whole catalog
        if option == "1":
            clear()
            print("CATALOG")
            print("-------")
            try:
                with open ('car2.txt', 'r') as fp:
                    for line in fp:
                        print(f"Car Name: {line.split(', ')[1]}")
                        print(f"Car Model: {line.split(', ')[2]}")
                        print(f"Plate Number: {line.split(', ')[0]}")
                        print(f"Short Description: {line.split(', ')[8]}")
                        print(f"Seats: {line.split(', ')[6]}")
                        print(f"Fuel type: {line.split(', ')[8]}")
                        print(f"Status: {line.split(', ')[4]}")
                        print(f"Price: {line.split(', ')[9]}")
                        print()

            except:
                print("No record to show or File cannot be opened.")
                return input("Press 'r' to return or 'x' to exit. ")

            return input("Press 'r' to return to the previous screen.")

        if status.lower() == "registered":
            # Modifying personal details
            if option == "2":
                clear()
                user_details = search_file("customer2.txt", username)
                print("MODIFY PERSONAL DETAILS")
                print("-----------------------")
                print("Which detail do you wish to modify?")
                print("[1] Username")
                print("[2] Password")
                print("[3] Full Name")
                print("[4] IC/Passport Number")
                print("[5] Age")
                print("[6] Phone number")
                print("[7] Address")

                detail_to_modify = int(input("Please choose an option: "))

                if detail_to_modify != 7:
                    new_detail = input("New data: ")
                    user_details[detail_to_modify-1] = new_detail

                else:
                    new_address = input("New data: ")
                    new_address = sanitize_detail(new_address)
                    user_details[detail_to_modify-1] = new_address

                try: 
                    new_line = ""
                    with open("customer2.txt", "r") as fp:
                        for line in fp:
                            new_line += line if user_details[0] not in line else ", ".join(user_details)
                    with open("customer2.txt", "w") as fp:
                        fp.writelines(new_line)

                except:
                    print("File cannot be opened.")
                    return input("Press 'r' to return or 'x' to exit. ")

                return input("Press 'r' to return to the previous screen.")

            elif option == "3":
                user_details = search_file("customer2.txt", username)
                purchase_history = user_details[9].split("-")
                clear()
                print("PURCHASE HISTORY")
                print("----------------")
                if len(purchase_history) != 0:
                    print(*purchase_history, sep="\n")
                else:
                    print("No record exists.")

                return input("Press 'r' to return to the previous screen.")

            elif option == "4":
                clear()
                user_details = search_file("customer2.txt", username)

                with open("car2.txt", "r") as fp:
                    car_details = [line.strip().split(", ") for line in fp if user_details[0] in line]

                count = 1
                while count <= len(car_details):
                    print(f"[{count}] {car_details[count-1][1]}: {car_details[count-1][4].title()}")
                    count += 1

                return input("Press 'r' to return to the previous screen.")

            elif option == "5":
                clear()

                try:
                    with open("car2.txt", "r") as fp:
                        car_details = [line.split(", ") for line in fp]
                except:
                    print("File cannot be opened.")
                    return input("Press 'r' to return or 'x' to exit. ")

                available_cars = [car for car in car_details if car[4].lower() == "available"]

                count = 1
                selected_car  = []
                while count <= len(available_cars):
                    for car in available_cars:
                        print(f"Option [{count}]")
                        print(F"Car Name: {car[1]}")
                        print(f"Car Model: {car[2]}")
                        print(f"Plate Number: {car[0]}")
                        print(f"Short description: {car[8]}")
                        print(f"Seats: {car[6]}")
                        print(f"Fuel Type: {car[7]}")
                        print(f"Price: {car[9]}/day")   
                        print()
                        selected_car.append([count, car[0], car[1], car[2], car[8], car[6], car[7], car[9]])

                        count += 1

                rental_choice = input("Choose an option: ")

                for car in selected_car: 
                    if int(rental_choice) == car[0]:
                        input_date = input("When do you want to start renting the car? \nPlease provide the date in this format YYYY-MM-DD: ")
                        while True: 
                            try: 
                                rental_duration = int(input("How long do you want to rent (in days)? "))
                                break
                            except:
                                print("Your rental duration should be a number. Do not type it out.")
                                continue
                        start_date = datetime.date.fromisoformat(input_date)
                        end_date = start_date + datetime.timedelta(days=rental_duration)
                        total_rent = int(car[7][2:])*rental_duration

                        user_decision = input(f"You chose to rent {car[2]}, plate number {car[1]} from {start_date} until {end_date} for a total of {rental_duration} days. The total rent is RM{total_rent}. \nConfirm your choice? [y/n] ")

                        if user_decision.lower() == "y":
                            # Amending the rented car's details
                            rented_car_details = search_file("car2.txt", car[1])

                            rented_car_details[4] = "Rented"
                            rented_car_details[5] = str(rental_duration)

                            try:
                                car_new_line = ""
                                with open("car2.txt", "r") as fp:
                                    for line in fp:
                                        if rented_car_details[0] not in line:
                                            car_new_line += line

                                        else:
                                            car_new_line += ", ".join(rented_car_details)

                                with open("car2.txt", "w") as fp:
                                    fp.writelines(car_new_line)

                            except:
                                print("File cannot be opened.")
                                return input("Press 'r' to return or 'x' to exit. ")

                            # Amending the user's purchase history
                            user_details = search_file("customer2.txt", username)

                            if len(user_details[9]) >= 2:
                                user_details[9] = user_details[9].split("-")
                                user_details[9].append(rented_car_details[1])
                                user_details[9] = ("-").join(user_details[9])

                            else:
                                user_details[9] += rented_car_details[1]
                            try: 
                                user_new_line = ""
                                with open("customer2.txt", "r") as fp:
                                    for line in fp:
                                        if user_details[0] not in line:
                                            user_new_line += line

                                        else:
                                            user_new_line += ", ".join(user_details)

                                with open("customer2.txt", "w") as fp:
                                    fp.writelines(user_new_line)
                            except:
                                print("File cannot be opened.")
                                return input("Press 'r' to return or 'x' to exit. ")

                            print("PAYMENT")
                            print("-------")
                            print("[1] Credit card")
                            print("[2] Paypal")
                            print("[3] Pay after rental", end="\n\n")
                            print("[R] Return to previous screen")
                            print("[X] Exit")

                            payment_method = input("Please choose a payment method: ")

                            if payment_method == "1":
                                payment("credit card", total_rent)
                                user_details = search_file("customer2.txt", username)
                                payment_month = datetime.datetime.now().month
                                user_details[7] += str(payment_month) + "-" + str(total_rent) + "; "

                                try: 
                                    new_line = ""
                                    with open("customer2.txt", "r") as fp:
                                        for line in fp:
                                            new_line += line if user_details[0] not in line else ", ".join(user_details)
                                    with open("customer2.txt", "w") as fp:
                                        fp.writelines(new_line)

                                except:
                                    print("File cannot be opened.")
                                    return input("Press 'r' to return or 'x' to exit. ")

                            elif payment_method == "2":
                                payment("paypal", total_rent)
                                user_details = search_file("customer2.txt", username)
                                payment_month = datetime.datetime.now().month
                                user_details[7] += str(payment_month) + "-" + str(total_rent) + "; "

                                try:
                                    new_line = ""
                                    with open("customer2.txt", "r") as fp:
                                        for line in fp:
                                            new_line += line if user_details[0] not in line else ", ".join(user_details)
                                    with open("customer2.txt", "w") as fp:
                                        fp.writelines(new_line)

                                except:
                                    print("File cannot be opened.")
                                    return input("Press 'r' to return or 'x' to exit. ")

                            elif payment_method == "3":
                                user_details = search_file("customer2.txt", username)
                                user_details[8] += str(total_rent)

                                try: 
                                    new_line = ""
                                    with open("customer2.txt", "r") as fp:
                                        for line in fp:
                                            new_line += line if user_details[0] not in line else ", ".join(user_details)
                                    with open("customer2.txt", "w") as fp:
                                        fp.writelines(new_line)

                                except:
                                    print("File cannot be opened.")
                                    return input("Press 'r' to return or 'x' to exit. ")


                return input("Press 'r' to return to the previous screen.")

            else:
                return "r"

        else:
            # Registering
            if option == "2":
                register(role)
                print("You've successfully registered")

                return input("Press 'r' to return to the previous screen.")

            # Invalid input
            else:
                return "r"

# ------------------ MAIN PROGRAM -------------------------
# Selecting the role
role = role_selection()

while role != "x":
    # Breaking the loop
    if role == "x":
        break

    # Selecting whether to login or register or skip(only for customers)
    user_choice = login_register_menu(role)

    while user_choice != "r":

        if user_choice == "r":
            break

        # User chose login
        elif user_choice == "1":
            user_access, username, status = login(role)
            if user_access:
                user_action = granted_for_access(role, username, status)

                if user_action.lower() == "x":
                    exit()

                while user_action != "r":
                    user_action = access(role, status, user_action)
                    
                    if user_action == "r":
                        user_action = granted_for_access(role, username, status)

                    elif user_action.lower() == "x":
                        exit()

            else:
                user_action = input("Invalid credentials given. Press 'r' to try again.")


        # User chose register
        elif user_choice == "2":
            register(role)
            user_access, username, status = login(role)
            if user_access:
                user_action = granted_for_access(role, username, status)

                if user_action.lower() == "x":
                    exit()

                while user_action.lower() != "r":
                    user_action = access(role, status, user_action)

                    if user_action.lower() == "r":
                        user_action = granted_for_access(role, username, status)

                    elif user_action.lower() == "x":
                        exit()

            else:
                user_action = input("Invalid input given. Press 'r' to try again. ")
                    

        # User chose skip
        elif user_choice == "3":
            user_action = granted_for_access(role, "Customer", "Unregistered")
            
            if user_action.lower() == "x":
                exit()
            
            while user_action.lower() != "r":

                    if user_action.lower() == "r":
                        user_action = granted_for_access(role, username, status)
                    else:
                        user_action = access(role, status, user_action)

        elif user_choice == "x":
            exit()


        user_choice= login_register_menu(role)

    role = role_selection()