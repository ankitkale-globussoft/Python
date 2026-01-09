# yield function ko freeze (pause) karta hai,
# local variables + execution position save karta hai,
# aur next call pe wahin se resume karta hai.

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num) 