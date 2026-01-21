def calculate_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da
    tax = gross * 0.05
    net = gross - tax
    return hra, da, gross, tax, net


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    hra, da, gross, tax, net = calculate_salary(basic)

    with open("payroll.txt", "a") as file:
        file.write(f"\nID: {emp_id}")
        file.write(f"\nName: {name}")
        file.write(f"\nBasic Salary: {basic}")
        file.write(f"\nHRA: {hra}")
        file.write(f"\nDA: {da}")
        file.write(f"\nGross Salary: {gross}")
        file.write(f"\nTax: {tax}")
        file.write(f"\nNet Salary: {net}")
        file.write("\n----------------------")

    print("\nEmployee payroll added successfully!")


while True:
    print("\n--- Employee Payroll System ---")
    print("1. Add Employee")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
