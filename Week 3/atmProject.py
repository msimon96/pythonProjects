from getpass import getpass
import datetime
now = datetime.datetime.now()

username = input("What is your username? \n")
allowedUsers = ['Mario','John','Jane']
allowedPassword = ['PassMario','PassJohn','PassJane']
balance = round(1000.00, 2)

if(username in allowedUsers):
    password = getpass("Please enter your password \n")
    userId = allowedUsers.index(username)

    if(password == allowedPassword[userId]):
        def mainMenu():
            while(True):
                print ('Current date and time : ')
                print (now.strftime("%Y-%m-%d %H:%M:%S"))
            #Insert welcome message "Hi " + %name + ", How can we assist you today?"
                print ("Hi %s" % username + ", How can we assist you today?") 
                print("These are your available options to choose from:")
                print("1. Withdraw Funds")
                print("2. Make a Deposit")
                print("3. File a Complaint")
                print("4. Check My Balance")
                print("5. Exit")

                selectedOption = int(input("Please select an option by typing the number associated with it: \n"))

                if(selectedOption == 1):
                    #How much would you like to withdraw and user defines amount (recieve user input and store in variable)
                    withdraw = int(input("How much would you like to withdraw? \n"))
                    cashOut = round(balance - withdraw, 2) 
                    #output "take your cash"
                    print("Take your cash") 
                    print("Your available balance is: $%s" % cashOut)

                elif(selectedOption == 2):
                    #How much would you like to deposit? (receive user input and store in variable)
                    deposit = int(input("How much would you like to deposit? \n"))
                    cashIn = round(balance + deposit, 2)
                    print("Your available balance is: $%s" % cashIn)
                    print("Thank for using our service, %s" %username)
                
                elif(selectedOption == 3):
                    #What issue would you like to report? (receive user input and store in variable)
                    complaint = input("What would you like to report? \n")
                    print("Thank you for your feedback, we will investigate the issue")
                    
                
                elif(selectedOption == 4):
                    print("Your available balance is: \n")
                    print("$" + round(balance, 2))
                
                elif(selectedOption == 5):
                    closeApp = input("Are you sure you want to exit the application? enter Y for YES and N for NO \n")
                    if(closeApp == "Y"):
                        print("Thank your time, come again!")
                        exit(0)
                    else:
                        return mainMenu()

                else:
                    print("Invalid option selected. Please try again.")
        mainMenu()
    else: 
        print ("Sorry, the PASSWORD you entered is incorrect, please try again")

else:
    
    print("The username entered could not be found, please try again")
