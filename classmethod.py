
class Person:
    @classmethod
    def leifangfa(cls):
        print("this is a class method", cls)


class A(Person):
    pass


A.leifangfa();