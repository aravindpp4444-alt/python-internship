print("==== Conversion Menu ====")
print("1. Celsius to Fahrenheit")
print("2. Kilometers to Miles")
print("3. Kilograms to Pounds")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

elif choice == 2:
    km = float(input("Enter distance in Kilometers: "))
    miles = km * 0.621371
    print(f"{km} km = {miles} miles")

elif choice == 3:
    kg = float(input("Enter weight in Kilograms: "))
    pounds = kg * 2.20462
    print(f"{kg} kg = {pounds} pounds")

else:
    print("Invalid choice")
