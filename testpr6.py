import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import matplotlib.animation as animation

fig,ax=plt.subplots(figsize=(8,4))
ax.set_xlim(13,0)
ax.set_ylim(0,8)
ax.axis('off')

# for flag
flag_height=3
flag_widht=6
flag_top=1
flag_left=1
wave_amplitude=.1
wave_frequency=1*np.pi*flag_height


# mesh
x=np.linspace(0,flag_widht,300)
y=np.linspace(0,flag_height,200)
X,Y=np.meshgrid(x,y)


def update(time):
    ax.clear()
    ax.set_xlim(0,13)
    ax.set_ylim(0,8)
    ax.axis('off')

# green
    Z=wave_amplitude*np.sin(wave_frequency*Y+time)
    ax.contourf(X+Z+flag_left,Y+flag_top,np.ones_like(Z),levels=1,colors='green')

    # red
    center_x=flag_left+flag_widht/2+wave_amplitude*np.sign(time+2)
    center_y=flag_top+flag_height/2
    circle=Circle((center_x,center_y),.6,color='red')
    ax.add_patch(circle)

ani=animation.FuncAnimation(fig,update,frames=np.linspace(0,2*np.pi,60),interval=50)







plt.show()


