
# <<<<<<<<<< Function annotations: >>>>>>>>>>>>>>>>>>>>

'''
    Function annotations (->) provide additional information about the expected types of function parameters and the return value.

    - they are not enforced by the Python interpreter
    - do not have any impact on the actual execution of the code.
    - serve as a form of documentation

    ex: def add(a: int, b: int) -> int:
            return a + b
'''

# <<<<<<<<<<<<<<< Pickling and Unpickling >>>>>>>>>>>>>

'''
        The Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using the dump function, this process is called pickling. 
        
        While the process of (reverse of this method) which is retrieving original Python objects from the stored string representation is called unpickling.
'''

# <<<<<<<<<<<< PIP (python installer package) >>>>>>>>>>>>>

'''
        PIP (Python Installer Package) which provides an interface to install various Python modules. 

        It is a command-line tool that can search for packages over the internet and install them without any user interaction.
'''

# <<<<<<<<<<<<< ZIP function >>>>>>>>>>>>>>>>

'''
the zip function is a built-in function that is used to combine multiple iterables (such as lists, tuples, or strings) element-wise into a single iterable. 

	- it creates an iterator that generates tuples (which contains the elements from the input iterables)

			ex; zip(iterable1, iterable2, ...)'''

# example: 
        
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "red"]

combined = zip(fruits, colors)  # Combining 'fruits' and 'colors' element-wise using zip

result = list(combined) # # Converting the zip iterator to a list of tuples
print(result)

# which gives the output as:	[('apple', 'red'), ('banana', 'yellow'), ('cherry', 'red')]