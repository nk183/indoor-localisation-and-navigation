
import csv
import math
inputDict = {}
import os

def getInput(dict_wknn_value,dict_wknn_coo,filename):
    with open(filename, mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            # print(lines[0],lines[1])
            # row = lines[0].split(',')
            # print(row)
            inputDict[lines[0]] = float(lines[1])

def euclideanDist(dict_wknn_value,dict_wknn_coo,dict):
    sqsum = 0
    for mac,rssi in inputDict.items():
        x = 0
        if mac in dict.keys():
           x =  dict[mac]
        sqsum = sqsum + pow(rssi-x ,2)
    for mac,avgRssi in dict.items():
        if mac not in inputDict.keys():
            sqsum = sqsum + pow(avgRssi, 2)
        
    
    return math.sqrt(sqsum)

def matching(dict_wknn_value,dict_wknn_coo,filenames):
    i=0
    for filename in filenames:
        dict = {}
        with open('data/avg/'+filename, mode ='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                row = lines[0].split(',')
                dict[lines[0]] = float(lines[1])

        dict_wknn_value[i] = euclideanDist(dict_wknn_value,dict_wknn_coo,dict)
        # print(dict_wknn_value[i])
        i=i+1


def wknn(dict_wknn_value,dict_wknn_coo,k):
    sorted_dic = sorted(dict_wknn_value.items(), reverse = True,key=lambda x:x[1])
    dict_wknn = dict(sorted_dic)
    x=0
    y=0
    sum=0
    i=0
    for indx,val in dict_wknn_value.items():
        if i==k:
            break
        st = dict_wknn_coo[indx] 
        coo = st.split(',')
        x += float(coo[0]) * val
        y += float(coo[1]) * val
        sum+=val
        i=+1

    x=x/sum
    y=y/sum
    lis=[x,y]
    print("xxxxxxxxxx",lis)
    return lis
    

def apply_wknn():
    k=4
    dict_wknn_value = {}
    dict_wknn_coo = {}
    dir_list = os.listdir("data/avg")
    # filenames = ['lib_(1,1).csv','lib_(1,2).csv','lib_(2,1).csv','lib_(2,2).csv']
    # filenames = ['lib_(1,1).csv','lib_(1,2).csv','lib_(2,1).csv','lib_(2,2).csv']
    filenames = os.listdir("data/avg")
    inputFilename='input.csv'
    i=0
    for n in filenames:
        s = n.index('(')
        e = n.index(')')
        coo = n[s+1:e]
        # print(coo)
        dict_wknn_coo[i] = coo
        i=i+1


    getInput(dict_wknn_value,dict_wknn_coo,inputFilename)
    matching(dict_wknn_value,dict_wknn_coo,filenames)
    sorted_dic = sorted(dict_wknn_value.items(),reverse=True ,key=lambda x:x[1])
    dict_wknn_value = dict(sorted_dic)
    # print(dict_wknn_value)
    # print(dict_wknn_coo)
    return wknn(dict_wknn_value,dict_wknn_coo,k)
    
# apply_wknn()

