# kwargs used to get the arguments in a key value pair

def hero(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

hero(name="shaktiman", power="lazer")
print("---------")
hero(name="shaktiman")
print("---------")
hero(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")
print("---------")