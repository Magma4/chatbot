import datetime as dt # Import date and time


# speak("Hello, this isI am your AI assistant. You can ask me anything.")

# date()

def greetings():
    """This function let's magma greets the user when started"""
    # time()
    # date()
    hour = dt.datetime.now().hour
    if hour >= 6 and hour <= 12:
        print("Good morning")
    elif hour >= 12 and hour <= 18:
        print("Good afternoon")
    elif hour >= 18 and hour <= 24:
        print("Good evening")
    else:
        print("Good night")
    print("Welcome to the KNUST IT Support Center")  
    print("How can i help you?")

# wishMe()

def services():
    print("These are the list of support services we provide.")
    print("1. Admissions Support")
    print("2. Fees and Payment")
    print("3. AIM App and Student Portal")
    print("4. Transcript")
    print("5. Virtual Classroom")
    print("6. Graduation")
    print("7. ")

# services()

    
    # return query

def admissions():
    print("ADMISSIONS")
    print("1. Vouchers")
    print("2. Dates")
    print("3. Application")    
    print("4. Admitted")

    while True:
        userInput = int(input("Please choose an option: "))
        if userInput == 1:
            print("Vouchers")
            print("1. Paid For Voucher via MOMO, Did not receive it?")
            print("2. How much do application forms cost?")
            print("3. Where can I purchase vouchers?")
            sub_option = int(input("Please choose an option: "))


            if sub_option == 1:
                print("1. MOMO account debited")
                print("2. MOMO account not debited")
                sub_sub_option = int(input("Please choose an option: "))

                if sub_sub_option == 1:
                    print("When did you make payment?")
                    print("1. Under 24 hours")
                    print("2. Over 24 hours")
                    sub_sub_sub_option = int(input("Please choose an option: "))

                    if sub_sub_sub_option == 1:
                        print("Please wait for 24 hours")
                        break

                    elif sub_sub_sub_option == 2:
                        print("Provide MOMO number and Transaction ID")
                        break
                    else:
                        print("Invalid option, please try again")
                        break

                elif sub_sub_option == 2:
                    print("Please check MOMO balance and Try again")
                    break
        break

if __name__ == "__main__":
    greetings()
    services()
    query = int(input("Please select a service you need help with: "))
    
    while True:
        if query == 1:
            admissions()
            break
                
    

    
    



# #takeCommand()

# if __name__ == "__main__":

#     greetings()
#     services()
#     query = int(input("Please select a service you need help with: "))
    

#     while True:
#         query != ""

#         if query == 1:
#             admissions()
        
