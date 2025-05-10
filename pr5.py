import matplotlib.pyplot as plt

val=[50,100,100,30,60]
lb=['Tshirt',"Shirt",'pant','cap','shoose']
plt.pie(val,labels=lb,radius=1,autopct='%f%%')
plt.savefig('pie1.png')
plt.show()