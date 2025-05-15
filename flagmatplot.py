import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.axis('off')

# Parameters for flag
flag_height = 3
flag_width = 6
top = 1
left = 1
wave_amplitude = 0.1
wave_frequency = 5 * np.pi / flag_height

# Meshgrid
x = np.linspace(0, flag_width, 300)
y = np.linspace(0, flag_height, 200)
X, Y = np.meshgrid(x, y)

# Animation function
def update(time):
    ax.clear()
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # Waving green background
    Z = wave_amplitude * np.sin(wave_frequency * Y + time)
    ax.contourf(X + Z + left, Y + top, np.ones_like(Z), levels=1, colors=['#006a4e'])

    # Waving red circle
    center_x = left + flag_width / 2 + wave_amplitude * np.sin(time + 2)
    center_y = top + flag_height / 2
    circle = Circle((center_x, center_y), 0.6, color='#f42a41')
    ax.add_patch(circle)

# Create and show animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 60), interval=50)
plt.show()
