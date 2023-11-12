# <<<<<<<<<<<<<<<< Threading >>>>>>>>>>>>>>

'''
    Python provides a built-in module called threading to work with threads.

    It is all about executing several tasks simultaneously where each task is a seperate independent part of the same program,
        here each independent part is called thread.
    
    - thread class methods: ex: run(), start() etc.
    - every program consists one 'main' thread which executes the python program
    
    >> Main advantage of multitasking is to improve the performance of the system and reducing the response time.
'''

# EXAMPLE for multi threading in python

import threading
import time

print("<<<<< example of multithreading starts here >>>>>>>")
def print_numbers():
    for i in range(5):
        print(f"first thread: {i}")
        time.sleep(1)

def print_letters():
    for l in 'abcde':
        print(f"second thread: {l}")
        time.sleep(1)

# t1 and t2 are threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# This starts both threads, allowing them to run concurrently.
t1.start()
t2.start()

# The join() method is used to wait for a thread to finish its execution
t1.join()
t2.join()
print("Both threads are finished")

'''
gives o/p as: (o/p is random in order)

first thread: 0
second thread: a
first thread: 1
second thread: b
second thread: c
first thread: 2
second thread: d
first thread: 3
second thread: e
first thread: 4
Both threads are finished
'''

#*********** GIL (Global Interpretor Lock) ***************************

'''
    It is a type of process lock whenever it deals with processes.

        - The performance of the single-threaded process & the multi-threaded process will be the same in Python & this is because of GIL in Python.

        - We can not achieve multithreading in Python because we have a GIL that restricts the threads & works as a single thread.
'''


# <<<<<<<< lambda function: >>>>>>>>>>>>>>>>>>>

# syntax:        lambda arguments : expression   

'''lamda function in python is a small anonymous function that can have any number of arguments
 but can take only one expression
 
 - it is used for short and simple operations'''

# example: lambda function to add two numbers

add_num = lambda x,y : x + y
res = add_num(9,11)
print(f"sum of two numbers using lambda: {res}")

# gives o/p as >>       sum of two numbers using lambda: 20

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

# example: basic generator function

print("<<<<< example of generator starts here >>>>>>>")

def num_gen(n):
    for i in range(n):
        yield i

gen = num_gen(5)    # creating generator object
for num in gen:     # iterating through the generator
    print(num)

'''
gives o/p as:

0
1
2
3
4
'''

'''
    Adavantages:: 
        - Generators are Memory Efficient because they don't store the entire sequence in memory; they produce values on-the-fly as needed.
        - Lazy Evaluation: Generators use lazy evaluation, meaning they generate values one at a time when requested.
        - Performance: Generators can improve performance in cases where you don't need all the values at once.
'''

# Decorators:

'''they are used to enhance the behaviour of the functions/methods without changing their code.

- decorators are often used for logging, authentication, access control and more

- Another def >> they are essentially funtions that add functionality to an existing function in python
without changing the structure of the function itself.'''

'''syntax:          def decorator_func():
                        wrapper_func()
                            statement/code
                        return wrapper_func
                        
                    @decorator_func
                        def my_func()
                            func code here'''