def tag(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return '<{0}>{1}</{0}>'.format(name, func(*args, **kwargs))
        return wrapper
    return decorator

class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @tag('div')
    @tag('p')
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)

@tag('em')
def greet():
    return 'hello'

jane = Person('Jane', 'Doe')
print(greet(), jane.fullname())
