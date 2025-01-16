# SDEV 220 Python Class Notes 1.13.25

"""

Author: Sammi Harper
Assignment: Module 1 Numbers

"""


#adding a function
def is_odd(v: int) -> bool:
    #documentation for functions
    """determines whether v is odd or not
    
    args: 
        v (int): the integer to check if odd or not
        
    Reference:
        bool: true if odd, otherwise false
    """
    
    pass
    return True

# creating a mulitple line string using triple quotation marks aka doc strings
my_s: str = """
line 1
line 2
line 3
"""
print(my_s)


my_int: int = 5 #this is an integer
print(type(my_int))
fname: str = "Sammi"
my_int = "Sam" #we rewrote the variable as a string
print(type(my_int))


# tuple and parathesis cannot change AKA immutable
tpl: tuple =(1, 2, 3)
print(tpl)
#tuples start counting from 0 in position
print(tpl[0])
# for loop to print each item in tuple on different lines
for itm in tpl:
    print(itm)


#list square brackets can shange values AKA mutable values
lst: list = [1.0, 2.0, 3.0]
print(lst)
#lists count from 0 in position
print(lst[1])
#print last item in list
print(lst[-1])

# for loop to print each item in list on different lines
for itm in lst:
    print(itm)


# dictionary of key value pairs use curly brackets, quotes around key and value unless int then no quotes
mydic: dict = {
    # key on left value on right -- key must be unique -- values can repeat
    "first_name": "Sammi", 
    "last_name": "Harper", 
    "age" : 31
    }

print(mydic["first_name"])

# for loop to print each item in doctionary on different lines
for itm in mydic:
    print(itm)






