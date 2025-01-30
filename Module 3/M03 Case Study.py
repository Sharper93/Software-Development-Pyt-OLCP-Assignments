"""
    Author: Samantha Harper
    Date: 01/30/2025
    File: M03 Case Study 
    Description: This program will create a Vehicle class and its subclasses Automobile. The program will ask the user for the
    vehicle type (car, truck, plane, boat, or broomsticker are acceptable), year, make, model, door (2 or 4), roof type(solid or sun),
    and then display the vehicle details. If any information inputed is not the correct data type, an error message is returned. 
"""

# Super Class Creation
class Vehicle:
    # initialize vehicle type attribute
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
    

# sub class of Vehicle Class
class Automobile(Vehicle):
    # creation of vehicle information objects
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        # initalize the attributes of automobile and call superclass
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        

# function to validate the user inputs
def validate_input(prompt, valid_values=None, valid_type=None, allow_alpha=True):
    while True:
        user_input = input(prompt)
        
        # Check if the input is in the correct type and within the valid range or values
        if valid_type:
            try:
                user_input = valid_type(user_input)
            except ValueError:
                print(f"Invalid input. Please enter a valid {valid_type.__name__}.")
                continue
        
        # validate against allowed values
        if valid_values and user_input not in valid_values:
            print(f"Invalid input. Please choose from {valid_values}.")
            continue
        
        # Check if the input is letters only if allow_alpha is True
        if valid_type == str and not allow_alpha and not user_input.isalpha():
            print("Invalid input. Please enter letters only.")
            continue
        
        return user_input


# Main function to run the program
def main():
    # Allowable vehicle types
    vehicle_types = ["car", "truck", "boat", "plane", "broomstick"]
    
    # get vehicle type and test if it is allowed
    vehicle_type = validate_input("Enter vehicle type: ", valid_values=vehicle_types)

    # Accept user input for all aditional objects and check if input is allowed through validation
    year = validate_input("Enter the year: ", valid_type=int)
    make = validate_input("Enter the make: ", valid_type=str, allow_alpha=False)
    model = validate_input("Enter the model: ", valid_type=str)
    doors = validate_input("Enter the number of doors (2 or 4): ", valid_values=[2, 4], valid_type=int)
    roof = validate_input("Enter the type of roof (solid or sun roof): ", valid_values=["solid", "sun roof"])

    # Create an instance of Automobile
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Output the data in an easy-to-read format
    print(f"\nVehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")

if __name__ == "__main__":
    main()
