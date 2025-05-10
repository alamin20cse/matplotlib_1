import matplotlib.pyplot as plt

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


# Add a circle (sun) at the top
circle = plt.Circle((1, 8), 0.5, color='yellow')  # (x,y), radius, color
plt.gca().add_patch(circle)

plt.axis('equal')  # To ensure the circle appears circular

plt.show()