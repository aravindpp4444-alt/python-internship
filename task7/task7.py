import datetime
import json
import os

FILE_NAME = "attendance.txt"

# Load attendance from file
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save attendance to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Mark attendance
def mark_attendance(data):
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    
    if date == "":
        date = str(datetime.date.today())

    students = int(input("Enter number of students: "))
    data[date] = {}

    for i in range(students):
        name = input("Enter student name: ")
        status = input("Present or Absent: ")
        data[date][name] = status

    save_data(data)
    print("✅ Attendance saved successfully")

# View attendance
def view_attendance(data):
    date = input("Enter date to view attendance (YYYY-MM-DD): ")

    if date in data:
        print(f"\nAttendance for {date}:")
        for name, status in data[date].items():
            print(name, ":", status)
    else:
        print("❌ No data found for this date")

# Main menu
def main():
    data = load_data()

    while True:
        print("\n--- Attendance Management System ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance(data)
        elif choice == "2":
            view_attendance(data)
        elif choice == "3":
            print("Thank you 👋")
            break
        else:
            print("Invalid choice ❌")

main()
