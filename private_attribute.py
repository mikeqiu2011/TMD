
class Animal:
    __x = 10
    def test(self):
        print(self.__x)
        print(Animal.__x)
    pass


print(Animal.__dict__)
print(Animal._Animal__x)


# class Dog(Animal):
#     def test2(self):
#         print(self.__x)
#         print(Animal.__x)
#     pass
#
# a =  Animal()
# a.test()
#
# d = Dog()
# d.test2()
#
# print(Animal.__x)
# print(Dog.__x)
#
# __all__ = ["__a"]
#
# __a = 666