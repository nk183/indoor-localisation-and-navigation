
from dataCollectionInput import get_input 
from knn import apply_knn
from wknn import apply_wknn
import rssi
# from animation import 
import csv

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from avrageRSSI import avg_rssi
# def graph():
#     style.use('fivethirtyeight')

#     fig=plt.figure()
#     ax1=fig.add_subplot(1,1,1)

#     def animate(i):
        
#         xs=[]
#         ys=[]
#         data=open("cood.csv")
#         for lines in data:
#             if len(lines)>1:
#                 print(lines)
#                 x,y=lines.split(",")
#                 xs.append(float(x))
#                 ys.append(float(y))
#         data.close()
#         ax1.clear()
#         ax1.axis([-8, 8, -10, 8])
#         ax1.plot(xs,ys)

#     ani = animation.FuncAnimation(fig,animate,interval=1000)
#     plt.show()

def looper():
    # graph()
    # while True:
    get_input(rssi)
    # knn_output = apply_knn()
    avg_rssi()
    wknn_output = apply_wknn()
    with open('cood.csv', 'a')as file:
        writer = csv.writer(file)      
        
        # writer.writerow([knn_output[0],knn_output[1]])
        writer.writerow([wknn_output[0],wknn_output[1]])

looper()
        

