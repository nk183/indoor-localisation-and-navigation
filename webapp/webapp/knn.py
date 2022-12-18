
import csv
import math
inputDict = {}

dists = []

def getInput(filename):
    with open(filename, mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines[0],lines[1])
            # row = lines[0].split(',')
            # print(row)
            inputDict[lines[0]] = float(lines[1])

def euclideanDist(dict):
    sqsum = 0
    for mac,rssi in inputDict.items():
        x = 0
        if mac in dict.keys():
           x =  dict[mac]
        sqsum = sqsum + pow(rssi-x ,2)
    for mac,avgRssi in dict.items():
        if mac not in inputDict.keys():
            sqsum = sqsum + pow(avgRssi-x, 2)
        


    dists.append(math.sqrt(sqsum))

def matching(filenames):
    for filename in filenames:
        dict = {}
        with open('avg'+filename, mode ='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                row = lines[0].split(',')
                dict[lines[0]] = float(lines[1])
        
        euclideanDist(dict)

def apply_knn():
    filenames = ['lib_(1,1).csv','lib_(1,2).csv','lib_(2,1).csv','lib_(2,2).csv']
    inputFilename='input.csv'
    getInput(inputFilename)
    matching(filenames)
    print(dists)


    