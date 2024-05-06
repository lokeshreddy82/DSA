def lokesh(num):
    listt=[]
    countt=num*3
    if num<=1:
        return num
    for i in range(1,num+1):
        listt.append(i)
    listt.append(i+i)
    for j in range(countt,countt-num,-1):
        listt.append(j)
    m=j
    for k in range(1,num):
        listt.append(m-num)
        if len(listt)==countt:
            return listt
        else:
            m +=1
num=int(input("enter a number"))
result=lokesh(num)
print(result)
