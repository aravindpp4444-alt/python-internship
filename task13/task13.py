import os

FILE_NAME = "accounts.txt"

def create_account():
    acc_no = input("Enter Account Number: ")
    name = input("Enter Name: ")
    balance = float(input("Enter Initial Balance: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{acc_no},{name},{balance}\n")

    print("✅ Account created successfully")

def deposit():
    acc_no = input("Enter Account Number: ")
    amount = float(input("Enter Deposit Amount: "))

    lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            acc, name, bal = line.strip().split(",")
            if acc == acc_no:
                bal = float(bal) + amount
                file.write(f"{acc},{name},{bal}\n")
                found = True
            else:
                file.write(line)

    if found:
        print("💰 Amount deposited successfully")
    else:
        print("❌ Account not found")

def withdraw():
    acc_no = input("Enter Account Number: ")
    amount = float(input("Enter Withdraw Amount: "))

    lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            acc, name, bal = line.strip().split(",")
            bal = float(bal)
            if acc == acc_no:
                if bal >= amount:
                    bal -= amount
                    print("💸 Withdrawal successful")
                else:
                    print("❌ Insufficient balance")
                file.write(f"{acc},{name},{bal}\n")
                found = True
            else:
                file.write(line)

    if not found:
        print("❌ Account not found")

def check_balance():
    acc_no = input("Enter Account Number: ")

    with open(FILE_NAME, "r") as file:
        for line in file:
            acc, name, bal = line.strip().split(",")
            if acc == acc_no:
                print(f"📊 Account Holder: {name}")
                print(f"💰 Balance: ₹{bal}")
                return

    print("❌ Account not found")

while True:
    print("\n--- BANK MANAGEMENT SYSTEM ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("👋 Thank you for using Bank System")
        break
    else:
        print("❌ Invalid choice")
