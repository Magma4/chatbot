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
    print("7. Request For Documents")

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
                        print("Visit helpdesk.knust.edu.gh and create a ticket with your MOMO number and Transaction ID")
                        break
                    else:
                        print("Invalid option, please try again")
                        break

                elif sub_sub_option == 2:
                    print("Please check MOMO balance and Try again")
                    break


            elif sub_option == 2:
                print("1. Cost for regular students forms?")
                print("2. Cost for IDL application forms")
                print("3. Cost for international applicants")
                sub_sub_option = int(input("Please choose an option: "))

                if sub_sub_option == 1:
                    print("1. Is it for a undergraduate form?")
                    print("2. Is it for a postgraduate form?")
                    sub_sub_sub_option = int(input("Please choose an option: "))

                    if sub_sub_sub_option == 1:
                        print("Regular Undergraduate forms cost GHS 250")
                        break

                    elif sub_sub_sub_option == 2:
                        print("Regular Postgraduate forms cost GHS 280")
                        break

                elif sub_sub_option == 2:
                    print("1. Undergraduate(Diploma, Top-up, Bridging)")
                    print("2. Postgraduate")
                    sub_sub_sub_option = int(input("Please choose an option: "))

                    if sub_sub_sub_option == 1:
                        print("Undergraduate(Diploma, Top-up, Bridging) forms cost GHS 250")
                        break

                    elif sub_sub_sub_option == 2:
                        print("Postgraduate forms cost GHS 280")
                        break
                
                elif sub_sub_option == 3:
                    print("International students application forms cost USD$ 150")
                    break

            elif sub_option == 3:
                print("1. Eligible banks to purchase the forms from?")
                print("2. The mobile shortcode to use to purchase the forms?")
                print("3. Which post office can i pourchase the forms from?")
                sub_sub_option = int(input("Please choose an option: "))

                if sub_sub_option == 1:
                    print("You can purchase the forms from any of these banks, GCB, Ecobank, Calbank.")
                    break
                elif sub_sub_option == 2:
                    print("You can purchase the forms using the shortcode *447*160#")
                    break
                elif sub_sub_option == 3:
                    print("Any post office in Ghana")
                    break
        
        elif userInput == 2:
            print("DATES")
            print("1. When are application forms going to be released?")
            print("2. When is the deadline for the current admissions cycle?")
            print("3. When do we report to school?")
            sub_option = int(input("Please choose an option: "))

            if sub_option == 1:
                print("Please visit https://www.knust.edu.gh/admissions/prospective/applying for more information")
                break
            elif sub_option == 2:
                print("Please visit https://www.knust.edu.gh/admissions/prospective/applying for more information")
                break
            elif sub_option == 3:
                print("Please visit https://www.knust.edu.gh/academics/provisional-2023-2024-academic-year for more information")

        elif userInput == 3:
            print("APPLICATIONS")
            print("1. What is my current admission status?")
            print("2. Stuck at Application Review Stage?")
            sub_option = int(input("Please choose an option: "))

            if sub_option == 1:
                print("Please log in to the admissions portal and Select check Admission Status")
                break
            elif sub_option == 2:
                print("Go through the application and ensure that all fields are properly filled")
                break
        
        elif userInput == 4:
            print("ADMITTED")
            print("1. What do i do after gaining admission?")
            sub_option = int(input("Please choose an option: "))

            if sub_option == 1:
                print("Please log in to the admissions portal, download and print your provisional admission and acceptance letter. Fill the acceptance letter and post it to the school.")
                print("1. Are you a non-scholarship student?")
                print("2. Are you a scholarship student?")
                sub_sub_option = int(input("Please choose an option: "))

                if sub_sub_option == 1:
                    print("Check the fees schedule and make appropriate academic fees payment. then book and make payment for accommodation after.")
                    break
                elif sub_sub_option == 2:
                    print("Contact your benefactor, then book and make payment for accommodation after.")
                    break
        break

def fees():
    print("FEES AND PAYMENTS")

def aim():
    print("AIM APP AND STUDENT PORTAL")
    print("1. Login Issues")
    print("2. Course Registration")
    print("3. Check Results")
    print("4. Fees")

    while True:
        userInput = int(input("Please choose an option: "))
        if userInput == 1:
            print("1. Cannot Login?")
            print("2. Do not have credentials?")
            sub_option = int(input("Please choose an option: "))

            if sub_option == 1:
                print("Which account can't you login into?")
                print("1. AIM App")
                print("2. Student Portal")
                sub_sub_option = int(input("Please choose an option: "))

                if sub_sub_option == 1:
                    print("Log in with your student email and Password. If your username is 'jdoe1', you are required to enter 'jdoe1@st.knust.edu.gh', with your password to be able to login.")
                    break
                elif sub_sub_option == 2:
                    print("Use credentials given or Reset password using the link https://apps.knust.edu.gh/students")
                    break
            
            elif sub_option == 2:
                print("Reset your password from here https://apps.knust.edu.gh/students/Account/ForgotPassword")
                print("Or")
                print("Create a ticket at helpdesk.knust.edu.gh")
                break

        elif userInput == 2:
            print("1. Unable to register your courses.")
            sub_option = int(input("Please choose an option: "))

            if sub_option == 1:
                print("1. Have you paid your fees?")
                print("2. Check deadline for course registration")
                print("3. Have you contacted your exams officer?") # This is the last commit i did, we have to sort out the flowchart.
                


if __name__ == "__main__":
    greetings()
    services()
    query = int(input("Please select a service you need help with: "))
    
    while True:
        if query == 1:
            admissions()
            break
        elif query == 2:
            fees()
            break
        elif query == 3:
            aim()
                
    

    
    



# #takeCommand()

# if __name__ == "__main__":

#     greetings()
#     services()
#     query = int(input("Please select a service you need help with: "))
    

#     while True:
#         query != ""

#         if query == 1:
#             admissions()
        
