class solution:
   def memorization(self,ind1,ind2,st,rev,dp,n):
      if ind1==n or ind2==n:
         return 0
      if dp[ind1][ind2]!=-1:
         return dp[ind1][ind2]
      not_pick=max(self.memorization(ind1+1,ind2,st,rev,dp,n),self.memorization(ind1,ind2+1,st,rev,dp,n))
      pick=0
      if st[ind1]==rev[ind2]:
         pick=1+self.memorization(ind1+1,ind2+1,st,rev,dp,n)
      dp[ind1][ind2]=max(pick,not_pick)
      return dp[ind1][ind2]
   def tabularization(self,st,rev):
      n=len(st)
      dp=[[0 for i in range(n+1)] for j in range(n+1)]
      res=0
      for i in range(1,n+1):
         for j in range(1,n+1):
            not_pick=max(dp[i-1][j],dp[i][j-1])
            pick=0
            if st[i-1]==rev[j-1]:
               pick=1+dp[i-1][j-1]
            dp[i][j]=max(pick,not_pick)
      return dp[n][n]
s=solution()
st="nitin"
n=len(st)
dp=[[-1 for i in range(n)] for j in range(n)]
rev=st[::-1]
print(s.memorization(0,0,st,rev,dp,n))
print(s.tabularization(st,rev))