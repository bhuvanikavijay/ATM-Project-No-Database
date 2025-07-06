from atm_functions import*
def main():
    while True:
        print("==========Welcome to BHU Bank==========")
        print("1. Login")
        print("2. Create Account")
        print("3. Settings")
        print("4. Exit")
        choice = input("Enter your Choice: ")
        if choice == "1":
            acc_no = login()
            if acc_no:
                while True:
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Show Balance")
                    print("4. Logout")
                    atm_choice = input("Choose an option: ")
                    if atm_choice == "1":
                        deposit(acc_no)
                    elif atm_choice == "2":
                        withdraw(acc_no)
                    elif atm_choice == "3":
                        show_balance(acc_no)
                    elif atm_choice == "4":
                        print("Logged out")
                        break
                    else:
                        print("Invalid option")
        elif choice == "2":
            create_account()
        elif choice == "3":
            print("----Settings----")
            print("1. Forgot Password")
            print("2. Find ID")
            settings_choice=input("Enter your Choice: ")
            if settings_choice == "1":
                forgot_password()
            elif settings_choice == "2":
                find_id()
            else:
                print("Invalid settings option!")
        elif choice == "4":
            print("Thank you for using BHU Bank. Have a Nice Day!!!")
            break
        else:
            print("Invalid main option!")
if __name__ == "__main__":
    main()

                
        
            
                       
