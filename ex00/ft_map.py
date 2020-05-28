def ft_map(fct, lst):
    if isinstance(lst, list) is False\
        and isinstance(lst, str) is False\
            and isinstance(lst, dict) is False\
            and isinstance(lst, tuple) is False\
            and isinstance(lst, set) is False:
            print("Can't iterate on", type(lst), "type")
            exit(1)
    ret = []
    for e in lst:
        ret.append(fct(e))
    return ret
