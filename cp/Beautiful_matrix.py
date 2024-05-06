row=0
col=0
for i in range(5):
    n=list(map(int,input().split()))
    for ind,j in enumerate(n):
        if j==1:
            col=ind
            row=i
            break
    break
n=5
row_reach=2
row_col=2
