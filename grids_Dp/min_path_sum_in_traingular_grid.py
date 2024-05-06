"""
We are given a Triangular matrix. 
We need to find the minimum path sum from the first row to the last row.

At every cell we can move in only two directions: 
either to the bottom cell (↓) or to the bottom-right cell(↘)
"""
class solution:
   def memorization(self,matrix,dp,row,col,end):
      if row==end:
         return matrix[row][col]
      if dp[row][col]!=-1:
         return dp[row][col]
      down=matrix[row][col]+self.memorization(matrix,dp,row+1,col,end)
      diagonal=matrix[row][col]+self.memorization(matrix,dp,row+1,col+1,end)
      dp[row][col]=min(down,diagonal)
      return dp[row][col]
   def tabularization(self,matrix,row,col):
      dp=[[-1 for i in range(col)]for j in range(row)]
      dp[0][0]=matrix[0][0]
      for i in range(1,row):
         dp[i][0]=matrix[i][0]+dp[i-1][0]
      ans=dp[i][0]
      end=col
      for i in range(1,row):
         column=len(matrix[row])
         for j in range(1,column):
            pass
matrix=[[1],
        [2,3],
        [3,6,7],
        [8,9,6,10]]
row=len(matrix)
col=len(matrix[-1])
dp=[[-1 for i in range(col)]for j in range(row)]
s=solution()
print(s.memorization(matrix,dp,0,0,row-1))
print(s.)