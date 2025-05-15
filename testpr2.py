import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
import matplotlib.animation as animation

fig,ax=plt.subplots(figsize=(8,4))
ax.set_xlim(0,13)
ax.set_ylim(0,5)
ax.axis('off')

ret1=Rectangle((1,1),6,2)
ret2=Rectangle((2,1.5),4,2)
ax.add_patch(ret1)
ax.add_patch(ret2)

cir1=Circle((2,1),.5,color='black')
cir2=Circle((6,1),.5, color='black')
ax.add_patch(cir1)
ax.add_patch(cir2)

# for road
ret3=Rectangle((0,0),13,.5,color="gray")
ax.add_patch(ret3)

def update(frame):
    dx=.1*frame
    ret1.set_xy((dx+1,1))
    ret2.set_xy((dx+2,1.5))
    cir1.set_center((dx+2,1))
    cir2.set_center((dx+6,1))
    return ret1,ret2,cir1,cir2

ani=animation.FuncAnimation(fig,update,frames=100, interval=50,blit=True)






plt.show()