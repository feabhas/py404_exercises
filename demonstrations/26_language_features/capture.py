
def add_n(n):
    def do_add(x):
        return x+n

    return do_add

add2 = add_n(2)
value = add2(10)
print(value)

add100 = add_n(100)
value = add100(10)
print(value)

print(add_n(1)(2))


def addn(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + n

        return wrapper
    return decorator

@addn(10)
def add(a, b):
    return a + b

value = add(3, 4)
print(value)
