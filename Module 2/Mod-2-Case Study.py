"""
    Author: Samantha Harper
    Date: 01/22/2025
    File: Mod-2-Case Study
    Description: This program will take the name of a student and gpa. 
    Then the program determines if they are honor roll, dean's list, or neither
"""
    
# constant variables
deans_list: float = 3.5
honor_roll: float = 3.25
exit_value: str = 'ZZZ'

# additional variables for input 
GPA: float = 0.0
first_name: str = " "
last_name: str = " "

#start loop for input
while last_name != exit_value:
    
    # ask for last name of student
    last_name = input("Enter student's last name (ZZZ to quit): ")
    
    #check if last name equals sentinel value to end loop
    if last_name == exit_value:
        break
    
    # ask for first name of student
    first_name = input("Enter student's first name: ")
    
    #ask for GPA of student
    GPA = input("Enter student's GPA: ")
    
    #convert GPA from sting to float
    try: 
        GPA = float(GPA)
    except ValueError:
        print("Invalid GPA. Please enter a number.")
        continue
    
    #if statements to determine if the student is Dean's List or Honor Roll
    if GPA >= deans_list:
        print(f"{last_name}, {first_name}, Dean's List!")
        
    elif GPA >= honor_roll:
        print(f"{last_name}, {first_name}, Honor Roll!")
    
    else:
        print(f"{last_name}, {first_name}, Needs Improvement")