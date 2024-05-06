class solution:
   def memorization(self,ind1,ind2,s1,s2,dp,n,m) -> int:
      if ind1<0 or ind2<0:
         return 0
      if dp[ind1][ind2]!=-1:
         return dp[ind1][ind2]
      not_pick=max(self.memorization(ind1-1,ind2,s1,s2,dp,n,m),self.memorization(ind1,ind2-1,s1,s2,dp,n,m))
      pick=0
      if s1[ind1]==s2[ind2]:
         pick=1+self.memorization(ind1-1,ind2-1,s1,s2,dp,n,m)
      dp[ind1][ind2]=max(pick,not_pick)
      return dp[ind1][ind2]
s=solution()
s1="abcd"
s2="anc"
n,m=len(s1),len(s2)
dp=[[-1 for i in range(m)]for j in range(n)]
k=s.memorization(n-1,m-1,s1,s2,dp,n,m)
print(n-k+m-k)