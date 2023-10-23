
# 1. lambda function:

# syntax:        lambda arguments : expression   

'''lamda function in python is a small anonymous function that can have any number of arguments
 but can take only one expression
 
 - it is used for short and simple operations'''

# 2. list comprehension:

# syntax        [exp for item in iterable if condition]

'''they allow you to create new lists by applying an expression for each item in an existing iterable and
optionally filtering the items based on a condition 

- they are more declarative than loops and are easy to read and understand
- they are used few scenarios like mapping and filtering'''

# 3. Generators:

''' syntax        def gen_func():
                    yield statement'''

'''generator func in python is defined like a normal function but when it needs to generate a value
then it does with the yield keyword rather than return

- if the body of the function contains yield then the function automatically becomes a generator function'''

# Decorators:

'''syntax:          def decorator_func():
                        wrapper_func()
                            statement/code
                        return wrapper_func
                        
                    @decorator_func
                        def my_func()
                            func code here'''

'''they are used to enhance the behaviour of the functions/methods without changing their code

- they are essentially funtions that add functionality to an existing function in python
without changing the structure of the function itself

- decorators are often used for logging, authentication, access control and more'''