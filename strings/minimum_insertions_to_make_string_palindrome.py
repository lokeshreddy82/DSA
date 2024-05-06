class solution:
   def memorization(self,ind1 :int,ind2 :int,st :str,rev :str,dp ,n):
      if ind1==n or ind2==n:
         return 0
      if dp[ind1][ind2]!=-1:
         return dp[ind1][ind2]
      tool=0
      if st[ind1]==rev[ind2]:
         tool=0+self.memorization(ind1+1,ind2+1,st,rev,dp,n)
      else:
         tool=1+self.memorization(ind1+1,ind2+1,st,rev,dp,n)
      dp[ind1][ind2]=tool
      return dp[ind1][ind2]
   def tabularization(self,st,rev):
      n=len(st)
      dp=[[-1 for i in range(n+1)] for j in range(n+1)]
      for i in range(1,n+1):
         for j in range(1,n+1):
            if st[i-1]==rev[j-1]:
               dp[i][j]=1+dp[i-1][j-1]
            else:
               dp[i][j]=max(dp[i-1][j],dp[i][j-1])
      return n-dp[i][j]
s=solution()
st="nithin"
rev=st[::-1]
n=len(st)
dp=[[ -1 for i in range(n)] for j in range(n)]
print(s.memorization(0,0,st,rev,dp,n))
print(s.tabularization(st,rev))