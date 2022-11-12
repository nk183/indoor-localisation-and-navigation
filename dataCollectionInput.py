import csv
import rssi

interface = 'wlo1'
rssi_scanner = rssi.RSSI_Scan(interface)
filename = 'input.csv'
ssids = ['PEC_WIFI']
with open(filename, 'w')as file:
    ap_info = rssi_scanner.getAPinfo(ssids,sudo=True)
    writer = csv.writer(file)      
    for rssi in ap_info:
        writer.writerow([rssi['mac'],rssi['signal']])
    
# print(ap_info)

# from access_points import get_scanner


# for i in range(0,100):
#     wifi_scanner = get_scanner()
#     print(wifi_scanner.get_access_points())
#     i=i+1

# x = wifi_scanner.get_access_points()
# for i in x:
#     print(i)

# f = open("(1,1).csv","rt")

# x =  f.read() 
# # print(x[1])

# dict = {}
# with open('(1,1).csv', mode ='r')as file:

#     csvFile = csv.reader(file)
#     for lines in csvFile:
#         x = lines[0].split(',')
#         # dict= 
#         print(x)
