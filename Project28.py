class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

radius = float(input("Enter the radius of the circle: "))

circle = Circle(radius)

print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")