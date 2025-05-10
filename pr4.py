
import matplotlib.pyplot as plt
import numpy as np

product=np.array([1,2,3,4,5,6,7])
prices=[5,2,3,3,5,7,3]
profit=[3,1,2,2,1,4,1]
plt.bar(product,prices,width=.5,color='green',label='Price')
plt.bar(product+.5,profit,width=.5,color="red",label='Profit')
plt.legend()
plt.show()