#   <<<<<<<< Inheritance >>>>>>>>>>>>>

'''
        it allows you to create a new class that inherits the attributes and methods from an existing class.
        - it promotes code re-useability

        new class is called >> derived class, sub class, child class
        existing class is called >> base class, super class, parent class

        ex: class BaseClass:
                def .........
            class SubClass(BaseClass):
                def ........
'''

# inheritance is of 4 types:

# Single Inheritance: a class that inherits only from one base class

class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
dog = Dog()
print(dog.speak())

# multiple inheritance: a class that inherits from more than one base class

class Engine:
    def start(self):
        return "engine started"
class Electric():
    def charge(self):
        return "battery charged"
class Car(Engine, Electric):        # inheriting from more that one base class
    def drive(self):
        return "car is driving"

my_car = Car()
print(my_car.start())
print(my_car.charge())
print(my_car.drive())

'''
        in multiple inheritance we have a concept called MRO which is 
        Method Resolution Order:
                it is a mechanism to determine the order in which classes are searched when looking for a method/attribute of an object.
                - It ensures a consistent and predictable method resolution order for your classes.

        NOTE:  MRO is used to avoid ambiguity and to determine which class's method will be called when there are name conflicts
'''

# example of MRO

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())  # You can access the MRO of a class by using the mro() method or the __mro__ attribute

# Multi-level inheritance: a class inherits from other class which intern inherits from another class.

'''
        class X:
            pass
        class Y(X):
            pass
        class Z(Y):
            pass
'''

# Hierarchical Inheritance:  multiple derived classes inherit from a single base class

'''
    class A:
        pass
    class B(A):
        pass
    class C(A):
        pass
    class D(A):
        pass
'''