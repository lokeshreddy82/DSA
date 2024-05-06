#Partition Set Into 2 Subsets With Min Absolute Sum Diff
"""
We are given an array ‘ARR’ with N positive integers. 
We need to partition the array into two subsets such that the absolute difference of the sum of elements of the 
subsets is minimum.

We need to return only the minimum absolute difference of the sum of elements of the two partitions.
"""
class solution:
   def memorization(self,ind,array,target,dp):
      if target==0:
         return True
      if ind==0:
         return target==array[ind]
      if dp[ind][target]!=-1:
         return dp[ind][target]
      not_pick=self.memorization(ind-1,array,target,dp)
      pick=False
      if array[ind]<=target:
         pick=self.memorization(ind-1,array,target-array[ind],dp)
      dp[ind][target]=pick or not_pick
      return dp[ind][target]
   def tabularization(self,array,target):
      dp=[[False for i in range(target+1)]for j in range(len(array))]
      if array[0]<=target:
         dp[0][array[0]]=True
      for i in range(1,len(array)):
         for j in range(1,target+1):
            not_pick=dp[i-1][j]
            pick=False
            if array[i]<=j:
                 pick = dp[i - 1][j - array[i]]
            dp[i][j] = not_pick or pick
      return dp[len(array)-1][target]
s=solution()
array=[1,2,3,4]
total_sum=sum(array)
dp=[[-1 for i in range(total_sum+1)]for j in range(len(array))]
n=len(array)-1
for i in range(1,total_sum + 1):
   s.memorization(n,array,i,dp)
res=float('inf')
iter=total_sum//2
for i in range(1,iter+1):
   if dp[n][i]==True:
      res=min(res,abs(i-(total_sum-i)))
print(res)
