def tag(name):
    def decro(func):
        def inner(content):
            return "<{name}>{func}<{name}>".format(name=name,func=func(content))
            # return "<p>" + func(content) + "<p>"
        return inner
    return decro


@tag("b")
def test(content):
    return content


print(test("mike"))
