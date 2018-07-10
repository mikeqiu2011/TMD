# class Caculator:
#     @staticmethod
#     def isint(n):
#         if not isinstance(n,int):
#             raise TypeError("expected int value")
#
#     def __init__(self, init_value):
#         Caculator.isint(init_value)
#         self.__result = init_value
#
#     def add(self,value):
#         self.__result += value
#
#     def substract(self,value):
#         self.__result -= value
#
#     def multiply(self,value):
#         self.__result *= value
#
#     def getresult(self):
#         return self.__result
#
#
# # c = Caculator("hihi")
# c= Caculator(2)
# c.add(4)
# c.substract(5)
# c.multiply(5)
# print(c.getresult())
# c.__result =10
# print(c.__dict__)
# print(c.getresult())

# using decrorator

class Caculator:
    def echo_opr_gen(opr=""):
        def __echo_opr(func):
            def inner(self, num):
                print(opr, num)
                return func(self, num)
            return inner
        return __echo_opr

    def __check_number(func):
        def inner(self, num):
            if not isinstance(num, int):
                raise TypeError("int expected!")
            return func(self, num)
        return inner

    @__check_number
    @echo_opr_gen("init")
    def __init__(self, init_value):
        self.__result = init_value
        # return self

    @__check_number
    @echo_opr_gen("add")
    def add(self, value):
        self.__result += value
        return self

    @__check_number
    @echo_opr_gen("sub")
    def substract(self, value):
        self.__result -= value
        return self

    @__check_number
    @echo_opr_gen("multiply")
    def multiply(self, value):
        self.__result *= value
        return self

    @property
    def result(self):
        return self.__result




# c = Caculator(2).add(4).substract(3).multiply(6)
# # c.add(4)
# # c.substract(3)
# # c.multiply(6)
# print(c.result)
