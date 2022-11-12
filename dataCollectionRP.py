import csv

import time
import rssi

interface = 'wlo1'
rssi_scanner = rssi.RSSI_Scan(interface)
filename = 'lib_(1,1).csv'
ssids = ['PEC_WIFI']
with open(filename, 'w')as file:
    for i in range (1,20):
        ap_info = rssi_scanner.getAPinfo(ssids,sudo=True)
        writer = csv.writer(file)      
        for rssi in ap_info:
            writer.writerow([rssi['mac'],rssi['signal']])
        time.sleep(1)
        i=i+1
    
