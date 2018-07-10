import contextlib


@contextlib.contextmanager
def test():
    print("begin")
    yield "mikw"
    print("end")


with test() as t:
    print(t, "doing something")