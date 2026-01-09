def debug(func):
    def decor(*args, **kwargs):
        args_val = ', '.join(str(arg) for arg in args)
        kwargs_val = ', '.join(f"{k}={v}" for k, v in kwargs.items())

        print(f"calling: {func.__name__} with args: {args_val} and kwargs: {kwargs_val}")

        return func(*args, **kwargs)
    return decor

@debug
def ex_func(a, b):
    return a+b

@debug
def greet(name, greeting="Hello ji"):
    print(f"{greeting}, {name}")

ex_func(2, 2)
ex_func(6, 1)
ex_func(7, 6)

greet('ankit', greeting="Namaste")