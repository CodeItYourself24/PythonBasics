
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

#**************** append() **********************
# adds one element at a time to the end of the list

a = []
a.append(1)  # appending elements to list
a.append(3)
a.append(5)
print(a)

# adding elements to the list
# using iterator
for i in range(91,94):
    a.append(i)
print("using an iterator:", a)

# adding tuple to a list
a.append(("its","tuple"))
print("adding tuple to a list:", a)

#**************** insert() **********************
# inserts an element based on the index given

inls = [11,22,33,44,55]
inls.insert(0,"its")
inls.insert(4,"insert")
print("use of insert method:", inls)

#**************** extend() **********************
# used to add multiple elements at the same time at the end of the list.

exls = ['pagani','suzuki']
exls.extend(['mazarati','BMW'])
print("using extend method:", exls)