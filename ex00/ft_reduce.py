def ft_reduce(fct, lst):
    if isinstance(lst, list) is False\
        and isinstance(lst, str) is False\
            and isinstance(lst, dict) is False\
            and isinstance(lst, tuple) is False\
            and isinstance(lst, set) is False:
            print("Can't iterate on", type(lst), "type")
            exit(1)
    ret = 0
    for a in lst:
        if isinstance(a, int):
            ret += a
        else:
            ret += len(a)
    return ret
