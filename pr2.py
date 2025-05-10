import matplotlib.pyplot as plt


x=[1,3,4,5,6,7,10]
y=[1,2,3,3,5,7,3]

# plt.scatter(x,y ,color='red', linewidth=5,linestyle='dotted')
plt.plot(x,y,'g+-')
x=[1,2,3,5,6,7,10]
y=[1,2,3,3,10,7,11]
# plt.scatter(x,y,color='Green',linestyle='dashdot')
plt.plot(x,y,'rD')
plt.xlabel('Day')
plt.ylabel('Work Time')
plt.title("Work chart")
plt.show()