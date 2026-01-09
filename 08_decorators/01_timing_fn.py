import time

def timer(func):
    def wrapper(*args, **kwargs):
        strat = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - strat} time")
        return result
    return wrapper

@timer
def ex_function(n):
    time.sleep(n)

ex_function(2.055)