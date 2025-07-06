from tkinter import *
from tkinter import messagebox

users = {}

# Function: Deposit
def deposit_screen(account_number):
    def deposit():
        try:
            amt = float(amount_entry.get())
            users[account_number]['balance'] += amt
            messagebox.showinfo("Success", f"₹{amt} deposited!")
            deposit_win.destroy()
        except ValueError:
            messagebox.showerror("Error", "Enter valid amount!")

    deposit_win = Toplevel(root)
    deposit_win.title("Deposit Money")
    deposit_win.geometry("250x150")

    Label(deposit_win, text="Enter amount:").pack()
    amount_entry = Entry(deposit_win)
    amount_entry.pack()

    Button(deposit_win, text="Deposit", command=deposit).pack(pady=10)

# Function: Withdraw
def withdraw_screen(account_number):
    def withdraw():
        try:
            amt = float(amount_entry.get())
            if amt <= users[account_number]['balance']:
                users[account_number]['balance'] -= amt
                messagebox.showinfo("Success", f"₹{amt} withdrawn!")
                withdraw_win.destroy()
            else:
                messagebox.showerror("Error", "Not enough balance!")
        except ValueError:
            messagebox.showerror("Error", "Enter valid amount!")

    withdraw_win = Toplevel(root)
    withdraw_win.title("Withdraw Money")
    withdraw_win.geometry("250x150")

    Label(withdraw_win, text="Enter amount:").pack()
    amount_entry = Entry(withdraw_win)
    amount_entry.pack()

    Button(withdraw_win, text="Withdraw", command=withdraw).pack(pady=10)

# Function: Show Balance
def show_balance(account_number):
    balance = users[account_number]['balance']
    messagebox.showinfo("Balance", f"Your balance is ₹{balance}")

# After login menu
def open_main_menu(account_number):
    menu_win = Toplevel(root)
    menu_win.title("ATM Menu")
    menu_win.geometry("300x250")

    Label(menu_win, text=f"Welcome, {users[account_number]['name']}!").pack(pady=10)

    Button(menu_win, text="Deposit", width=20, command=lambda: deposit_screen(account_number)).pack(pady=5)
    Button(menu_win, text="Withdraw", width=20, command=lambda: withdraw_screen(account_number)).pack(pady=5)
    Button(menu_win, text="Show Balance", width=20, command=lambda: show_balance(account_number)).pack(pady=5)
    Button(menu_win, text="Logout", width=20, command=menu_win.destroy).pack(pady=10)

# Login function
def login():
    acc = acc_entry.get()
    pwd = pwd_entry.get()
    if acc in users and users[acc]["password"] == pwd:
        open_main_menu(acc)
    else:
        messagebox.showerror("Login Failed", "Invalid account or password.")

# Create account window
def open_create_account():
    def create():
        name = name_entry.get()
        acc = acc_entry_new.get()
        pwd = pwd_entry_new.get()
        balance = bal_entry.get()

        if acc in users:
            messagebox.showerror("Error", "Account already exists!")
        else:
            try:
                users[acc] = {
                    "name": name,
                    "password": pwd,
                    "balance": float(balance)
                }
                messagebox.showinfo("Success", "Account created successfully!")
                create_win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Balance must be a number!")

    create_win = Toplevel(root)
    create_win.title("Create Account")
    create_win.geometry("300x250")

    Label(create_win, text="Name:").pack()
    name_entry = Entry(create_win)
    name_entry.pack()

    Label(create_win, text="Account Number:").pack()
    acc_entry_new = Entry(create_win)
    acc_entry_new.pack()

    Label(create_win, text="Password:").pack()
    pwd_entry_new = Entry(create_win, show='*')
    pwd_entry_new.pack()

    Label(create_win, text="Initial Balance:").pack()
    bal_entry = Entry(create_win)
    bal_entry.pack()

    Button(create_win, text="Create Account", command=create).pack(pady=10)

# Main GUI
root = Tk()
root.title("ATM Machine - Login")
root.geometry("300x220")

Label(root, text="Account Number:").pack()
acc_entry = Entry(root)
acc_entry.pack()

Label(root, text="Password:").pack()
pwd_entry = Entry(root, show='*')
pwd_entry.pack()

Button(root, text="Login", command=login).pack(pady=10)
Button(root, text="Create New Account", command=open_create_account).pack()

root.mainloop()

