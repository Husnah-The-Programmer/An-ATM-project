print("Welcome to access bank")
password = int(input("Enter your 4 digit pin number:\n"))
balance =10000000
if(password == 1234):
    print("Automated Teller Machine")
    print("Choose 1 for Withdraw")
    print("Choose 2 for Balance Enquiry")
    print("Choose 3 for fast cash")
    print("choose 4 for deposit")
    print("Choose 5 for Exit")

    selection = int(input("enter your selection:"))
    if(selection == 1):
        withdrawalAmount =int(input("Enter amount to be  withdrawn:"))
        if(withdrawalAmount < balance):
            print("please take your amount:", withdrawalAmount)
            balance = balance - withdrawalAmount
            print("Debit successfull")
            print("Your balance is :", balance)
            print("Thanks for choosing access bank")
        else:
            print("insufficient funds")

    elif(selection == 2):
        print("Your available amount:", balance)

    elif(selection == 3):
        print("1->5,000")
        print("2->10,000")
        print("3->15,000")
        print("4->20,000")
        fastCashAmount = int(input("Enter fast cash option:"))
        if (fastCashAmount == 1 and 5000 < balance):
            print ("please take cash 5000")
            print("Debit successfull")
            balance = balance - 5000
            print("Your balance is :", balance)
        elif(fastCashAmount == 2 and 10000 < balance):
            print("please take cash 10000")
            print("Debit successfull")
            balance = balance - 10000
            print("Your balance is :", balance)
        elif(fastCashAmount == 3 and 15000 < balance):
            print("please take cash 15000")
            print("Debit successfull")
            balance = balance - 15000
            print("Your balance is :", balance)
        elif(fastCashAmount == 4 and 20000 < balance):
            print("please take cash 20000")
            balance = balance - 20000
            print("Your balance is :", balance)

    elif(selection == 4):
        print("How much would you like to deposit?:")
        deposit = int(input("Enter amount to deposit:"))
        balance = balance + deposit

        print("credit successful")
        print("Your balance is :", balance)
    elif(selection == 5):
        print("Are you sure you want to exit?:\n")
        exitAnswer = input("Enter yes or no\n")
        
        if(exitAnswer == "yes"):
            print("Exited successfully!\n")
            print("Access Bank loves you!\n")
            print("Thanks for banking with us")
        else:
            print("Cancel")
       
        
        

else:
    print("Password incorrect!")