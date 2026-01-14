students = {}

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        students[roll] = {"name": name, "marks": marks}
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for roll, data in students.items():
                print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")

    elif choice == "3":
        roll = int(input("Enter Roll Number to update: "))
        if roll in students:
            name = input("Enter new name: ")
            marks = int(input("Enter new marks: "))
            students[roll]["name"] = name
            students[roll]["marks"] = marks
            print("Student updated successfully!")
        else:
            print("Student not found.")

    elif choice == "4":
        roll = int(input("Enter Roll Number to delete: "))
        if roll in students:
            del students[roll]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
