import matplotlib.pyplot as plt

def DDA_line(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1

    steps=int(max(abs(dx),abs(dy)))

    Xinc=dx/steps
    Yinc=dy/steps

    x=x1
    y=y1

    x_point=[]
    y_point=[]

    for _ in range(steps+1):
        x_point.append(round(x))
        y_point.append(round(y))
        x+=Xinc
        y+=Yinc

    return x_point,y_point




xstart=int(input("Enter x1 :"))
ystart=int(input("Enter y1 :"))
xend=int(input("Enter x2 :"))
yend=int(input("Enter y2 :"))




Xval,Yval=DDA_line(xstart,ystart,xend,yend)
plt.figure(figsize=(8,4))
plt.plot(Xval,Yval,color='red')
plt.xlabel("X axix")
plt.ylabel("Y axix ")
plt.title("DDA algorithm")
plt.grid(True)

print(Xval)
print(Yval)





plt.show()