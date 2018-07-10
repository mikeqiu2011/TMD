# class Person(object):
#     """
#     this is a Person
#     hihihi
#     """
#     age = 19
#
#     def __init__(self):
#         self.name = "sz"
#
#     def run(self):
#         print("run")
#
#     pass
#
# # print(Person.__dict__)
# # print(Person.__bases__)
# # print(Person.__doc__)
#
# # help(Person )
# # print(Person.__name__)
# # print(Person.__module__)
#
# p_xxx = Person()
# print(p_xxx.__class__)


class Person:
    __age = 10

    def __run(self):
        print("run")


p = Person()
# p_xxx.__run()
# p_xxx._Person__run()

print(p.__dict__)
print(Person.__dict__)