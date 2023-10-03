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


# # for x in (o:=sub_gen()):
# print([o for o in sub_gen()])
from pathlib import Path
import re


def get_all_words(text):
    for word in re.findall(r"\w+", text):
        yield word


cur_file = Path("book.ipynb")
print(cur_file)
with open(cur_file, "r") as f:
    for word in get_all_words(f.read()):
        print(word)


# %%
from collections import deque


# %%
def DFS_classes(cls):
    visited = set()

    def traversal(cls, depth):
        cur = cls
        yield cur, depth
        for sub_cls in cur.__subclasses__():
            if sub_cls not in visited:
                visited.add(sub_cls)
                yield from traversal(sub_cls, depth + 1)

    return traversal(cls, 0)


def DFS_iter(cls):
    fringe = [(cls, int(0))]
    visited = set()
    while fringe:
        cur, depth = fringe.pop(0)
        yield cur, depth
        for sub_cls in cur.__subclasses__():
            if sub_cls not in visited:
                visited.add(sub_cls)
                fringe.append((sub_cls, depth + 1))


def BFS_classes(cls):
    queue = deque([(cls, 0)])
    while queue:
        cls, depth = queue.popleft()
        yield cls, depth
        for sub_cls in cls.__subclasses__():
            queue.append((sub_cls, depth + 1))


def tree(cls):
    def sub_tree(cls):
        for sub_cls in cls.__subclasses__():
            yield sub_cls.__name__, 1

    yield cls.__name__, 0
    yield from sub_tree(cls)

if __name__ == "__main__":
    display(Exception, DFS_iter)
