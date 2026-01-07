marks = int (input("Enter your marks:"))
if marks>=90 and marks <=100:
    print("grade:A")
elif marks>=80 and marks<90:
    print("grade:B")
elif marks>=65 and marks<80:
    print("grade:c")
elif marks>=45 and marks<65:
    print("grade:d")
else:
    print("grade:Fail")
