#Initializing the system
import random
import datetime

now = datetime.datetime.now()
prettyLine = "==========================================================" #line to make app more readable
database = {} #dictionary



def init():

    print(prettyLine)
    print("|              ***Welcome to Bank of Mario***            |")
    print("|                  Current date and time :               |")
    print(now.strftime("|                   %Y-%m-%d %H:%M:%S                  |"))
    print(prettyLine)

    haveAccount = int(input(("Do you have an account with us: (1) YES (2) NO (3) EXIT \n")))
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    elif(haveAccount == 3):
        exit()
    else:
        print("You have selected an invalid option")
        

#Login Function
def login():

    print(prettyLine)
    print("|                       *LOGIN*                          |")
    print(prettyLine)

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = raw_input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
            
    print("Invalid account or passsword, please try again")
    login()

#Register Function
def register(): 
    print(prettyLine)
    print("|                      *REGISTER*                        |")
    print(prettyLine)

    email = raw_input("What is your email address? \n")
    firstName = raw_input("What is your FIRST name \n")
    lastName = raw_input("What is yout LAST name \n")
    password = raw_input("Create a password \n")
    validPassword = raw_input("Please re-enter the password \n")
    initialDeposit = int(input("How much would you like to deposit today?"))

    if(password != validPassword):
        print("passwords DO NO MATCH, try again")
        register()
    elif(password == validPassword):
    
        accountNumber = generationAccountNumber()

        database[accountNumber] = [ firstName, lastName, email, password, initialDeposit ]

        print("Congratulations, your account has been created succesfully!")
        print(prettyLine)
        print("%s, your account number is: %d" % (firstName, accountNumber))
        print("Please make sure to keep your account information safe!")
        print(prettyLine)
        

        login()

#Bank Operations Function
def bankOperation(user):
    print(prettyLine)
    print("Welcome %s %s " % ( user[0], user[1] ))
    print(prettyLine)

    selectedOption = int(input("What would you like to do? (1) WITHDRAW (2) DEPOSIT (3) FILE A COMPLAINT (4) CHECK BALANCE (5) LOGOUT (6) EXIT \n"))
    
    if(selectedOption == 1):
        withdrawalOperation(user)
    elif(selectedOption == 2):
        depositOperation(user)
    elif(selectedOption == 3):
        complaintOperation(user)
    elif(selectedOption == 4):
        checkBalanceOperation(user)
    elif(selectedOption == 5):
        logout()
    elif(selectedOption == 6):
        closeAppOperation()
    else:
        print("Invalid option selected")
        bankOperation(user)

#Widthdrawal Function
def withdrawalOperation(user):
    #How much would you like to withdraw and user defines amount (recieve user input and store in variable)
    withdraw = int(input("How much would you like to withdraw? \n"))
    print(prettyLine)
    user[4] = round(user[4] - withdraw, 2) 
    #output "take your cash"
    print("Take your cash") 
    print("Your available balance is: $%d" % user[4])
    bankOperation(user)

#Deposit Function
def depositOperation(user):
     #How much would you like to deposit? (receive user input and store in variable)
    deposit = int(input("How much would you like to deposit? \n"))
    print(prettyLine)
    user[4] = round(user[4] + deposit, 2)
    print("Your available balance is: $%d" % user[4])
    print("Thank for using our service, %s" % user[0])
    bankOperation(user)

#File a Complaint Function
def complaintOperation(user):
    #What issue would you like to report? (receive user input and store in variable)
    complaint = raw_input("What would you like to report? \n")
    print(prettyLine)
    print("Thank you for your feedback, we will further investigate the issue")
   
    bankOperation(user)

#Check Balance Function
def checkBalanceOperation(user):
    print(prettyLine)
    print("Your available balance is: \n")
    print("$%d" % user[4])

    bankOperation(user)

#Logout Function Returns User Back to Login
def logout():
    login()

#Close App Funtion Exits Application 
def closeAppOperation():
    closeApp = input("Are you sure you want to exit the application? enter (Y) for YES and (N) for NO \n")
    if(closeApp == "Y"):
        print("Thank you for your time, come again!")
        exit()
    else:
        return bankOperation(user)

#Generates the Account Number
def generationAccountNumber():
    return random.randrange(1111111111,9999999999)


#### ACTUAL BANKING SYSTEM #####


init()