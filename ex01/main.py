class ObjectC(object):
    def __init__(self):
        return


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


def what_are_the_vars(*args, **kwargs):
    n_var = ""
    i = 0
    for value in kwargs:
        if value.startswith("var_") is True:
            return None
        setattr(obj, value, kwargs.get(value))
    for value in args:
        n_var = "var_" + str(i)
        setattr(obj, n_var, value)
        i += 1
    return obj


if __name__ == "__main__":
    obj = ObjectC()
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
