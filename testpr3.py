import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle

fig,ax=plt.subplots(figsize=(8,4))
ax.set_xlim(0,13)
ax.set_ylim(0,5)
ax.axis('off')

rt1=Rectangle((1,1),6,1, color='yellow')
rt2=Rectangle((2,1.5),4,1,color='Yellow')
ax.add_patch(rt1)
ax.add_patch(rt2)

cr1=Circle((2,1),0.5,color='black')
cr2=Circle((6,1),0.5,color='black')
ax.add_patch(cr1)
ax.add_patch(cr2)\



plt.show()

