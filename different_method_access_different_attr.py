
class Person:
    age = 10
    def shilifangfa(self):
        print(self)
        print(self.age)
        print(self.num)

    @classmethod
    def leifengfa(cls):
        print(cls)
        print(cls.age)
        print(cls.num)

    @staticmethod
    def jingtaifangfa():
        pass


p = Person()
p.num = 20

p.shilifangfa()
p.leifengfa()