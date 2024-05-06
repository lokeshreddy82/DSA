#Count subset sum with sum K
"""
We are given an array ‘ARR’ with N positive integers and an integer K. 
We need to find the number of subsets whose sum is equal to K.
"""
class solution:
   def memorization(self,ind,array,target,dp):
      if target==0:
         return 1
      if ind==0:
         return 1 if array[ind]==target else 0
      if dp[ind][target]!=-1:
         return dp[ind][target]
      not_pick=self.memorization(ind-1,array,target,dp)
      pick=0
      if array[ind]<=target:
         pick=self.memorization(ind-1,array,target-array[ind],dp)
      dp[ind][target]=pick+not_pick
      return dp[ind][target]
   def tabularization(self,array,target):
      n=len(array)
      dp=[[-1 for i in range(target+1)]for j in range(n)]
      if array[0]<=target:
         dp[0][array[0]]=1
      for i in range(1,n):
         for j in range(1,target+1):
            notTaken = dp[i - 1][j]
            taken = 0
            if array[i] <= j:
                taken = dp[i - 1][j - array[i]]
            dp[i][j] = notTaken + taken
      return dp[n-1][target]
s=solution()
array=[1,2,3]
target=3
n=len(array)
dp=[[-1 for i in range(target+1)]for j in range(n)]
print(s.tabularization(array,target))