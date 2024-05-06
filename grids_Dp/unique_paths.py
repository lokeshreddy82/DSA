class grid_unique_paths:
   def memoritzation(self,matrix,dp,row,column):
      if row <0 or column<0:
         return 0
      if row==0 and column==0:
         return 1
      if dp[row][column]!=-1:
         return dp[row][column]
      up=self.memoritzation(matrix,dp,row-1,column)
      down=self.memoritzation(matrix,dp,row,column-1)
      dp[row][column]=up+down
      return dp[row][column]
   def tabulization(self,matrix):
      row=len(matrix)
      col=len(matrix[0])
      dp=[[-1 for i in range(col)]for j in range(row)]
      dp[0][0]=1
      for i in range(row):
         dp[i][0]=1
      for k in range(col):
         dp[0][k]=1
      for i in range(1,row):
         for j in range(1,col):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
      return dp[row-1][col-1]
   def space_optimization(self,matrix):
      row=len(matrix)
      col=len(matrix[0])
      prev=[1 for i in range(col)]
      for i in range(1,row):
         present=[-1 for i in range(col)]
         present[0]=1
         for j in range(1,col):
            present[j]=present[j-1]+prev[j]
         prev=present
      return prev[col-1]
matrix=[[0 for i in range(12)] for j in range(3)]
dp=[[-1 for i in range(len(matrix[0]))]for j in range(len(matrix))]
s=grid_unique_paths()
print(s.memoritzation(matrix,dp,len(matrix)-1,len(matrix[0])-1))
print(s.tabulization(matrix))
print(s.space_optimization(matrix))