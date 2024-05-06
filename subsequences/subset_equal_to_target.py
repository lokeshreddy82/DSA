#Problem Statement
'''
We are given an array ‘ARR’ with N positive integers. 
We need to find if there is a subset in “ARR” with a sum equal to K. 
If there is, return true else return false

'''
class solution:
   def memorization(self,ind,array,target,dp):
      if target==0:
         return True
      if ind==0:
         return target==array[ind]
      if dp[ind][target]!=-1:
         return dp[target][ind]
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
target=4
array=[1,2,3,4]
dp=[[-1 for i in range(target+1)] for j in range(len(array))]
print(s.memorization(len(array)-1,array,target,dp))
print(s.tabularization(array,target))