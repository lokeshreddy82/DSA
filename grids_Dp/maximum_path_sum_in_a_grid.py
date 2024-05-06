"""
Problem Description: 

We are given an “N*M” matrix of integers. 
We need to find a path from the top-left corner to the bottom-right corner of the matrix, 
such that there is a minimum cost past that we select.

At every cell, we can move in only two directions: right and bottom. 
The cost of a path is given as the sum of values of cells of the given matrix.
"""
class solution:
   def memorization(self,matrix,dp,row,col):
      if row<0 or col<0:
         return 1e9
      if row==0 and col==0:
         return matrix[0][0]
      if dp[row][col]!=-1:
         return dp[row][col]
      left=matrix[row][col]+self.memorization(matrix,dp,row-1,col)
      right=matrix[row][col]+self.memorization(matrix,dp,row,col-1)
      dp[row][col]=min(left,right)
      return dp[row][col]
   def tabularization(self,matrix):
      row=len(matrix)
      col=len(matrix[0])
      dp=[[-1 for i in range(col)]for j in range(row)]
      dp[0][0]=matrix[0][0]
      for i in range(1,row):
         dp[i][0]=matrix[i-1][0]+matrix[i][0]
      for j in range(1,col):
         dp[0][j]=dp[0][j-1]+matrix[0][j]
      for i in range(1,row):
         for j in range(1,col):
            dp[i][j]=matrix[i][j]+min(dp[i-1][j],dp[i][j-1])
      return dp[row-1][col-1]
   def space_optimization(self,matrix):
      row=len(matrix)
      col=len(matrix[0])
      prev=[-1 for i in range(col)]
      prev[0]=matrix[0][0]
      for i in range(1,col):
         prev[i]=prev[i-1]+matrix[0][i]
      for i in range(1,row):
         curr=[-1 for i in range(col)]
         curr[0]=matrix[i][0]+prev[0]
         for j in range(1,col):
            curr[j]=matrix[i][j]+min(prev[j],curr[j-1])
         prev=curr
      return prev[col-1]
matrix=[[5,9,6],[11,5,2]]
row=len(matrix)
col=len(matrix[0])
dp=[[-1 for i in range(col)]for j in range(row)]
s=solution()
print(s.memorization(matrix,dp,row-1,col-1))
print(s.tabularization(matrix))
print(s.space_optimization(matrix))
