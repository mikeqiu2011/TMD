# class Person:
#     pass
#
# p_xxx = Person()
# # print(p_xxx)
# # print(id(p_xxx))
# print(hex(id(p_xxx)))
#
# p2 = Person()
# print(hex(id(p2)))
#
# i = 1
# j = 1
#
# print(id(i))
# print(id(j))

# reference count

# import sys
# class Person:
#     pass
#
# p1 = Person()
# print(sys.getrefcount(p1))
# p2 = p1
# print(sys.getrefcount(p1))
# del p2
# print(sys.getrefcount(p1))
# del p1

# reference change senario

import sys


# class Person:
#     pass
#
# p_xxx = Person()
#
# print(sys.getrefcount(p_xxx))
#
# # def log(obj):
# #     print(sys.getrefcount(obj))
# #
# # log(p_xxx)
# #
# # for attr in dir(log):
# #     print(attr, getattr(log, attr))
#
# l = [p_xxx]
# print(sys.getrefcount(p_xxx))

# recursive reference

# import sys
# import objgraph
#
# class Person:
#     def __init__(self, pet=None):
#         self.pet = pet
#
#     def setPet(self, pet):
#         self.pet = pet
#
#     pass
#
#
# class Dog:
#     def __init__(self, master=None):
#         self.master = master
#
#     pass
#
#
# p = Person()
# d = Dog(p)
# p.setPet(d)
#
# print(objgraph.count("Person"))
# print(objgraph.count("Dog"))
#
# # print(sys.getrefcount(p))
# # print(sys.getrefcount(d))
#
# del p
# del d
#
# # print(sys.getrefcount(p))
# # print(sys.getrefcount(d))
# print("#"*100)
# print(objgraph.count("Person"))
# print(objgraph.count("Dog"))

# test gc

# import gc
#
# print(gc.get_threshold())
#
# gc.enable()
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())

#manual gc
import gc
import sys
import objgraph
import weakref
class Person:
    def __del__(self):
        print("Person obj has been deleted")
    pass

class Dog:
    def __del__(self):
        print("Dog obj has been deleted")
    pass

p = Person()
d = Dog()

p.pet = d
# d.master = weakref.ref(p)
d.master = p

# print(sys.getrefcount(p))
# print(sys.getrefcount(d))

p.pet = None
del p
del d

# gc.collect()

print(objgraph.count("Person"))
print(objgraph.count("Dog"))


