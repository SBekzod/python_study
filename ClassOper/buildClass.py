class Person:
    position = 'user'
    __property = 500000

    def __init__(self, name, age, nation, is_married, secrets):
        self.name = name
        self.age = age
        self.nation = nation
        self.is_married = is_married
        self.__secret_message = secrets

    def get_jump(self, height):
        print('{0} jumped with {1} metres'.format(self.name, height))

    def get_swim(self):
        print('{0} started to swim'.format(self.name))

    def change_your_name(self, new_name):
        print('{0} changed own name into {1}'.format(self.name, new_name))
        self.name = new_name

    def make_greeting(self):
        print('Hi, my name is {0} and I am {1} years-old.'.format(self.name, self.age))

    def reveal_message(self):
        return self.__secret_message

    def __change_message(self, new_secrets):
        self.__secret_message = new_secrets
        print('Message is changed into {0}'.format(self.__secret_message))
        return self.__secret_message

    def please_change_message(self, new_secrets):
        self.__change_message(new_secrets)
        return self.__secret_message

    def change_position_to_admin(self):
        self.position = 'admin'


person = Person("David", 32, 'uzbek', True, 'apple')
print('=' * 41)
print('person position: {0}'.format(person.position))
# print('person property: {0}'.format(person.__property))              # do not reach
person.make_greeting()
print('=' * 41)
person.change_your_name('Patrick')
print('=' * 41)
person.make_greeting()
print('=' * 41)
print('Initial position: {0}'.format(person.position))
person.change_position_to_admin()
print('Position after change: {0}'.format(person.position))
print()

print('**** second phase started **** ')
print(person.name)                   # name is obtainable
# print(person.__secret_message)       # is not achievable

print('The secret message is {0}'.format(person.reveal_message()))  # name is obtainable
# print(person.__change_message('cherry'))  # is not achievable
person.please_change_message('cherry')  # do reach
