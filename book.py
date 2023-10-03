import numpy as np

my_arr = np.arange(1_000_000)

my_list = list(range(1_000_000))
import numpy as np

np.dtype(np.int16)


# %timeit my_arr2 = my_arr * 2
# %timeit my_list2 = [x * 2 for x in my_list]

# %%
import re

m = re.search("(?<=abc)def", "abcdef")
m1 = re.search("(abc)def", "abcdef")

if m and m1:
    for g1 in m1.groups():
        print(g1)


# %%
def sub_gen():
    yield 1.1
    yield 1.2
    return "Done!"


def gen():
    yield 1
    yield from sub_gen()
    # print('<--', result)
    yield 2


