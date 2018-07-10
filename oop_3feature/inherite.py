# # # # class Animal:
# # # #     pass
# # # #
# # # # class xxx:
# # # #     pass
# # # #
# # # # class Dog(Animal, xxx):
# # # #     pass
# # # #
# # # #
# # # # print(Dog.__bases__)
# # # # print(Animal.__bases__)
# # # # print(int.__bases__)
# # # # print(float.__bases__)
# # # # print(bool.__bases__)
# # # # print(str.__bases__)
# # #
# # # #inherit resource
# # #
# # # class Animal:
# # #     a = 1
# # #     _b =2
# # #     __c = 3
# # #
# # #     def t1(self):
# # #         print("t1")
# # #
# # #     def _t2(self):
# # #         print("t2")
# # #
# # #     def __t3(self):
# # #         print("t3")
# # #
# # #     def __init__(self):
# # #         print("init")
# # #
# # #
# # # class Person(Animal):
# # #     def test(self):
# # #         print(self.a)
# # #         print(self._b)
# # #         # print(self.__c)
# # #
# # #         self.t1()
# # #         self._t2()
# # #         # self.__t3()
# # #
# # #         self.__init__()
# # #
# # # p = Person()
# # # p.test()
# # # print(id(Animal.a))
# # # Animal.a = 666
# # # print(id(Animal.a))
# # #
# # # p.test()
# # #
# #
# # #resource access order
# #
# # # class C:
# # #     # age = "c"
# # #     pass
# # #
# # # class B(C):
# # #     # age = "b"
# # #     pass
# # #
# # # class A(B):
# # #     # age = "a"
# # #     pass
# # #
# # # print(A.age)
# # import inspect
# #
# #
# # class C:
# #     # age = "c"
# #     pass
# #
# # class B(C):
# #     # age = "b"
# #     pass
# #
# # class E:
# #     age = "e"
# #     pass
# #
# # class D(E):
# #     age = "d"
# #     pass
# #
# #
# #
# # class A(B,D):
# #     # age = "a"
# #     pass
# #
# #
# # print(A.age)
# #
# # print(inspect.getmro(A))
# # print(A.mro())
# # print(A.__mro__)
#
# # self and class in inheritage
# #
# # class B:
# #     def test1(self):
# #         print(self)
# #     @classmethod
# #     def test2(cls):
# #         print(cls)
# #
# # class A(B):
# #     pass
# #
# # a = A()
# # a.test1()
# # a.test2()
#
#
# #resource access in obj inheritage
#
# class B:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#
#     def test1(self):
#         print("test1")
#
#     @classmethod
#     def test2(cls):
#         print("test2")
#
#     @staticmethod
#     def test3():
#         print("test3")
#
# class A(B):
#     a = 2
#
#     def __init__(self):
#         # super(A, self).__init__()
#         # B.__init__(self)
#         super().__init__()
#         self.c = 3
#
#     def test1(self):
#         # super().test1()
#         print("A.test1")
#     pass
#
#
#
# # print(A.a)
# a = A()
# print(a.__dict__)
# a.test1()
# # print(a.b)
# # print(a.c)
# #
# # a.test1()
# # a.test2()
# # a.test3()

class D:
    def __init__(self):
        print("d")

class B(D):
    def __init__(self):
        super().__init__()
        print("b")

class C(D):
    def __init__(self):
        super().__init__()
        print("c")

class A(B,C):
    def __init__(self):
        # super().__init__()
        B.__init__(self)
        C.__init__(self)
        print("a")

A()