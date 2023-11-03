# find the largest number in a list

l = [10,40,11,55,34,20]

# using sort()
l.sort()            
print("largest number using sort: ",l[-1])

# using max() method
print("largest no: using max: ",max(l))


# without using built in functions (comparing numbers)
def max(ls):
    max=ls[0]
    for x in ls:
        if x>max:
            max=x
    return max

ls = [10, 20, 4, 45, 99]
print("largest number is: ",max(ls))


# using lambda function
lst = [20, 10, 20, 4, 100]
largest_num = max(lst,key=lambda x: int(x))
print("largest number using lambda: ",largest_num)