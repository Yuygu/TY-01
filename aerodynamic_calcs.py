import math

# Constants
air_density = 1.225  # kg/m^3, standard air density at sea level
gravity = 9.81  # m/s^2

# Rocket cone parameters (adjustable)
diameter = 0.1  # meters
velocity = 100  # m/s, estimated velocity
drag_coefficient = 0.5  # typical for cone shape
cone_length = 0.5  # meters
mass = 2  # kg, estimated mass of the rocket

# Calculating cross-sectional area of the cone
area = math.pi * (diameter / 2) ** 2  # m^2

# Drag force calculation
drag_force = 0.5 * air_density * area * drag_coefficient * velocity ** 2

# Weight force (gravity)
weight_force = mass * gravity

# Lift-to-Drag Ratio (L/D Ratio)
# For simplicity, we assume lift = 0 for now, but you can expand with a lift component.
lift_force = 0  # Modify if lift calculation is included
lift_to_drag_ratio = lift_force / drag_force if drag_force != 0 else 0

# Output the results
print("Rocket Cone Aerodynamic Calculations")
print(f"Cross-sectional Area: {area:.4f} m^2")
print(f"Drag Force: {drag_force:.2f} N")
print(f"Weight Force: {weight_force:.2f} N")
print(f"Lift-to-Drag Ratio: {lift_to_drag_ratio:.2f}")

# Notes:
# Adjust the parameters like velocity, drag coefficient, etc., for specific testing.
