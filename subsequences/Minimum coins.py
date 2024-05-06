class solution:
   def memorization(self,ind,arr,target,dp):
      if target==0:
         return 0
      if ind==0:
         if target%arr[ind]==0:
            return target//arr[ind]
         return 1e9
      if dp[ind][target]!=-1:
         return dp[ind][target]
      not_pick=0+self.memorization(ind-1,arr,target,dp)
      pick=1e9
      if arr[ind]<=target:
         pick=1+self.memorization(ind,arr,target-arr[ind],dp)
      dp[ind][target]=min(pick,not_pick)
      return dp[ind][target]
   def tabularization(self,arr,target):
      n=len(arr)
      dp=[[0 for i in range(target+1)] for j in range(n)]
      
arr=[1,2,3]
target=7
dp=[[-1 for i in range(target+1)]for j in range(len(arr))]
n=len(arr)-1
s=solution()
print(s.memorization(n,arr,target,dp))