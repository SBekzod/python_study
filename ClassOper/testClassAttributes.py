class Person:
    __position = 'user'
    __property = 500000
    friend = 'fop'

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


per_one = Person("David", 32, 'uzbek')
per_two = Person("Tina", 32, 'korean')
print(per_one.friend)
print(per_two.friend)

print('=' * 40)
Person.friend = 'oop'
print(per_one.friend)
print(per_two.friend)


