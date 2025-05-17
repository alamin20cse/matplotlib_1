import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle, Circle

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')

# Car components
car_body = Rectangle((0, 0.5), 2, 0.5, color='blue')
car_top = Rectangle((0.4, 1), 1.2, 0.4, color='lightblue')
wheel1 = Circle((0.5, 0.4), 0.2, color='black')
wheel2 = Circle((1.5, 0.4), 0.2, color='black')

road=Rectangle((0,0),13,.5,color='gray')
ax.add_patch(road)

# Add components to the axis
ax.add_patch(car_body)
ax.add_patch(car_top)
ax.add_patch(wheel1)
ax.add_patch(wheel2)

# Update function for animation
def update(frame):
    dx = 0.1 * frame
    car_body.set_xy((dx, 0.5))
    car_top.set_xy((dx + 0.4, 1))
    wheel1.center = (dx + 0.5, 0.4)
    wheel2.center = (dx + 1.5, 0.4)
    return car_body, car_top, wheel1, wheel2

# Animate
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
