
class Vehicle:
    """
    Represents a vehicle with shared color and individual speed.
    """

    color = "White"  # Class attribute

    def __init__(self, brand, speed):
        """
        Initialize a vehicle with its brand and speed.
        """
        self.brand = brand
        self.speed = speed

    def display_info(self):
        """
        Display vehicle information.
        """
        print(f"{self.brand} - Color: {self.color}, Speed: {self.speed}")


# Main program
print("===== Vehicle Information =====")

brand1 = input("Enter first vehicle brand: ")
speed1 = int(input("Enter first vehicle speed: "))

brand2 = input("Enter second vehicle brand: ")
speed2 = int(input("Enter second vehicle speed: "))

# Create two objects
v1 = Vehicle(brand1, speed1)
v2 = Vehicle(brand2, speed2)

# Display default shared color
print("\n--- Before Changing Class Attribute ---")
v1.display_info()
v2.display_info()

# Change class attribute
new_color = input("\nEnter a new shared color: ")
Vehicle.color = new_color

# Display updated shared color
print("\n--- After Changing Class Attribute ---")
v1.display_info()
v2.display_info()
