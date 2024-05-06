from collections import Counter
n=int(input(""))
for i in range(n):
   s=int(input(""))
   arr=list(map(int,input().split()))
   hashing=Counter(arr)
   sizes=[3,4,5,6,7,8,9,10]
   res=0
   ans=0
   for key,value in hashing.items():
      for i,j in enumerate(sizes):
         if value>=j and res<j:
            res=j
            ans=i
   print(ans)