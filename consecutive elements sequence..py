def longestconsecutive_sequence(num):
    if len(num)==0:
        return 0
    num=list(set(num))
    num.sort()
    diff=num[1]-num[0]
    countt=1
    for i in range(1,len(num)):
        if num[i]-num[i-1]==diff:
            countt +=1
    return countt
num=[0,3,7,2,5,8,4,6,0,1]
print(longestconsecutive_sequence(num))
