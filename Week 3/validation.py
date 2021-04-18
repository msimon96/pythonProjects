# Validation 
def account_validation(account_number):
    # check if accountNumber is not empty
    # if accountNumber is 10 digits
    # if the accountNumber is an integer
    if account_number:

        if len(str(account_number)) == 10:

            try: 
                int(account_number)
                return True
            except ValueError:
                print("Invalid Account Number, account number should be a number")
            except TypeError:
                print("Invalid account type")
                return False

        else:
            print("Account Number cannot be more than or less than 10 digits")
            return False
    else:
        print("Account Number is a required field")
        return False
