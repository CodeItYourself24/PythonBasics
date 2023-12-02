# converting a nested list to a flat list

nested_list= [[2, 4, 6, 8], [10, 12, 14], [16, 18, 20]]

# using list comprehension
flat_list = [element for inner_list in nested_list for element in inner_list]
print(f"nested to flat using list comprehension: {flat_list}")

# using chain in iter_tools
from itertools import chain
flt_list = list(chain.from_iterable(nested_list))
print(f"nested to flat using chain from iter_tools: {flt_list}")

print("*****************************************")
# double nested list
nstd_list = [[2, 4, 6, 8], [10, 12, 14, [16, 18, 20]]]

def flatten(l):
    for i in l:
        if isinstance(i,list):
            yield from flatten(i)
        else:
            yield i

flatten_list = list(flatten(nstd_list))
print(f"nested to flat using func, isinstance: {flatten_list}")

print("*****************************************")
# triple nested list
tnls = [[2, 4, 6, 8,[10, 12, 14, [16, 18, 20]]]]

def triple_flat(l):
    for i in l:
        if isinstance(i,list):
            if isinstance(i,list):
                yield from triple_flat(i)
        else:
            yield i

fls = list(triple_flat(tnls))
print(f"triple nested to flat using isinstance: {fls}")