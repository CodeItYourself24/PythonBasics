'''
Enumerate function: 

            it is a built in function that allows you to loop over a sequence (list,tuple,string) to get the index and the value of each element in the sequence at the same time.
'''


marks = [75,62,54,88,91]

# for index, item in enumerate(iterable):
for index, m in enumerate(marks):
    print(f"Index {index}: {m}")


'''
Map function: 

        it helps you to apply a function to a sequence of elements (i.e., to each element in the sequence) and returns a new sequence. 
        - these functions are known as higher order functions, as they take functions as arguments.

        - a sequence can be list, tuple or any other iterable object.

        syntax:     map(function, iterable)
'''

# example:

def cube(x):
    return x*x*x

l = [1,2,3,4,5]
newl = list(map(cube,l))        # it takes the func as an argument and iterates through the list
print("basic example for map func: ",newl)

# using a lambda for the above instead of using a func

l1 = [2,5,8,10,14,25]
newl1 = list(map(lambda x:x*x*x, l1))
print("using map and lambda: ", newl1)


'''
Filter function: 

            it filters a sequence of elements based on a give predicate (a function that returns a boolean value) and returns the values that are true.

            syntax:     filter(predicate,iterable)
'''

newf = list(filter(lambda x: x > 500,newl1))
print("using filter with lambda: ", newf)


'''
Reduce: 

            it applies a function to a sequence and returns a single value.

            - the function argument takes two arguments and returns a single value

            - the reduce func applies the func to the first two elements in the sequence/iterable and applies the result to the next element. 

            syntax:     reduce(function, iterable)
'''

# example:

from functools import reduce
l2 = [512, 1000, 2744, 15625]
newr = reduce(lambda x,y:x+y, l2)
print("reduce using lambda: ",newr)