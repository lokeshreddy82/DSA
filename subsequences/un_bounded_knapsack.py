class solution:
   def memorization(self,ind,weight,values,w,dp):
      if ind < 0:
        return 0
      if dp[ind][w]!=-1:
         return dp[ind][w]
      not_pick=self.memorization(ind-1,weight,values,w,dp)
      pick=0
      if weight[ind]<=w:
         pick=values[ind]+self.memorization(ind,weight,values,w-weight[ind],dp)
      dp[ind][w]=max(not_pick,pick)
      return dp[ind][w]
   def tabularization(self,):
      ...
s=solution()
wt=[2,4,6]
val=[5,11,13]
w=10
dp=[[-1 for i in range(w+1)]for j in range(len(wt))]
print(s.memorization(len(wt)-1,wt,val,w,dp))