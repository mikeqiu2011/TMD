#
# # class Person(object):
# #     def __init__(self):
# #         __age = 18
# #
# #     def get_x(self):
# #         return self.__age
# #
# #     def set_x(self,value):
# #         self.__age = value
# #
# #     age = property(get_x,set_x)
# #
# #
# # p_xxx = Person()
# #
# # p_xxx.age = 10
# # print(p_xxx.age)
# # print(p_xxx.__dict__)
#
# # class Person(object):
# #     def __init__(self):
# #         self.__age = 18
# #
# #     @property
# #     def age(self):
# #         print("-"*10, "get age")
# #         return self.__age
# #
# #     @age.setter
# #     def age(self,value):
# #         print("-"*10, "set age")
# #         self.__age = value
# #
# #
# #
# # p_xxx = Person()
# # print(p_xxx.age)
# #
# # p_xxx.age = 10
# #
# # print(p_xxx.age)# class Person(object):
# # #     def __init__(self):
# # #         __age = 18
# # #
# # #     def get_x(self):
# # #         return self.__age
# # #
# # #     def set_x(self,value):
# # #         self.__age = value
# # #
# # #     age = property(get_x,set_x)
# # #
# # #
# # # p_xxx = Person()
# # #
# # # p_xxx.age = 10
#
# #--------------------classic---------------
#
# # class Person:
# #     def __init__(self):
# #         self.__age = 18
# #
# #     def get_x(self):
# #         print("get")
# #         return self.__age
# #
# #     def set_x(self,value):
# #         print("set")
# #         self.__age = value
# #
# #     age = property(get_x,set_x)
# #
# #
# # p_xxx = Person()
# #
# # # p_xxx.age = 10
# # # print p_xxx.age
# # #
# # p_xxx.age = 10
# # print p_xxx.age
# #
# # print(p_xxx.__dict__)
#
# class Person:
#     def __init__(self):
#         self.__age = 18
#
#     @property
#     def age(self):
#         print("get age")
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         print("set age")
#         if isinstance(value, int) and value in range(1,100):
#             self.__age = value
#         else:
#             print("value not valid")
#
#     pass
#
#
# p_xxx = Person()
# print p_xxx.age
#
# p_xxx.age = 10
# print(p_xxx.age)
#
# print p_xxx.__dict__

class Person:
    def __setattr__(self, key, value):
        print(key,value)

        if key == "age" and key in self.__dict__.keys():
            print("this is a readonly attribute")
        else:
            self.key = value
            # self.__dict__[key] = value


p1 = Person()

p1.age = 18
p1.height = 10

# print(p1.age)
print p1.__dict__

p1.age = 20