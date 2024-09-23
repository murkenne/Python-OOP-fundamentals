'''
1. City Infrastructure Management System
Objective: The aim of this assignment is to apply the concepts of Object-Oriented Programming in 
Python to build a simulated City Infrastructure Management System. 
This system will incorporate classes, objects, methods, and data structures to manage different 
aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System

- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner.
Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
'''


class Vehicle:
    def __init__(self, registration_number, type, owner):
        self.registration_number = registration_number
        self.type = type
        self.owner = owner

        
        
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to {new_owner} ")
        
    def show_info(self):
        return (f"Registration Number: {self.registration_number}, Type: {self.type}, Owner: {self.owner}")
        
        
# Creating an instance of the Vehicle class  
vehicle_1 = Vehicle(34344, "Tahoe", "Mugzy Bowles")

 # Printing the type of vehicle
print(vehicle_1.show_info())


# Updating the owner of the vehicle
vehicle_1.update_owner("John Doe")


print(vehicle_1.show_info())
