
def decn(func):
    def do_dec1(*args, **kwargs):
        return func(*args, **kwargs) + 1

    return do_dec1


@decn
def add(a, b):
    return a + b

value = add(3, 4)
print(value)



