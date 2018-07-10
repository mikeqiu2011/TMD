import abc


class Animal(object, metaclass=abc.ABCMeta):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):
        print("%s playing" % self)
        pass

    def eat(self):
        print( "%s eating" % self)
        pass

    def sleep(self):
        print( "{} sleeping".format(self))
        pass

    @abc.abstractmethod
    def work(self):
        pass


class Dog(Animal):
    def __str__(self):
        return "a dog named {} aged {} is".format(self.name, self.age)

    def work(self):
        print(self, "door watching")


class Cat(Animal):
    def __str__(self):
        return "a cat named {} aged {} is".format(self.name, self.age)

    def work(self):
        print(self, "mouse catching")


class Person(Animal):
    def __init__(self, name, pets=[], age=1):
        super().__init__(name, age)
        self.pets = pets

    def __str__(self):
        return "a person named {} aged {} is".format(self.name, self.age)

    def work(self):
        print("person is working")
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()

    def makepetswork(self):
        for pet in self.pets:
            pet.work()


d = Dog("xiaobao", 10)
d.play()
d.sleep()
d.eat()
d.work()

print("#" * 100)

c = Cat("miaomiao", 5)
c.play()
c.sleep()
c.eat()
c.work()

print("#" * 100)

p = Person("mike",[d, c], 35)
p.play()
p.sleep()
p.eat()
print("#" * 100)

p.work()
p.makepetswork()
