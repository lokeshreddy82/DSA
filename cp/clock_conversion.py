n=int(input(""))
res=[]
for i in range(n):
    time=input("")
    normal=int(time[0:2])
    if normal==0:
        res.append("12"+time[2:]+" AM")
    elif normal<12:
            res.append(time+" AM")
    elif normal==12:
            res.append(time+" PM")
    else:
        normal -=12
        if normal>9:
            res.append(str(normal)+time[2:]+" PM")
        else:
            res.append("0"+str(normal)+time[2:]+" PM")
for i in res:
    print(i)
        
