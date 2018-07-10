
# class Money:
#     age = 18
#     __count = 1
#     num = 666
#
# # Money.__dict__ = {"sex": "male"}
# Money.__dict__["age"] = 20
# print(Money.age)
#
# print(Money.__dict__)

class Person:
    __slots__ = ["age"]
    pass

p1 = Person()
p1.age = 1
p1.num = 10

# p2 = Person()
# p2.a = 1
# p2.b =2