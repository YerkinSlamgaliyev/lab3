import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius = float(input("Enter the radius: "))

volume = sphere_volume(radius)

print(f"Volume of the sphere is {volume:.2f}")