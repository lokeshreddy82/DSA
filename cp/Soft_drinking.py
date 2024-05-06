listt=list(map(int,input().split()))
all_friends=listt[1]*listt[2]
case1=all_friends//listt[0]
case2=listt[3]*listt[4]
case3=listt[5]//listt[-1]
print(min(case1,case2,case3)//listt[0])


