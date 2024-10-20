import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, N(m/kg)^2
M_E = 5.972e24  # Mass of Earth, kg
R_E = 6.371e6  # Radius of Earth, meters


# Function to calculate work done
def calculate_work(G, M_E, R_E, h, m):
    r0 = R_E
    r = R_E + h
    W = G * M_E * m * (1 / r0 - 1 / r)
    return W


# Accepting user input for altitude (h) and mass of rocket (m)
try:
    h = float(input("Enter the altitude of the orbit in meters (e.g., 300000 for 300 km): "))
    m = float(input("Enter the mass of the rocket in kilograms: "))
except ValueError:
    print("Please enter valid numerical values for altitude and mass.")
    exit()

# Calculating the work done
work_done = calculate_work(G, M_E, R_E, h, m)
print(f"Work done by gravitational force: {work_done:.2e} Joules")

# Plotting the Earth and the rocket's orbit
fig, ax = plt.subplots()

# Earth
earth = plt.Circle((0, 0), R_E, color='b', alpha=0.5, label='Earth')

# Orbit path
theta = np.linspace(0, 2 * np.pi, 100)
x_orbit = (R_E + h) * np.cos(theta)
y_orbit = (R_E + h) * np.sin(theta)

# Initial position (on the surface of the Earth)
x_initial = R_E
y_initial = 0

# Final position (in orbit)
x_final = R_E + h
y_final = 0

# Plotting the Earth
ax.add_patch(earth)

# Plotting the orbit
ax.plot(x_orbit, y_orbit, 'r--', label='Orbit Path')

# Plotting the initial and final positions of the rocket
ax.plot([0, x_initial], [0, y_initial], 'ko', label='Initial Position (Surface)')
ax.plot([0, x_final], [0, y_final], 'go', label='Final Position (Orbit)')

# Setting the aspect ratio and limits
ax.set_aspect('equal')
ax.set_xlim(-1.2 * (R_E + h), 1.2 * (R_E + h))
ax.set_ylim(-1.2 * (R_E + h), 1.2 * (R_E + h))

# Adding labels and legend
ax.set_xlabel('Distance (meters)')
ax.set_ylabel('Distance (meters)')
ax.set_title('Rocket Orbit around Earth')
ax.legend()

# Show the plot
plt.show()
