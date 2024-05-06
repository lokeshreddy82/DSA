n=int(input())
for i in range(n):
    ind=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    res=0
    l=0
    r=ind[0]-1
    while arr[l] and arr[r] and ind[1]:
        if l==r:
            arr[l] -=ind[1]
            if arr[l]<1:
                ind[1]=0
                res +=1
                arr[l]=0
        else:
            target=arr[l]+arr[r]
            if target<=ind[1]:
                res +=2
                arr[l]=0
                arr[r]=0
                l +=1
                r -=1
                ind[l] -=target
            elif target//2<ind[l]:
                res +=1
                m=min(arr[l],arr[r])
                arr[l] -=m
                arr[r] -=m
                ind[1] -=(m+m)
            else:
                if ind[1]>1:
                    arr[l] -=1
                    arr[r] -=1
                    if arr[1]==0:
                        res +=1
                        l +=1
                    if arr[r]==0:
                        res +=1
                        r -=1
                else:
                    ind[1] -=1
                    if arr[l]==0:
                        res +=1
                    ind[1]=0
    print(res)
                
                
