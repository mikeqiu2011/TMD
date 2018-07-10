import abc

class Animal(object,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def bark(self):
        pass

class Dog(Animal):
    def bark(self):
        print("wangwang")

class Cat(Animal):
    def bark(self):
        print("miaomiao")

class Glass:
    pass

def test(obj):
    if not isinstance(obj, Animal):
        raise TypeError("must be animal")
    obj.bark()

Animal()

c = Cat()

test(c)

g = Glass()
test(g)