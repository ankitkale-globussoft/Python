age = int(input("enter the age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 59:
    print("Adult")
else:
    print("Senior")