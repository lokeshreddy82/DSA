n=int(input(""))
for i in range(n):
    inp=list(map(int,input().split()))
    if inp[0]==0:
        print(0)
    elif inp[0]==1:
        print(inp[1])
    else:
        one=inp[1]*inp[0]
        two=float('inf')
        if inp[0]%2==0:
            two=(inp[0]//2)*inp[2]
        else:
            two=((inp[0]//2)*inp[2])+inp[1]
        print(min(one,two))
