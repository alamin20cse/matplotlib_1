import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')

# Create and add a red rectangle
rt1 = Rectangle((1, 1), 6, 1, color='red')
rt2=Rectangle((3,1.5),2,1,color='blue')
cr1=Circle((2,1),0.5, color='black')
cr2=Circle((6,1),0.5,color='black')

ax.add_patch(rt1)
ax.add_patch(rt2)
ax.add_patch(cr1)
ax.add_patch(cr2)

def update(frame):
    dx=.1*frame
    rt1.set_xy((dx+1,1))
    rt2.set_xy((dx+3,1.5))
    cr1.set_center((dx+2,1))
    cr2.set_center((dx+6,1))
    return rt1,rt2,cr1,cr2


ani=animation.FuncAnimation(fig,update,frames=100,interval=50,blit=True)




plt.show()
