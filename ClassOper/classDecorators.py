class Person:
    __position = 'user'
    __property = 500000

    def __init__(self, name, age, nation):
        self.__name = name
        self.__age = age

    def say_name(self):
        return self.__name

    def change_your_name(self, new_name):
        self.__name = new_name
        return self.__name

    @property
    def named(self):
        return self.__name

    @named.setter
    def named(self, new_name):
        self.__name = new_name

    @named.deleter
    def named(self):
        del self.__name

    @classmethod
    def get_property(cls):
        print('The class initial state variable {0}'.format(cls.__position))

    @staticmethod
    def get_pure_command():
        print('Dear class breeze with fresh air')


person = Person("David", 32, 'uzbek')
print('=' * 41)

# traditional way
answer_one = person.say_name()
print(answer_one)
answer_two = person.change_your_name('Erick')
print(answer_two)

print('=' * 41)

# PROPERTY DECORATORS
print(person.named)
person.named = 'Marcos'
print(person.named)
del person.named
# print(person.named)         # will not reach because of deletion
print()

# CLASS DECORATORS
print('=' * 41)
print('=' * 41)
Person.get_property()
Person.get_pure_command()

