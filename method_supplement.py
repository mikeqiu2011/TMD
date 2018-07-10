# # # class Person:
# # #     def __init__(self, age, name):
# # #         self.__age = age
# # #         self.__name = name
# # #
# # #     def __str__(self):
# # #         # return str(self.__age) + self.__name
# # #         # return "name is {}, age is {}".format(self.__name, self.__age)
# # #         return "name is %s, age is %s" % (self.__name, self.__age)
# # #
# # #     @property
# # #     def age(self):
# # #         return self.__age
# # #
# # #     @age.setter
# # #     def age(self, age):
# # #         self.__age = age
# # #
# # #     @property
# # #     def name(self):
# # #         return self.name
# # #
# # #     @name.setter
# # #     def name(self, name):
# # #         self.__name = name
# # #
# # #
# # # p1 = Person(30, "mike")
# # # p2 = Person(35, "fei")
# # # print(p1)
# # # print(p2)
# # #
# # # print("*" * 100)
# # #
# # # p1.name = "andrew"
# # # print(p1)
# # #
# # # p2.age = 50
# # # print(p2)
# #
# # # s = str(p1)
# # # print(s, type(s))
# #
# #
# # class Person:
# #     def __init__(self, age, name):
# #         self.__age = age
# #         self.__name = name
# #
# #     def __str__(self):
# #         return "name is %s, age is %s" % (self.__name, self.__age)
# #
# #     def __repr__(self):
# #         return "xxx"
# #
# #
# # p1 = Person(30, "mike")
# # p2 = Person(35, "fei")
# #
# # print(p1)
# # print(repr(p1))
#
# # import datetime
# #
# # t =  datetime.datetime.now()
# # print(t)
# # print(repr(t))
# #
# # tmp =  repr(t)
# # __result = eval(tmp)
# # print(__result)
#
# #---------------__call__ method--------
#
# # class Person:
# #     def __call__(self, *args, **kwargs):
# #         print("xxx", args, kwargs)
# #     pass
# #
# # p_xxx = Person()
# # p_xxx(123, "abc", name = "mike")
#
# # def createPen(p_color, p_type):
# #     print("created a {}, its color is {}".format(p_type,p_color))
# #
# # # createPen("pen", "red")
# # # createPen("pen", "pink")
# # # createPen("pen", "blue")
# #
# # import functools
# #
# # penFunc = functools.partial(createPen,p_type="pen")
# #
# # penFunc("red")
# # penFunc("pink")
# # penFunc("blue")
#
# # class PenFactory:
# #     def __init__(self,p_type):
# #         self.__p_type = p_type
# #
# #     def __call__(self, p_color):
# #         print("created a {}, its color is {}".format(self.__p_type, p_color))
# #
# #
# # gangbiF = PenFactory("Pen")
# # gangbiF("red")
# # gangbiF("blue")
# # gangbiF("yellow")
# #
# # qianbiF = PenFactory("pencil")
# # qianbiF("purple")
# # qianbiF("green")
# # qianbiF("black")
#
# class Person:
#     def __init__(self):
#         self.cache = {}
#
#     def __setitem__(self, key, value):
#         self.cache[key] = value
#         # print("setitem", key, value)
#
#     def __getitem__(self, item):
#         return self.cache[item]
#
#     def __delitem__(self, key):
#         del self.cache[key]
#
#
# p_xxx = Person()
# p_xxx["name"] = "sz"
#
# print(p_xxx["name"])
#
# del p_xxx["name"]
#
#
# print(p_xxx["name"])

# class Person:
#     def __init__(self):
#         self.item = [ x for x in range(1,10)]
#         print(self.item)
#
#     def __setitem__(self, key, value):
#         # print(key, value)
#         # print(key.start)
#         # print(key.stop)
#         # print(key.step)
#         # self.item[key] = value
#         self.item[key.start:key.stop:key.step] = value
#         pass
#
#     def __getitem__(self, item):
#         print("get item", item)
#         return self.item[item]
#         pass
#
#     def __delitem__(self, key):
#         print("del", key)
#         del self.item[key]
#         pass
#
#
# p_xxx = Person()
# p_xxx[0:5:2] = ["a", "b", "c"]
# print(p_xxx.item)
#
# print(p_xxx.item)
# del p_xxx[0:5:2]
#
# print(p_xxx.item)

# slice


# ------------comapre------------

# class Person:
#     def __init__(self, age, height):
#         self.age = age
#         self.height = height
#
#     def __eq__(self, other):
#         print(other)
#         if isinstance(other,Person):
#             return self.age == other.age
#
#     def __ne__(self, other):
#         pass
#
#     def __le__(self, other):
#         pass
#
#     def __gt__(self, other):
#         pass
#
#     def __ge__(self, other):
#         pass
#
#     def __lt__(self, other):
#         pass
#
#
#
# a1 = Person(20, "mike")
# a2 = Person(20, "henry")
#
# print(a1 == a2)
# print(a1 != a2)


###############for in################

# class Person:
#     def __init__(self, max):
#         # self.items = [x for x in range(0,10)]
#         self.iter = 1
#         self.max = max
#
#     # def __iter__(self):
#     #     # print(self)
#     #     return self.items
#
#     def __getitem__(self, item):
#         # print("item is ", item)
#         # return self.items[item]
#         self.iter += 1
#         if self.iter >= self.max:
#             raise StopIteration("xxxx")
#         else:
#             return self.iter
#
#
# person = Person(100)
#
# for p_xxx in person:
#     print(p_xxx)



##################descriptor##########3

# class Age:
#     def __get__(self, instance, owner):
#         print("get")
#         return instance.v
#
#     def __set__(self, instance, value):
#         # print("set", self, instance, value)
#         instance.v = value
#
#     def __del__(self):
#         print("delete")
#
# class Person:
#     age = Age()
#     # def __getattribute__(self, item):
#     #     print("xxx")
#
# p1 = Person()
# p2 = Person()
#
# p1.age = 18
# p2.age = 19
#
# print(p1.age)
# print(p2.age)

# def check(func):
#     def d():
#         print("before check")
#         func()
#         print("after check")
#     return d

class check:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("before")
        self.func()
        print("after")

@check
def test():
    print("test")

# test = check(test)

test()