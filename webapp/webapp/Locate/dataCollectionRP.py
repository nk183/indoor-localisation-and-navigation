import csv

import time
import rssi

interface = 'wlo1'
rssi_scanner = rssi.RSSI_Scan(interface)
filename = 'xaudi_(2,0).csv'
ssids = ['PEC_WIFI']
with open(filename, 'w')as file:
    for i in range (1,60):
        ap_info = rssi_scanner.getAPinfo(ssids,sudo=True)
        writer = csv.writer(file)      
        for rssi in ap_info:
            writer.writerow([rssi['mac'],rssi['signal']])
        time.sleep(0.6)
        i=i+1
    
