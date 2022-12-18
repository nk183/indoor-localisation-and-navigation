

def remove_outliers():
    count=0
    c=0
    # filenames = ['lib_(1,1).csv','lib_(1,2).csv','lib_(2,1).csv','lib_(2,2).csv']
    filenames = ['data.csv']
    same_mac_sig = []
    seen_mac = set()

    d=[]

    for file in filenames:
        u=open(file)
        print(file)
        for line in u:
            mac,sig=line.split(",")
            if mac not in seen_mac:
                seen_mac.add(mac)

                #same_mac_sig.append(sig)
                u2 = open(file)
                for line2 in u2:                                       #looking for same mac
                    mac1,sig1=line2.split(",")
                    if mac1==mac:
                        same_mac_sig.append(int(sig1))                      #creating list of all sig with same mac
                u2.close()
                same_mac_sig.sort(reverse=True)                      #sorting

                i = 0
                while i < len(same_mac_sig) - 1:
                    #print(same_mac_sig[i])
                    if (int(same_mac_sig[i]) - int(same_mac_sig[i + 1])) > 5:
                        same_mac_sig.pop(i + 1)
                        count+=1
                        i = i - 1
                    i = i + 1
                #print(count)
                if count>0:
                    d.append(count)
                count = 0
                ro = open(file, "a")
                for j in same_mac_sig:
                    ro.write(mac+","+str(j)+"\n")
                ro.close()
                same_mac_sig.clear()
        u.close()
        seen_mac.clear()

    print(d)

remove_outliers()

