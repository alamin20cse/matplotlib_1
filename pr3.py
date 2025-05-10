import matplotlib.pyplot as plt

days=[1,2,3,4,5,6]
MAX_w=[50,50,60,70,40,46]
MIN_w=[20,30,30,40,20,24]
AVG_w=[30,40,45,55,30,35]

plt.plot(days,MAX_w,label="Max",color='red')
plt.plot(days,MIN_w ,label="Min",color='green')
plt.plot(days,AVG_w,label="AVG",color='yellow')
# plt.legend(loc="upper right")
plt.legend(loc="best")
# plt.legend(loc="lower right")
plt.grid()
plt.show()