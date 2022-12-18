import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from main_looper import looper

style.use('fivethirtyeight')

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
    
    xs=[]
    ys=[]
    data=open("cood.csv")
    for lines in data:
        if len(lines)>1:
            print(lines)
            x,y=lines.split(",")
            xs.append(float(x))
            ys.append(float(y))
    data.close()
    ax1.clear()
    ax1.axis([-8, 8, -10, 8])
    plt.plot(xs, ys, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="red")
    ax1.plot(xs,ys)
    looper()
    # ax1.plot(2,3)

ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()