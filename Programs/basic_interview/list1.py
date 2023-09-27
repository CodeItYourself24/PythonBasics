
# <<<<<<<< average of a list in python:

ls = [4, 5, 1, 2]
total = sum(ls)        # using normal method
average = total/len(ls)
print("average using normal method: ", average)

# using a function
def avg(lst):
    if len(lst)==0:
        return None
    average = sum(lst)/len(lst)
    return average

ls = [11,22,33,44,55]
print("average using function:", avg(ls))

ls1 = [6,7,8,9]
avg = sum(ls1)/len(ls1) if len(ls1) > 0 else None
print("avg using list comprehension:", avg)

# <<<<<<<<< reversing a list:

ls2 = [4, 5, 6, 7, 8, 9]
reversed_lst = ls2[::-1]
print('reverse of a list using slicing: ', reversed_lst)

ls3 = [1,2,3,4,'strng']
ls3.reverse()
print('using reverse: ',ls3)

ls4 = [11,22,33,44]
print('using reversed: ', list(reversed(ls4)))

# <<<<<<<<<<<< converting string into list

strng = "converting string into list"

list_conv = list(strng)
print("str to list using list: ", list_conv)

lc = [i for i in strng]
print('using list comprehension: ', lc)

lc1 = "using the split method"
lcs = strng.split()
print("using split(): ", lcs)

# <<<<<<<<<<<<< converting tuple to list

tple = (1,2,3,4)

lst = list(tple)
print("using list: ", lst)

l = []
l2 = (4,5,6,7)
for i in l2:
    l.append(i)

print("using for loop:", l)

lc = [i for i in l2]
print("using list comprehension: ", lc)

upt = (10,20,30,40)
upl = [*upt]
print("using * unpacking:", upl)

# <<<<<< remove last element from the list

l = ["im", "new", "to", "coding"]
l.pop()
print("using pop():", l)

l1 = [99,88,77,66]
l1.remove(66)
print("using remove:", l1)


l2 = [13, 34, 36, 23, 15, 88]
print("using negative slicing:", str(l2[:-1]))

l3 = [1,2,3,4]
del l3[-1]
print("using delete: ", l3)