import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle,Rectangle
import numpy as np

fig,ax=plt.subplots(figsize=(8,4))
ax.set_xlim(0,13)
ax.set_ylim(0,8)
ax.axis('off')


# for flag 
ft=1
fl=1
fh=3
fw=6
wa=.1
wf=5*np.pi/fh


# meshgrid
x=np.linspace(0,fw,300)
y=np.linspace(0,fh,200)
X,Y=np.meshgrid(x,y)


def update(time):
    ax.clear()
    ax.set_xlim(0,13)
    ax.set_ylim(0,8)
    ax.axis('off')
    # for bg
    Z=wa*np.sin(wf*Y+time)
    ax.contourf(X+Z+ft,Y+ft,np.ones_like(Z),levels=1,color='green')

    # for circle
    xCenter=fl+fw/2+ wa*np.sin(time+2)
    yCenter=ft+fh/2
    circle=Circle((xCenter,yCenter),.6,color="red")
    ax.add_patch(circle)

ani=animation.FuncAnimation(fig,update,frames=np.linspace(0,2*np.pi,60),interval=1)




plt.show()