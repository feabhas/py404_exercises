class MobilePhone:
    def __init__(self, model, number):
        self.model = model
        self.number = number
        self.call_list = []

    def __str__(self):
        return 'MobilePhone model={}, number={}, calls={}' \
            .format(self.model, self.number, self.call_list)

    def add_call(self, call):
        self.call_list.append(call)

    def get_number(self):
        return self.number

    def set_number(self, number):
        if not number.startswith('07') or len(number) != 11:
            raise UserWarning('Invalid module phone number: {}'.format(number))
        self.number = number


print('Create Nokia')
nokia = MobilePhone('Nokia 5110', '07891012345')
nokia.add_call({'07923456789': 12.2})
print(nokia)

nokia.set_number('07987654321')
print('New number {}'.format(nokia.get_number()))

class SmartPhone(MobilePhone):
    def __init__(self,  model, number):
        super().__init__( model, number)
        self.apps = []

    def __str__(self):
        return '{}, apps={}' \
            .format(super().__str__(), self.apps)

    def add_app(self, app):
        self.apps.append(app)

print('Create iPhone')
iphone = SmartPhone('iPhone', '07923456789')
iphone.add_app('DropBox')
iphone.add_call({'07891012345': 12.2})
print(iphone)


class MobilePhoneException(Exception):
    pass