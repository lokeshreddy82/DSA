class solution:
   def memorization(self,ind1,ind2,s1,s2,n,m,dp):
      if ind1==n or ind2==m:
         return n-ind1+m-ind2
      if dp[ind1][ind2]!=-1:
         return dp[ind1][ind2]
      not_taken=1+min(self.memorization(ind1+1,ind2,s1,s2,n,m,dp),self.memorization(ind1,ind2+1,s1,s2,n,m,dp))
      taken=float('inf')
      if s1[ind1]==s2[ind2]:
         taken=1+self.memorization(ind1+1,ind2+1,s1,s2,n,m,dp)
      dp[ind1][ind2]=min(taken,not_taken)
      return dp[ind1][ind2]
s1="brute"
s2="groot"
n=len(s1)
m=len(s2)
dp=[[-1 for i in range(m)] for j in range(n)]
s=solution()
print(s.memorization(0,0,s1,s2,n,m,dp))