import string
from functools import reduce
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce


# Test with list, dict, set, tuple
def addition(n):
    return n + n


def s_addition(n, a):
    return n + a


def ft_is_greater(n):
    return n > 5


tst = [2, 4, 8]
haha = {
    "salut": "hello",
    "goodbye": "ciao",
    "merci": "danke",
}
a = ft_map(addition, tst)
a1 = map(addition, tst)
print("ft_map A")
for e in a:
    print(e, "|", end='')
print("\nmap A1")
for e in a1:
    print(e, "|", end='')
b = ft_map(addition, haha)
b1 = map(addition, haha)
print("\n\nft_map B")
for e in b:
    print(e, "|", end='')
print("\nmap B1")
for e in b1:
    print(e, "|", end='')
c = ft_map(addition, "hello")
c1 = map(addition, "hello")
print("\n\nft_map C")
for e in c:
    print(e, "|", end='')
print("\nmap C1")
for e in c1:
    print(e, "|", end='')
print("")
tpl = (1, 4, 6)
d = ft_map(addition, tpl)
print("\n\nft_map D")
for e in d:
    print(e, "|", end='')
d1 = map(addition, tpl)
print("\nmap D1")
for e in d1:
    print(e, "|", end='')
st = {2, 5, 9}
e = ft_map(addition, st)
print("\n\nft_map E")
for x in e:
    print(x, "|", end='')
print("\nmap E1")
e1 = map(addition, st)
for e in e1:
    print(e, "|", end='')

n_lst = [2, 9, 0, 29, 3, 5, 3, 7]
f = ft_filter(ft_is_greater, n_lst)
f1 = filter(ft_is_greater, n_lst)
print("\n\nFt_filter F")
for e in f:
    print(e, "", end='')
print("\nfilter F1")
for e in f1:
    print(e, "", end='')


g = ft_reduce(s_addition, n_lst)
g1 = reduce(s_addition, n_lst)
print("\n")
print(g)
print("")
print(g1)
a = ft_reduce(s_addition, tst)
a1 = reduce(s_addition, tst)
print("\n\nft_reduce A")
print(a, "&&", a1)
b = ft_reduce(s_addition, haha)
b1 = reduce(s_addition, haha)
print("\n\nft_reduce B")
print(b, "&&", b1)
c = ft_reduce(s_addition, "hello")
c1 = reduce(s_addition, "hello")
print("\n\nft_reduce C")
print(c, "&&", c1)
print("")
tpl = (1, 4, 6)
d = ft_reduce(s_addition, tpl)
print("\n\nft_reduce D")
d1 = map(addition, tpl)
print("\nmap D1")
print(d, "&&", d1)
st = {2, 5, 9}
e = ft_map(addition, st)
print("\n\nft_reduce E")
e1 = map(addition, st)
print(e, "&&", e1)
