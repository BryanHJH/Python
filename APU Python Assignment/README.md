- [1. Introduction](#1-introduction)
- [2. Expected files](#2-expected-files)
  - [2.1 Python files](#21-python-files)
  - [2.2 Text files](#22-text-files)
  - [2.3 PDF files](#23-pdf-files)
- [3. Links to Reference](#3-links-to-reference)
  - [3.1 Youtube](#31-youtube)
- [4. Flow of Program](#4-flow-of-program)
  - [4.1 For both roles (Customer and Admin)](#41-for-both-roles-customer-and-admin)
    - [4.1.1 Role selection screen](#411-role-selection-screen)
    - [4.1.2 Register screen](#412-register-screen)
    - [4.1.3 Login Screen](#413-login-screen)
    - [4.1.4 Exit](#414-exit)
  - [4.2 For Admin](#42-for-admin)
    - [4.2.1 Option screen](#421-option-screen)
    - [4.2.2 Add Cars to be rented out](#422-add-cars-to-be-rented-out)
    - [4.2.3 Modifying Car Details](#423-modifying-car-details)
    - [4.2.4 Displaying all records](#424-displaying-all-records)
    - [4.2.5 Displaying specific records](#425-displaying-specific-records)
    - [4.2.6 Return a Rented Car](#426-return-a-rented-car)
  - [4.3 For Customers (Unregistered)](#43-for-customers-unregistered)
    - [4.3.1 Displaying all Records](#431-displaying-all-records)
  - [4.4 For Customers (Registered)](#44-for-customers-registered)
    - [4.4.1 Modifying Personal Details](#441-modifying-personal-details)
    - [4.4.2 View Personal Purchase History](#442-view-personal-purchase-history)
    - [4.4.3 View Detail of Cars to be Rented Out](#443-view-detail-of-cars-to-be-rented-out)
    - [4.4.4 Renting a car for a duration](#444-renting-a-car-for-a-duration)
    - [4.4.5 Making payment](#445-making-payment)
  - [5. Extra details](#5-extra-details)
    - [5.1 Navigation between options](#51-navigation-between-options)
  - [Choose an option:](#choose-an-option)
  - [Please type the name of the car that you wish to modify[Press Y to return to main menu]: (input)](#please-type-the-name-of-the-car-that-you-wish-to-modifypress-y-to-return-to-main-menu-input)

# 1. Introduction
The program that is written is for APU UCDF2005(DI) Python Assignment.

The assignment requires us to write out a car rental system with people logging in with different roles. Each role will have a text file containing their login credentials, named after their roles. (e.g. role: admin, text file: admin_login_credentials.txt)

Every role will have different priveleges. All priveleges are listed in the [Assignment File](https://bit.ly/3aOD3v7). 

# 2. Expected files
This section contains all the expected files for this assignment.

## 2.1 Python files
1. main.py: The python file where all the code goes

## 2.2 Text files
1. [admin_login_credentials.txt](admin_login_credentials.txt): Text file containing all credentials of admins, including the       usernames, passwords, names, address, contact no. and so on  
2. customer_login_credentials.txt: Text file contaning all credentials of users, including the usernames, passwords, names, age, address, contact no. and so on  
3. Car_Records.txt: Text file containing the details of cars, including car names, brand, model, status (available or rented), duration being rented, price  
4. Customer_Records.txt: Text file containing the purchase details of customers, including their names, IC, bookings, no. of cars rented, amount paid, amount overdue, rental duration 
5. Admin_Records.txt: Text file containing the details of Admins 

## 2.3 PDF files
1. Documentation: Converted from a Word file about the program written.
2. Instruction/Assignment Question: [Assignment File](https://bit.ly/3aOD3v7)
   
# 3. Links to Reference
## 3.1 Youtube
1. [Python Tutorial: Create a Simple Login System Using a Text File](https://www.youtube.com/watch?v=_uefYX5ACZ8)
2. [python login system tutorial (For beginners) Python Tutorial](https://www.youtube.com/watch?v=1e9okb_gVXc)

# 4. Flow of Program
## 4.1 For both roles (Customer and Admin)
### 4.1.1 Role selection screen 
   1. It would show the 2 options (Admin & Customer) or 3 options (Admin, Member, Other). For other, it is the unregistered customer. If use 3 options, the "Skip" in register screen will useless
   
### 4.1.2 Register screen
   1. If it is **customer**, there would be an **extra option which is "Skip"** for the user to not register or login as they might just want to browse through the catalog
   2. When registering, we need to include details other than username and password. Other details (listed below) must also be included.
   3. All details will be appended into the text file
   4. All details must follow the order that is set, which is:
      1. Username
      2. Email
      3. Password
      4. Full name
      5. IC/Passport number
      6. Admin ID (For Admins Only)
      7. Age
      8. Phone Number
      9. Address
      10. Payment/Amount Paid (For Customers Only)
      11. Amount Due (For Customers Only)
      12. Bookings (For Customers Only)
      13. No. of Cars Rented/Purchase History (For Customers Only)
      14. Rental Duration (For Customers Only)
   5. Admin and Customers will have their information appended to different files, which will be accepted as an argument in register() function.
   6. Before registering, the system **must** check whether **the user is already registered** (It can be in another function or be in the same function)
   
### 4.1.3 Login Screen
   1. User will need to input their username/email and password
   2. Validation of the input will be done in another function named validate_user()
   3. After logging in, there will be a **global variable named granted** which would be **True** if Login is successful (validate_user() returns True).
      1. 2 different functions, one for Admin, one for Customers
      2. **grant_for_admin()** will allow **admin** to view their privileges and select what to do
      3. **grant_for_customer()** will **customers** to view their privileges and select what to do

### 4.1.4 Exit
1. Just use quit() or break.

## 4.2 For Admin
### 4.2.1 Option screen
1. List out all their privileges/options that are listed in the [Assignment File](https://bit.ly/3aOD3v7). 

### 4.2.2 Add Cars to be rented out
1. A text file called Car_Records.txt is available with the Car Name, Car Brand, Car Model, Seats, Fuel Type, How many doors, How many luggage can it carry, Short description, Status(rented, pending, available), duration left being rented(if status is rented)  [Reference from Avis](https://www.avis.com.my/Malaysia-Standard-Fleet)
2. To add these details, open the file using **open(filename, 'a')** and then write to the file.
3. Order of the Car Details:
   1. Car Name
   2. Car Brand
   3. Car Model
   4. Plate Number
   5. Owner's name
   6. Status
   7. Duration left being rented
   8. Short Description
   9. Seats
   10. Fuel Type
   11. Price
4. Car Details should be saved as a list
   
### 4.2.3 Modifying Car Details
1. Able to modify all car details as well as removing the details.
2. To modify the details, first check for the car name and owner's name (using if...else statement) and then use filename.replace('word_to_be_changed', 'new_word'). [Reference](https://pythonexamples.org/python-replace-string-in-file/)
3. Can be made into a function that accepts 2 arguments ('word_to_be_changed', 'new_word').

### 4.2.4 Displaying all records
1. To display only cars that are **rented out**, can use if...else statement to filter out the Status of the cars then print them out. (Refer to the Cars_Records.txt)
2. To display only cars that are **available**, can use if...else statement to filter out the Status of the cars then print them out. (Refer to the Cars_Records.txt)
3. To display only **customers' bookings** (Refer to the Customer_Records.txt)
4. To display only **customers' payment** (Refer to the Customer_Records.txt)
5. When user select options 1 and 2, it is automatically printed out because no input is needed.
6. When user select options 3 and 4, the system requires an input (**probably by month** is best) so that the system can check for data in that month. (Probably need to **'import datetime'**)

### 4.2.5 Displaying specific records
1. To display only **customers' bookings**, we can use if...else statement to filter out base on the **customer name** then print them out. (Refer to the Customer_Records.txt)
2. To display only **customers' payment**, we can use if...else statement to filter out base on the **customer name** then print them out. (Refer to the Customer_Records.txt)
3. User needs to input the customer name to make the search. So use if customer_name in line_of_file then print the information

### 4.2.6 Return a Rented Car
1. I think this is just Modifying Car Details part but only specific to the status and duration of the car. (Update details of car and customer)

## 4.3 For Customers (Unregistered)
### 4.3.1 Displaying all Records
1. Show all car details except status, owner's name and duration. Only cars that are available are shown.

## 4.4 For Customers (Registered)
### 4.4.1 Modifying Personal Details
1. Details that can be modified:
   1. Username
   2. Email
   3. Password
   4. Full Name
   5. IC/Passport Number
   6. Age
   7. Address
   8. Phone Number
   9. Include all Car Details
2. Accepts input (sentinel loop, meaning keep asking until the user say quit) where the user select which detail to modify.
3. To modify, use the same method as the admin

### 4.4.2 View Personal Purchase History
1. Whenever the customer rents a car, append it into a list.
2. When the customer wants to view its purchase history, search for the customers name, by filtering based on his/her username then do print(*[list_of_cars], sep='\n')

### 4.4.3 View Detail of Cars to be Rented Out
1. Search through the Car_Records.txt for the customer's Full Name and print out all the cars that have the same match
2. The cars that are printed out must have the status 'available', **if rented, show 'rented'.**

### 4.4.4 Renting a car for a duration
1. Display all cars that are available that does not belong to the user
2. Make it menu-driven like how they would choose the options on what to do next.
3. When they select the car, the user needs to make another input on how many days they are renting the car. After the input, use datetime to calculate the end of the rental and tell the user. Save the end date of rental to a variable so that the system can update the Car_Records.txt after the user make the payment
4. Once all the details are keyed in by the user, set the selected car's status to pending

### 4.4.5 Making payment 
1. This is not in the main option menu. This will only appear after the Renting section where the input will be asked to "Continue to Payments" or "Continue Browsing" or "Cancel Booking".
2. If "Continue to Payments", the system will check for the duration of days and multiply with the renting rate of the selected car.
3. After calculation, the system will display the price then ask for payment method (Credit/Debit Card, Direct Debit, PayPal)
4. If Credit Card/Debit Card, ask for:
   1. Card Number
   2. Card Owner Name
   3. Expiry date
   4. CVV
5. If Direct Debit:
   1. Show the account information of the Rental Company bank, including:
      1. Bank Name
      2. Account Number
      3. Account Name
      4. Account Currency
      5. Account Type
6. If PayPal:
   1. Request PayPal email
   2. Request PayPal password
7. Should we include PayPal?
8. After payment is completed, using the variables set in the previous section, update the Car_Records.txt

## 5. Extra details
### 5.1 Navigation between options
So when the admin/customer selects one of the options after logging in, they need to have a button/option to go back to the main option menu screen. Since the main options are numbers, I think we can make going back to the main menu a letter like "Y" so that the user can choose other stuff to do without logging in several times. So the menu might look like:

Example of Main Option Menu (for Admin):
[1] Adding Cars to be Rented Out
[2] Modifying Car Details
[3] Display records
[4] Search records
[5] Return Rented Car
[6] Log Out

Choose an option: 
------------------------------------------
Example of Modifying Car Details:

Please type the name of the car that you wish to modify[Press Y to return to main menu]: (input)
------------------------------------------
Example of Display records:
Display Records of:
    [1] Rented cars
    [2] Available cars
    [3] Customer Bookings
    [4] Customer Payments
[Y] Return to Main Menu