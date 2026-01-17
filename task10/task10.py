import json
import os

FILE_NAME = "accounts.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f)

accounts = load_data()

while True:
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc_no = input("Enter account number: ")
        name = input("Enter customer name: ")
        accounts[acc_no] = {"name": name, "balance": 0}
        save_data(accounts)
        print("Account created successfully!")

    elif choice == "2":
        acc_no = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        save_data(accounts)
        print("Amount deposited successfully!")

    elif choice == "3":
        acc_no = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            save_data(accounts)
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        acc_no = input("Enter account number: ")
        print("Name:", accounts[acc_no]["name"])
        print("Balance:", accounts[acc_no]["balance"])

    elif choice == "5":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice!")
