#0/1 Knapsack
"""
A thief wants to rob a store. He is carrying a bag of capacity W. 
The store has ‘n’ items. Its weight is given by the ‘wt’ array and its value by the ‘val’ array. 
He can either include an item in its knapsack or exclude it but can’t partially have it as a fraction. 
We need to find the maximum value of items that the thief can steal.
"""
import sys
class solution:
   def memorization(self,ind,weight,values,bag_wt,dp):
      if ind==0:
         if bag_wt>=weight[ind]:
            return values[ind]
         return 0
      if dp[ind][bag_wt]!=-1:
         return dp[ind][bag_wt]
      not_pick=0+self.memorization(ind-1,weight,values,bag_wt,dp)
      pick=float('-inf')
      if weight[ind]<=bag_wt:
         pick=values[ind]+self.memorization(ind-1,weight,values,bag_wt-weight[ind],dp)
      dp[ind][bag_wt]=max(not_pick,pick)
      return dp[ind][bag_wt]
   def tabularization(self,wt,val,W):
      n=len(weight)
      dp=[[0 for i in range(bag_wt+1)] for j in range(n)]
      for i in range(wt[0], W + 1):
        dp[0][i] = val[0]
      for ind in range(1, n):
         for cap in range(W + 1):
               not_taken = 0 + dp[ind - 1][cap]
               taken = -sys.maxsize
               if wt[ind] <= cap:
                  taken = val[ind] + dp[ind - 1][cap - wt[ind]]
               dp[ind][cap] = max(not_taken, taken)
      return dp[n - 1][W]
weight=[1,2,3,4]
values=[5,4,8,6]
bag_wt=5
n=len(weight)
dp=[[-1 for i in range(bag_wt+1)] for j in range(n)]
s=solution()
print(s.memorization(n-1,weight,values,bag_wt,dp))
print(s.tabularization(weight,values,bag_wt))