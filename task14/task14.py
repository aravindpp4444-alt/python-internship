contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("⚠️ No contacts found.")
        return

    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("✅ Contact Found:")
            print(contact)
            found = True
            break

    if not found:
        print("❌ Contact not found.")

def update_contact():
    name = input("Enter name to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            print("✅ Contact updated successfully!")
            return

    print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("✅ Contact deleted successfully!")
            return

    print("❌ Contact not found.")

while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("👋 Exiting program. Bye!")
        break
    else:
        print("⚠️ Invalid choice. Try again.")
