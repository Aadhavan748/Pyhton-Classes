import math

angle_deg = float(input("Enter an angle in degrees: "))
angle_rad = math.radians(angle_deg)

sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)

print("Trigonometric Values:")
print("sin(", angle_deg, ") =", sin_value)
print("cos(", angle_deg, ") =", cos_value)
print("tan(", angle_deg, ") =", tan_value)