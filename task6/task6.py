# Student Registration Form with Validation

# Name validation
name = input("Enter your name: ")
if not name.isalpha():
    print("Error: Name should contain only alphabets")
    exit()

# Age validation
age = int(input("Enter your age: "))
if age < 18:
    print("Error: Age must be 18 or above")
    exit()

# Mobile number validation
mobile = input("Enter your mobile number: ")
if not mobile.isdigit() or len(mobile) != 10:
    print("Error: Mobile number must be 10 digits")
    exit()

# Email validation
email = input("Enter your email: ")
if "@" not in email or "." not in email:
    print("Error: Invalid email address")
    exit()

# Username validation
username = input("Enter username: ")
if username == "":
    print("Error: Username cannot be empty")
    exit()

# Password validation
password = input("Enter password: ")
if len(password) < 8:
    print("Error: Password must be at least 8 characters")
    exit()

print("\n✅ Registration Completed Successfully!")
