# Initializing the system
import random
import datetime
from getpass import getpass
# import json 
import os
import validation

os.system("clear")

now = datetime.datetime.now()
pretty_line = ("=" * 58)  # line to make app more readable
empty_space = "\n"
database = {}


# This exception was added due to receiving error when using input on python in VSCode
# try:
#     input = raw_input
# except NameError: pass


def init():
    print(pretty_line)
    print("|              ***Welcome to Bank of Mario***            |")
    print("|                  Current date and time :               |")
    print(now.strftime("|                   %Y-%m-%d %H:%M:%S                  |"))
    print(pretty_line)

    have_account = int(input("Do you have an account with us: (1) YES (2) NO (3) EXIT \n"))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    elif have_account == 3:
        exit()
    elif have_account == "":
        print("No option has been selected, please choose an option")
    else:
        print("You have selected an invalid option")


# Login Function
def login():
    print(pretty_line)
    print("|                       *LOGIN*                          |")
    print(pretty_line)

    account_number_from_user = input("What is your account number? \n")
    is_valid_account_number = validation.account_validation(account_number_from_user)

    if is_valid_account_number:
        password = getpass(prompt="What is your password? \n", stream=None)

        for account_number, user_details in database.items():
            if account_number == int(account_number_from_user):
                if user_details[3] == password:
                    bank_operation(user_details)

        print("Invalid account or password, please try again")
        login()
    else:
        init()


# Register Function
def register():
    print(pretty_line)
    print("|                      *REGISTER*                        |")
    print(pretty_line)

    email = input("What is your email address? \n")
    first_name = input("What is your FIRST name \n")
    last_name = input("What is your LAST name \n")
    password = getpass(prompt="Create a password \n", stream=None)
    valid_password = getpass(prompt="Please re-enter the password \n", stream=None)
    initial_deposit = int(input("How much would you like to deposit today?\n"))

    if password == valid_password:

        try:
            account_number = generate_Account_Number()
            database[account_number] = [first_name, last_name, email, password, initial_deposit]

            print("Congratulations, your account has been created successfully!")
            print(pretty_line)
            print("%s, your account number is: %d" % (first_name, account_number))
            print("Please make sure to keep your account information safe!")
            print(pretty_line)
            print(empty_space)

            login()
        except ValueError():
            print("Account Generation failed due to poor connection")
            init()
    else:
        if password != valid_password:
            print("passwords DO NO MATCH, try again")
            register()


# Bank Operations Function
def bank_operation(user):
    print(pretty_line)
    print("Welcome %s %s " % (user[0], user[1]))
    print(pretty_line)
    print(empty_space)

    selected_option = int(input("What would you like to do? (1) WITHDRAW (2) DEPOSIT (3) FILE A COMPLAINT (4) CHECK "
                                "BALANCE (5) LOGOUT (6) EXIT \n"))

    if selected_option == 1:
        withdrawal_operation(user)
    elif selected_option == 2:
        deposit_operation(user)
    elif selected_option == 3:
        complaint_operation(user)
    elif selected_option == 4:
        check_balance_operation(user)
    elif selected_option == 5:
        logout()
    elif selected_option == 6:
        close_app_operation(user)
    elif selected_option == "":
        print("No option has been selected, please choose an option")
    else:
        print("Invalid option selected")
        bank_operation(user)


# Withdrawal Function
def withdrawal_operation(user):
    print("Your available balance is: $%d" % user[4])
    # How much would you like to withdraw and user defines amount (receive user input and store in variable)
    withdraw = int(input("How much would you like to withdraw? \n"))
    if user[4] >= withdraw:
        print(pretty_line)
        user[4] = round(user[4] - withdraw, 2)
        # output "take your cash"
        print("Take your cash")
        print("Your available balance is: $%d" % user[4])
        print(empty_space)
        bank_operation(user)
    elif user[4] < withdraw:
        print("Insufficient Funds")
        print("Your available balance is: $%d" % user[4])
        print(empty_space)
        withdrawal_operation(user)
    else:
        bank_operation(user)


# Deposit Function
def deposit_operation(user):
    print("Your current balance is: $%d" % user[4])
    # How much would you like to deposit? (receive user input and store in variable)
    deposit = int(input("How much would you like to deposit? \n"))
    print(pretty_line)
    user[4] = round(user[4] + deposit, 2)
    print("Your available balance is: $%d" % user[4])
    print("Thank for using our service, %s" % user[0])
    print(empty_space)
    bank_operation(user)


# File a Complaint Function
def complaint_operation(user):
    # What issue would you like to report? (receive user input and store in variable)
    complaint = str(input("What would you like to report? \n"))
    print(complaint)
    print(pretty_line)
    print("Thank you for your feedback, we will further investigate the issue")

    bank_operation(user)


# Check Balance Function
def check_balance_operation(user):
    print(pretty_line)
    print(empty_space)
    print("Your available balance is: \n")
    print("$%d" % user[4])

    bank_operation(user)


# Logout Function Returns User Back to Login
def logout():
    # saveDatabase()
    login()


# Close App Function Exits Application
def close_app_operation(user):
    close_App = str(input("Are you sure you want to exit the application? enter (Y) for YES and (N) for NO \n"))
    if close_App == "Y":
        print(empty_space)
        print("Thank you for your time, come again!")
        # saveDatabase()
        exit()
    else:
        bank_operation(user)


# Generates the Account Number
def generate_Account_Number():
    return random.randrange(1111111111, 9999999999)


# ACTUAL BANKING SYSTEM


init()
