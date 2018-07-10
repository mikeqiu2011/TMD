# # # 1 / 0
# #
# # # "1" + 2
# #
#
# #
# # b = {"name": "mike", "age": 35}
# # print(b["name"])
# # # print(b["sex"])
# #
# # # int("abx")
# #
# # try:
# #     print(name)
# #     a = [1, 2]
# # except NameError:
# #     print("qingzixijiancha")
# # except
#
# try:
#     # 1/0
#     print(name)
#     # a = [1, 2]
#     # a[3]
#
# # except (NameError, ZeroDivisionError) as e:
# except Exception as e:
#     print("error", e)
#
# else:
#     print("ok")
# finally:
#     print("at last")
#
# a = 1
# b = 2
#
# a,b = b,a
# print(a)
# print(b)
#
# a = 1
# b = 2
# a,b = b,a+b
# print(a)
# print(b)

# with open("xxx.html", "rb") as f:
#
#     print(f.read())
# open
# class Test:
#     def __enter__(self):
#         print("enter")
#         return "xxx"
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(self, exc_type, exc_val, exc_tb)
#         print("exit")
#         return True
#
# with Test() as x:
#     print("body", x)
#     1/0

# import contextlib
#
# @contextlib.contextmanager
# def test():
#     print(1)
#     yield 1
#     print(2)
#
# with test() as x:
#     print(3, x)


# import contextlib
#
# @contextlib.contextmanager
# def ze():
#     print("begin")
#     try:
#         yield "xxx"
#     except ZeroDivisionError as e:
#         print("error", e)
#     print("end")
#
#
# x=1
# y=0
#
# with ze() as z:
#     print(z)
#     x/y
#
# with ze():
#     1/1

# with open("xxx") as f:
#     f.read()
# import contextlib
#
#
# class Test:
#     def t(self):
#         print("ttt")
#
#     def close1(self):
#         print("close")
#
#     # def __enter__(self):
#     #     print("enter")
#     #     return self
#     #
#     # def __exit__(self, exc_type, exc_val, exc_tb):
#     #     self.close()
#
#
# with contextlib.closing(Test()) as t:
#     t.t()

# with open("xxx.html", "r") as from_file:
#     with open("2.html", "w") as to_file:
#         content =  from_file.read()
#         to_file.write(content)

# with open("xxx.html", "r") as from_file, open("2.html", "w") as to_file:
#     content =  from_file.read()
#     to_file.write(content)\

class LessZero(Exception):
    def __init__(self,msg, ec):
        self.msg = msg
        self.ec = ec
    def __str__(self):
        return self.msg + str(self.ec)

def set_age(age):
    if 0 <= age <= 200:
        print("age is", age)
    else:
        raise LessZero("value not valid, must be between 0 and 200", 2)

try:
    set_age(-18)
except LessZero as ve:
    print("error", ve)


# set_age(18)
# set_age(201)




