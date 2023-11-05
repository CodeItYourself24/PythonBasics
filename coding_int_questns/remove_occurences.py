'''Remove all the occurrences of an element from a list'''

# using list comprehension

ls = [5, 20, 15, 20, 25, 50, 20]

new_ls = [i for i in ls if i!=20]
print("rem occ using list comp: ",new_ls)

# def list comp in a func

def new_ls1(ls,val):
    nl = [i for i in ls if i!=val]
    return nl
print("using list comp in func: ",new_ls1(ls,20))

# using enumerate func

