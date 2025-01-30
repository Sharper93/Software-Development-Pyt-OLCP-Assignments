# Notes 1.29


from dataclasses import dataclass

"""
    OBJECTS! and CLASSES
    
    OOP - object oriented programming
    
    simple objects: class title() or class title without parenthesesis 
    
    to declare a new object within a class you call it with parathenesis
    
    ex --> c_cat = cat () 
    
    classes are defined with an upper case letter in the title
    
    anytime you want to define attributes within a class you must use the __init__ method with self. 
    If you do not it cannot be inherited
    
    methods are defined inside a function with the same name as the class
    
    methods are called with parathenesis and can take parameters
    
    when you create a self function it is called a memeber function
    
    all standard objects most likely will have __init__
    
    abstract classes and methods are defined as empty
    
    when you change in sub class the parent class does not get
    
    when you use mulitple inherits the first attribute is what it uses to inherit from if it is inheriting from two parent classes
    
    extra parent class is a pretty print to print all objects in a class --> prints as a dictionary
    ^^ is called a mixin class 
    
    Adding the decorator (@) in code is not common in projection coding
    
    
    diameter is a read only property
    
    Name Mangling for Privacy -- variable or functions start with two __ 
    It mangles it so that it doesnt have the name at run time
    
    for global scope inside a class it is self. functions
    
    Within a class definition, a preceding @classmethod decorator indicates that that 
    following function is a class method.
    
"""

# create a class for cats
class Cat:
    
    # objects may have attributes/properties defines a function
    #__init__ is used for implmentation 
    def __init__(self, age: float, name: str):
        self.age: float = age
        self.name: str = name

    # methods in a class are defined inside a function with the same name as the class
    def meow(self) -> str:
        sounds: str = "meow"
        
        return sounds




# specific kind of cat that inherits from the class cat
class Calico(Cat):
    # give super for function and an additional property
    def __init__(self, age, name, num_toes: int):
        super().__init__(age, name)
        self.num_toes: int = num_toes
        
        
    #override the sounds from cat
    def meow(self):
        return super().meow()


# define an object for cat
a = Cat(age=1.5, name="Barney")

# define an object for calico
b = Calico(age=3, name="Bob")

print(a.meow())

print(b.meow())




class A():
    count = 0 # class veriable -- all below functions have access to it
    def __init__(self):
        A.count += 1
        
    def exclaim(self):
        print("I'm an A!")
    
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")
        
        
# static method
class CoyoteWeapon(): # whatever you tell it to do it will do it the same every time
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

# when creating class methods the self key word is always the first character



# MAJIC METHODS 
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2): #__EQ__ IS A MAJIC METHOD
        return self.text.lower() == word2.text.lower()
    

#storere perfers this method 
#_str__(self):
#   return self.text

# magic methods are just peference 
# or you can use functions

"""
    A named tuple is a subclass of tuples with which you can access values by 
    name (with .name) as well as by position (with [ offset ]).
"""

# data classes!!! not in book storer talks about

@dataclass
class Frog: 
    age: int
    length: int
    

f = Frog()

#data class is a class that has properties 

print(f) # prints Frog(age=0, length=0)

# dataclasses means you do not have to initalize the properties if you dont want to -- it just knows

# using dataclasses.field() decorator to specify default values






# most popular python modules is PANDAS -- check it out..https://pypi.org/project/pandas/

# can us pandas to use data manipulation 

# pandas to allow limitations

@dataclass
class Dogs:
    # can define paramerter to specify a limit to something like age
    pass


# MODULES packages and goodies

# modules are like folders where you can put python files
# such as from random inport choice


# if you simply put import fact rather than being specific of what in fast .. it can cause program to run slower

# to make your code more efficient and easy to understand you can use import * from module_name

# module is like a libary of types and functions

# if you want to import everything but not have to type module the whole name, you can do import module as abrevation
# can separate things in module by comma 
# can also rename function name with from mofule import module name as new_name


"""
from sources import fast, advice

print("Let's go to", fast.pick())
print("Should we take out?", advice.give())

"""
    
# python virtual environment allows you to store all modules that you need 


