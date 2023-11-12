
# polymorpshism >> taking many forms

'''
It is of 4 types:

    - duck typing
    - operator overloading
    - method overloading
    - method overriding

'''
# <<<<<<<<<<<<< duck typing: >>>>>>>>>>>>>>>>>>>>>>>>

'''under progress'''

# <<<<<<<<<<<<< operator Overloading: >>>>>>>>>>>>>>>>>>>>>>>>

'''under progress'''

# <<<<<<<<<<<<< Method Overloading: >>>>>>>>>>>>>>>>>>>>>>>>

# also known as Compile time polymorphism
# (Note: by default method overloading is not possible in python but there are other ways to achieve this)

''' If a class consists of two or more methods with the same name but different parameters then it is called method overloading.
'''

# example:

class Overloading:
    def add(self,a,b):      # methods with same name "add"
        return a+b
    def add(self,a,b,c):    # but different parameters
        return a+b+c
    
# o = Overloading()
# print(o.add(1,2))
# print(o.add(1,2,3))     # gives "TypeError: add() missing 1 required positional argument: 'c' " 

# << we can overcome this in different ways >>
# 1. using default argument

class MOverloading:
    def add(self,a,b,c=0):    # making c=0 a default argument
        return a+b+c
    
o = MOverloading()
print("using default argument:\n",o.add(1,2))
print(o.add(1,2,3))     # which gives 3 and 6

# 2.we can also use variable length argument (*args)

class MOverloading1:
    def add(self,*args):
        total = 0
        for i in args:
            total=total+i
        return total
    
o = MOverloading1()
print("using args:\n",o.add(1,2))
print(o.add(1,2,3))

# <<<<<<<<<<<<< Method Overriding: >>>>>>>>>>>>>>>>>>>>>>>>

# also known as Run time polymorphism

'''
when the same method name with same no: parameters are present in both parent and child class (i.e.,different classes) then it is called method overriding.
'''

class dad:
    def arrival(self):
        print("comes home by 9pm daily")
    def sleep_time(self):
        print("sleeps from 10pm to 5am")

class son(dad):                 # child class has same methods and same n0: parameters but has its own properties
    def arrival(self):
        print("unknown")        # overriding the fathers property
    def sleep_time(self):
        print("no perfect timing")
        super().sleep_time()       # by this way we can also inherit the father's sleeptime


sunny=son()
sunny.sleep_time()


# <<<<<<<< Differences between overloading and overriding >>>>>>>>>>>>>>
'''
        overloading                                         overriding

1.  occurs within the same class                - occurs in two or more classes (mostly in inheritance)

2.  must have same method name & diff           - method must have same name and same no: parameters
    no: parameters

3.  python by default does not support over-    - python supports over riding
    loading but it can be achieved by using
    default arguments/*args
'''