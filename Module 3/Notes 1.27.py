# class notes 1.27

""" functions can have positional and main parameters 

positional parameters are values and have to be in order
key word arguments like key do not have to be in order
default values must be at the end 

*args are not required but can be multiple agrements in the same AKA KW args

only can use * syntax in definition

KWares AKA key work arguments (**) two astriskets

karges convert all arguements to their key value pairs

inner functions are only available when calling the outer function

lamada function are annoymous functions - basically a function to make something happen 
without calling another specially named function

range is a generater - can only be called once without resetting the generator

@ goes in front of decorators -- decorators can be called with the @ then add another fucnction to it

def document_it(func):
    function details
    
    return func.__doc__
    
@document_it

def add(a, b):
    return a + b


if doing global variables and want to modify them in a function - must use global.animal = namechange

unless you put global. in function in from of variable the global variables will be read only

__main__ 

if __name__ == '__main__':
    print(__name__)
    
# function with positional and keyword arguments

def greet(name, age, location="New York"):
    print(f"Hello, {name}! You are {age} years old. You are from {location}.")

greet("John", 30)
greet("Jane", 25, "Los Angeles")

# function with *args

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
    
    
    print(multiply(2, 3, 4, 5))
    
    # function with **kwargs
    
    def print_kwargs(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    
    print_kwargs(name="John", age=30, location="New York")
    
    # lambda function
    
    add_two = lambda x, y: x + y
    print(add_two(2, 3))
    
    # range function
    
    for num in range(5):
        print(num)
    
    # decorators
    
    def document_it(func):
        def wrapper_func(*args, **kwargs):
            print(f"Running function: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper_func
    
    @document_it
    def add(a, b):
        return a + b
    
    print(add(2, 3))
    
    # global variables
    
    animal = "dog"
    
    def change_global():
        global animal
        animal = "cat"
    
    change_global()
    print(animal)
    
    # __main__
    
    print(__name__)
    if __name__ == "__main__":
        print("This script is being run directly.")
    else:
        print("This script is being imported.")
        

Can create your own exception as it is a class

class CustomError(Exception):

    def __init__(self, message):
    
        self.message = message
        


"""


# defining generator function
def get_odds():
    
    """
    Yields odd numbers in range 0-9
    """

    # iterate through numbers 0-9
    for num in range(10):
        
        #if number is odd, yield it
        if num % 2 != 0:
            yield num
    
#calling generator function for use   
odd_number = get_odds()

#printing numbers in range
print("Odd Numbers: ")
for num in odd_number:
    print(num)


# reset the generator function
odd_number = get_odds()

#print third value from generator function using enumerate function. Break after printing third value.
for i, value in enumerate(odd_number, start=1):        
    
    if i == 3:
        print("The third value returned by get_odds() is: ", value)
        break