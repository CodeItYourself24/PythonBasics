

# Python by default does not support Abstraction but it can be achieve it using abc module

#           <<<<<<<< Abstraction >>>>>>>>>>>>>>

    # show the essential information and hiding the complex details/implementation from the user

'''
    - mainly focusses on what the object does instead of how it does
    - Abstraction can achieved by using abstract classes and abstract classes.
'''

#           <<<<<<<< Abstract Method >>>>>>>>>

'''
    - it has only declaration but no implementation.
    - can declared with "@abstractmethod" decorator
    - it is present in abc module (here abc >> abstract base class) 
'''

from abc import *
class AbsDemo(ABC):     # inherits from ABC class which is an abstract class
    @abstractmethod     # declaring abstract method
    def display(self):
        pass


# obj = AbsDemo()
# object instantiation is not possible for abstract class with abstract methods

class Demo(AbsDemo):    # concrete class inheriting the Abstract parent class above
    def display(self):
        print("this is an example for abstract method")

obj = Demo()    # obj instantiation is possible only for concrete classes
obj.display()

# NOTE: the child class/concrete class should implement all the methods of abstract class


