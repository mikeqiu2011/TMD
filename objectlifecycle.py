# class Person:
#     # def __new__(cls, *args, **kwargs):
#     #     print("new a instance")
#
#     def __init__(self):
#         self.name = "sz"
#
#     def __del__(self):
#         print("delete the instance")
#     pass
#
#
# p_xxx = Person()
# print(p_xxx.name)
# print(p_xxx)

# a sample of object life cycle
class Person:
    __count = 0

    def __init__(self):
        Person.__count += 1

    def __del__(self):
        Person.__count -= 1

    @classmethod
    def log(cls):
        print(cls.__count)

p1 = Person()
p2 = Person()

Person.log()

del p1
Person.log()

# print(Person.__count)
