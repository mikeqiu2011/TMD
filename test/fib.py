
class fib:
    def __init__(self, n):
        self.pre = 0
        self.cur = 1
        self.n = n

    def __next__(self):
        if self.n > 0:
            value = self.cur
            self.cur = self.pre + self.cur
            self.pre = value
            self.n -= 1
            return value
        if self.n <= 0:
            raise StopIteration()

    def __iter__(self):
        return self

f = fib(10)
print(f)
print(id(f))
print(type(f))

# for i in f:
#     print(i)

print([i for i in f])

