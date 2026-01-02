age = int(input("Enter the age: "))
day = input("Enter weekday: ")

price = 12 if age > 18 else 8
if day == "Wednesday":
    price -= 2

print("Movie Ticket price for you is: $", price)