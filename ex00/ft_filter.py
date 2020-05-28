def ft_filter(fct, lst):
    if isinstance(lst, list) is False\
        and isinstance(lst, str) is False\
            and isinstance(lst, dict) is False\
            and isinstance(lst, tuple) is False\
            and isinstance(lst, set) is False:
            print("Can't iterate on", type(lst), "type")
            exit(1)
    ret = []
    for e in lst:
        if fct(e) is True:
            ret.append(e)
    return ret
