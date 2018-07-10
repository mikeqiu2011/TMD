
class Person:
    def __init__(self, age=18):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age in range(0,200):
            self.__age = age
        else:
            print("age not valid")
    pass

p1 = Person(18)

print(p1.age)

p1.age = 300

# p1.setAge(-10)
# p1.setAge(199)
# p1.setAge("abc")

p1.age = 199

print(p1.age)

# p2 = Person(19)
# p3 = Person(20)
#
# p1.age = -10
# print(p1.age)
# print(p2.age)
# print(p3.age)