# without list comprehention:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newList = []
# we want to add fruitnames that contain a in their name
# for x in fruits:
    # if 'a' in x:
        # newList.append(x)
# print(newList)

# with list comprehention: 
# syntax: newList = [experssion for x in iterable if condition == true]

newList = [x for x in fruits if 'p' in x]

print(newList)