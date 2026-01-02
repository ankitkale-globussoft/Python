# Que 1
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive = 0
# for num in numbers:
#     if num > 0:
#         positive += 1

# print('count of possitve number is: ', positive)

# Que 2
# n = int(input("Enter the nth number: "))
# even = 2
# sum = 0
# while even <= n:
#     sum += even
#     even += 2

# print('the sum is: ', sum)

# Que 10
waittime = 1
retrie = 5
passs = input("Enter the pass: ")

while passs != "aa":
    retrie-=1
    print(f"please retry after {waittime}sec, retires left is {retrie}")
    passs = input("Enter the pass: ")
    waittime *= 2
    if retrie == 0:
        print("Maximum attempts reached, please contact support")
        break