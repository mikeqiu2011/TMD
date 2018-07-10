
# colors = ["red","green","orange","white"]
#
# for i in range(0,len(colors)):
#     print("{}--->{}".format(i,colors[i]))
#
#
# for i, color in enumerate(colors):
#     print(i,color)
#
# print(': '.join(colors))

p = 'mike', 30, "IT"

# print(p)

# name, age, job = p
#
# print(name)
# print(age)
# print(job)

dick = {"name":"mike", "age":30, "job":"IT"}

# print(dick)

# for k in dick:
#     print("{}--->{}".format(k,dick[k]))
#
# for k, v in dick.items():
#     print(k,"--->",v)

def foo(value):
    value = 2
    print(value)

a = 1
foo(a)
print(a)


def bar(args):
    args.append(1)


b = []
print(b)
print(id(b))

bar(b)

print(b)
print(id(b))

