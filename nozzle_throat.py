import math

# Constants
R_specific = 287  # J/(kg*K), specific gas constant for air (example; adjust for specific gas)
gamma = 1.4       # Ratio of specific heats (Cp/Cv) for air; adjust based on fuel

# Input parameters
chamber_pressure = 5e6    # Pa, combustion chamber pressure (example value; adjust as needed)
exit_pressure = 1e5       # Pa, ambient pressure (example value; adjust as needed)
chamber_temperature = 2500  # K, combustion temperature (example)

# Calculating the pressure ratio
pressure_ratio = exit_pressure / chamber_pressure

# Calculate Mach number at throat (isentropic flow condition for nozzle throat)
mach_throat = math.sqrt((2 / (gamma + 1)))

# Calculate throat area based on pressure ratio and Mach number
throat_area = (chamber_pressure / (R_specific * chamber_temperature)) * mach_throat / pressure_ratio

# Calculate throat diameter
throat_diameter = math.sqrt((4 * throat_area) / math.pi)

# Output the result
print("Nozzle Throat Calculations")
print(f"Throat Diameter: {throat_diameter:.4f} meters")

# Notes:
# Modify constants (R_specific, gamma) for specific fuel gases.
# Input values for chamber pressure, temperature, and exit pressure based on testing conditions.
