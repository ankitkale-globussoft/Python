# *args used to get the dynamic number of arguments in a function
# like function(*args). it is a good practice to always use name args not any other 

def jodo(*args):
    for arg in args:
        print(arg)
    return "sum hai:- ",sum(args)

print(jodo(2, 3))
print(jodo(2, 3, 1))
print(jodo(2, 3, 1, 2))