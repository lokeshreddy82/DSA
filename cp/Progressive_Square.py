from collections import Counter
n=int(input(""))
for i in range(n):
    index=list(map(int,input().split()))
    indexing=sorted(list(map(int,input().split())))
    a11=indexing[0]
    matrix=[[-1 for i in range(index[0])]for j in range(index[0])]
    matrix[0][0]=a11
    for j in range(1,index[0]):
        matrix[0][j]=matrix[0][j-1]+index[2]
    for k in range(1,index[0]):
        matrix[k][0]=matrix[k-1][0]+index[1]
    for l in range(1,index[0]):
        for m in range(1,index[0]):
            matrix[l][m]=matrix[l][m-1]+index[2]
    res=[]
    for t in matrix:
        res =res+t
    if sorted(res)==sorted(indexing):
        print("Yes")
    else:
        print("No")
    
    
