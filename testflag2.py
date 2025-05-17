import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import matplotlib.animation as animation
import numpy as np

fig,ax=plt.subplots(figsize=(8,4))
ax.set_xlim(0,13)
ax.set_ylim(0,8)
ax.axis('off')

# for flag
flagTop=1
flagLeft=1
flagHeight=3
flagWidht=6
waveAmplitude=.1
waveFrequency=4*np.pi/flagHeight


# mesh gird
x=np.linspace(0,flagWidht,300)
y=np.linspace(0,flagHeight,200)
X,Y=np.meshgrid(x,y)




# for background
def update(time):
    ax.clear()
    ax.set_xlim(0,13)
    ax.set_ylim(0,8)
    ax.axis('off')

    Z=waveAmplitude*np.sin(waveFrequency*Y+time)
    ax.contourf(X+Z+flagLeft,Y+flagTop,np.ones_like(Z),levels=1)

    # for circle
    center_x=flagLeft+flagWidht/2+ waveAmplitude*np.sin(time+2)
    center_y=flagTop + flagHeight/2
    circle=Circle((center_x,center_y),.6,color='red')
    ax.add_patch(circle)



ani=animation.FuncAnimation(fig,update,frames=np.linspace(0,2*np.pi,60),interval=50)

plt.show()