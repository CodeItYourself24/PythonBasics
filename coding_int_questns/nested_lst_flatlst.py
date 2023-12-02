# converting a nested list to a flat list

nested_list= [[2, 4, 6, 8], [10, 12, 14], [16, 18, 20]]

# using list comprehension
inls = [element for inner_list in nested_list for element in inner_list]
print("making the inner list to a flat list",inls)

# using chain from iter tools
from itertools import chain
flat_list = list(chain.from_iterable(nested_list))
print("using chain from iter_tools: ",flat_list)     


# double nested list
nstd_list = [[2, 4, 6, 8], [10, 12, 14, [16, 18, 20]]]

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

flat_list = list(flatten(nstd_list))
print(flat_list)

# triple nested list
ns_list = [[2, 4, 6, 8,[10, 12, 14, [16, 18, 20]]]]
def flt(lst):
    for item in lst:
        if isinstance(item,list):
            if isinstance(item,list):
                yield from flt(item)
        else:
            yield item

fls = list(flt(ns_list))
print("triple nested list:",fls)
