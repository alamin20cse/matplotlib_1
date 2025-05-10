import matplotlib.pyplot as plt
# import matplotlib.patches as pt
x=[1,5]
y=[1,1]

plt.plot(x,y)

x=[1,1]
y=[1,5]
plt.plot(x,y,color='red')

x=[1,5]
y=[5,5]
plt.plot(x,y,color='green')

x=[5,5]
y=[1,5]
plt.plot(x,y,color='red')

x=[1,3]
y=[5,8]
plt.plot(x,y,color='red')


x=[3,5]
y=[8,5]
plt.plot(x,y,color='red')


x=[2.5,2.5]
y=[1,5]
plt.plot(x,y,color='red')

x=[3.5,3.5]
y=[1,5]
plt.plot(x,y,color='red')
# plt.circle((3,10),2)
# circle = pt.Circle((3, 10), 2, color='green')  # Center = (3,10), radius = 2
# plt.plot(circle)


plt.show()