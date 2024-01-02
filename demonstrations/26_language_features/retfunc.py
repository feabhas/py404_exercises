
def add1():
    def do_add1(x):
        return x+1

    return do_add1

inc = add1()
value = inc(2)
print(value)

def dec1(func):
    def do_dec1(x):
        return func(x+1)

    return do_dec1


@dec1
def square(a):
    return a**2

value = square(3)
print(value)
