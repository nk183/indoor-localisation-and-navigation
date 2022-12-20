import csv

import time
import rssi

def calibrate_func(rssi,location,x_coordinate,y_coordinate):
    interface = 'wlo1'
    rssi_scanner = rssi.RSSI_Scan(interface)
    filename = location+"_("+x_coordinate+","+y_coordinate+")"+".csv"
    ssids = ['PEC_WIFI']
    with open(filename, 'w')as file:
        for i in range (1,5):
            ap_info = rssi_scanner.getAPinfo(ssids,sudo=True)
            writer = csv.writer(file)      
            for rssi in ap_info:
                writer.writerow([rssi['mac'],rssi['signal']])
            time.sleep(0.6)
            i=i+1
        
