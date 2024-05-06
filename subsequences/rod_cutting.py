class solution:
   def memorization(self,ind,price,target,dp):
      if ind==0 and target==0:
         return 0
      if ind==0:
         return -1e9
      if dp[ind][target]!=-1:
         return dp[ind][target]
      not_pick=self.memorization(ind-1,price,target,dp)
      pick=0
      if ind<=target:
         pick=price[ind]+self.memorization(ind,price,target-ind,dp)
      dp[ind][target]=max(not_pick,pick)
      return dp[ind][target]
   def tabularization(self,):
      ...
s=solution()
n=5
price=[2,5,7,8,10]
price.insert(0,0)
dp=[[-1 for i in range(n+1)] for j in range(n+1)]
print(s.memorization(n-1,price,n,dp))