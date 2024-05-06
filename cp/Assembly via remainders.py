for i in range(int(input(""))):
   n=int(input())
   arr=list(map(int,input().split()))
   res=[0]*n
   ind=0
   flag=True
   if n==2:
      if arr[0]==1:
         res[0]=5
         res[1]=11
         flag=False
   elif flag:
      if arr[0]==1:
         res[0]=2
         ind +=1
      every=ind
      for i in range(ind,len(arr)):
         
   print(res)