def para(func):
    def wrapper(self, *args, **kwargs):
        return '<p>{}</p>'.format(func(self, *args, **kwargs))
    return wrapper

class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @para
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)

jane = Person('Jane', 'Doe')
print(jane.fullname())
