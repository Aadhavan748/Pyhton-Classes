class Dog:
    animal = "Dog"  # Class variable
    
    def __init__(self, breed, colour):
        self.breed = breed      # Instance variable
        self.colour = colour    # Instance variable
    
    def display_details(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
        print()

# Create two objects
dog1 = Dog("German Shepherd", "Black and Tan")
dog2 = Dog("Corgi", "Golden")

# Display details
print("Dog 1 Details:")
dog1.display_details()

print("Dog 2 Details:")
dog2.display_details()