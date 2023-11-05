''' removing duplicates from a list '''

# using set method
ls = [1, 5, 3, 6, 3, 5, 6, 1]

nls = list(set(ls))
print("rem duplicates using set methods: ", nls)

# using list comprehension

# [exp for item in iterable if condition]
res=[]
[res.append(x) for x in ls if x not in res]
print("using list comp: ",res)


# using list comp and enumerate
res1 = [i for n, i in enumerate(ls) if i not in ls[:n]]
print("using list comp and enumerate: ",res1)


'''print the duplicates and unique numbers in a seperate list'''

ls2 = [5, 3, 5, 2, 1, 6, 6, 4, 1, 3, 8, 9,5]
uls = []
dls = []
for i in ls2:
    if i not in uls:
        uls.append(i)
    else:
        dls.append(i)

print("list with no dup: ",uls)
print("duplicates: ",dls)


'''get the count of each duplicated element in a list'''

ls3 = [1, 1, 5, 7, 8, 3, 2, 8, 2, 4, 4, 9, 8, 5, 4, 3]

from collections import Counter
count_dict = dict(Counter(ls3))
print(f"count of each duplicated items using counter & dict: {count_dict}")


''''''