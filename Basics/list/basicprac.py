
# ******list beginner basics*******

'''ABOUT LISTS:
- comes under sequence data type
- declared with square brackets and seperated by commas
- they are mutable and duplicates are allowed
- they may contain DataTypes like Integers, Strings, as well as Objects
'''
#**********************************************
lst = [10,"programmar", 2.5]  # allow different datatypes
lst2 = [10,20,30,20]   # allow duplicates
print("allowes duplicates: ", lst)
print("allows duplicates: ", lst2)
print("accessing elements using index: ",lst2[2])

lst3 = [[1,2,3],40,50]  # multi dimensional list
print("accessing elements from a multidimensional list:", lst3[0][1])

lst4 = [11,22,33,44,55,66,77]
print("negative indexing: ", lst4[-1])
print("length: ",len(lst4))

#**********************************************
# user input
ls = list(input("Enter the elements: "))
print("creating list from user input: ",ls) # creating list from user input

string = input("Enter the elements: ")
lst5 = string.split()       # import list as string
print("list is:", lst5)

#**********************************************
a = []
print(a.append(1))  # appending elements to list
print(a.append(3))
print(a.append(5))
print(a)

