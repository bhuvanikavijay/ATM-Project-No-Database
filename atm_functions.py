users={}
def create_account():
    print("---Create Account---")
    name=input("Enter your name: ")
    acc_no=input("Enter your acc_no: ")
    email=input("Enter your Email ID: ")
    mobile=input("Enter your Mobile Number: ")
    password=input("Create your Own Password: ")
    if acc_no in users:
        print("Account already exists!")
    else:
        users[acc_no]={"name":name,
                       "email":email,
                       "mobile":mobile,
                       "password":password,
                       "balance":0}
        print("Account is Created Successfully!")

def login():
    print("---Login---")
    acc_no=input("Enter your Account Number: ")
    password=input("Enter your Password: ")
    if acc_no in users and users[acc_no]["password"]==password:
        print("Login Successfull!")
        return acc_no
    elif acc_no in users:
        print("Wrong Password")
        return None
    else:
        print("Account not found!")
        return None

def deposit(acc_no):
    print("----Deposit Money----")
    amount=int(input("Enter Amount to Deposit: "))
    users[acc_no]["balance"]+=amount
    print(f"${amount} deposited successfully!")

def withdraw(acc_no):
    print("----Withdraw Money----")
    amount=int(input("Enter amount to Withdraw: "))
    if amount <= users[acc_no]["balance"]:
        users[acc_no]["balance"] -= amount
        print(f"${amount} withdrawn successfully!")
    else:
        print("Insufficient balance!")

def show_balance(acc_no):
    print("----Balance Information----")
    print(f"Your Balance is $ {users[acc_no]['balance']}")

def forgot_password():
    print("----Forgot Password----")
    acc_no=input("Enter your Account Number: ")
    email=input("Enter your Email: ")
    if acc_no in users and users[acc_no]["email"]==email:
        new_password=input("Enter new password: ")
        users[acc_no]["password"]=new_password
        print("Password Entered Successfully")
    else:
        print("Details do not match!")

def find_id():
    print("----Find ID----")
    email=input("Entered your email: ")
    for acc_no, details in users.items():
        if details["email"]==email:
            print(f"your account number is: {acc_no}")
            return
        print("No account found with this email!")
    
        
               
