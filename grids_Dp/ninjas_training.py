#Ninga's trainning
"""
Problem Statement: 
A Ninja has an ‘N’ Day training schedule. 
He has to perform one of these three activities (Running, Fighting Practice, or Learning New Moves) each day.
There are merit points associated with performing an activity each day. The same activity can’t be performed on two consecutive days.
We need to find the maximum merit points the ninja can attain in N Days.

We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of specific activity on that particular day.
Our task is to calculate the maximum number of merit points that the ninja can earn."""
class solution:
   def memorization(self,ind,prev,matrix,dp):
      if dp[ind][prev]!=-1:
         return dp[ind][prev]
      if ind==0:
         ans=0
         for i in range(len(matrix[0])):
            if i!=prev:
               ans=max(ans,matrix[ind][i])
         return ans
      maxi=0
      for i in range(len(matrix[0])):
         if prev!=i:
            act=self.memorization(ind-1,i,matrix,dp)+matrix[ind][i]
            maxi=max(maxi,act)
      dp[ind][prev]=maxi
      return dp[ind][prev]
   def tabulization(self,matrix):
      pass

s=solution()
matrix=[[10,40,70],[20,50,80],[30,60,90]]
dp=[[-1 for i in range(len(matrix[0]))]for j in range(len(matrix))]
n=len(matrix)-1
m=len(matrix[0])-1
print(s.memorization(n,-1,matrix,dp))
print(s.tabulization())
print(dp)

