
def eat(food):
    print(1)
    print(2)
    print(food)


# eat("apple")


class Person:
    def eat(self):
        print("this is a instance method", self)

    @classmethod
    def leifangfa(cls):
        print("this is a class method",cls)

    @staticmethod
    def jingtaifangfa():
        print("this is a static method")




p = Person()
# print(Person.__dict__)

def run():
    print("run")

p.age = run
print(p.__dict__)

# p_xxx.eat()
# p_xxx.jingtaifangfa()
# p_xxx.leifangfa()

# Person.leifangfa()
# Person.jingtaifangfa()