
import csv

dictSum = {}
dictCount = {}
avg = {}

def updateSum(arr):
    # print(arr)
    if arr[0] in dictSum.keys():
        dictSum[arr[0]] = dictSum[arr[0]] + int(arr[1])
        dictCount[arr[0]] = dictCount[arr[0]] +1
    else : 
        dictSum[arr[0]] = int(arr[1])
        dictCount[arr[0]] = 1

def average():
    for mac,sum in dictSum.items():
        avg[mac] = sum/dictCount[mac]

def fun(filename):
    with open(filename, mode ='r')as file:

        csvFile = csv.reader(file)
        for lines in csvFile:
            updateSum(lines)
            average()
            
        for i,j in avg.items():
            print(i,j)
    with open('avg'+filename, 'w')as file:
        writer = csv.writer(file)                       
        # fieldnames = ["MAC","Avg RSSI"]
        # writer.writerow(fieldnames)
        for mac,avgRssi in avg.items():

            writer.writerow([mac,avgRssi])


def main():
    filenames = ['lib_(1,1).csv','lib_(1,2).csv','lib_(2,1).csv','lib_(2,2).csv']
    for filename in filenames:
        fun(filename)

main()
    
