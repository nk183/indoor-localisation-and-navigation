
import csv
import math
inputDict = {}
import os

def getInput(dict_knn_value,dict_knn_coo,filename):
    with open(filename, mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            # print(lines[0],lines[1])
            # row = lines[0].split(',')
            # print(row)
            inputDict[lines[0]] = float(lines[1])

def euclideanDist(dict_knn_value,dict_knn_coo,dict):
    sqsum = 0
    for mac,rssi in inputDict.items():
        x = 0
        if mac in dict.keys():
           x =  dict[mac]
        sqsum = sqsum + pow(rssi-x ,2)
    for mac,avgRssi in dict.items():
        if mac not in inputDict.keys():
            sqsum = sqsum + pow(avgRssi-x, 2)
        
    
    return math.sqrt(sqsum)

def matching(dict_knn_value,dict_knn_coo,filenames):
    i=0
    for filename in filenames:
        dict = {}
        with open('data/avg/'+filename, mode ='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                row = lines[0].split(',')
                dict[lines[0]] = float(lines[1])

        dict_knn_value[i] = euclideanDist(dict_knn_value,dict_knn_coo,dict)
        # print(dict_knn_value[i])
        i=i+1


def knn(dict_knn_value,dict_knn_coo,k):
    sorted_dic = sorted(dict_knn_value.items(), reverse = True,key=lambda x:x[1])
    dict_knn = dict(sorted_dic)
    indx = list(dict_knn.keys())[0]
    st = dict_knn_coo[indx] 
    coo = st.split(',')
    return [float(coo[0]),float(coo[1])]
    

def apply_knn():
    k=4
    dict_knn_value = {}
    dict_knn_coo = {}
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
        dict_knn_coo[i] = coo
        i=i+1


    getInput(dict_knn_value,dict_knn_coo,inputFilename)
    matching(dict_knn_value,dict_knn_coo,filenames)
    sorted_dic = sorted(dict_knn_value.items(),reverse=True ,key=lambda x:x[1])
    dict_knn_value = dict(sorted_dic)
    # print(dict_knn_value)
    # print(dict_knn_coo)
    return knn(dict_knn_value,dict_knn_coo,k)
    
# apply_knn()

