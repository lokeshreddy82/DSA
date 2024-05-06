class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[-1 for i in range(m)]for j in range(n)]
        def memorization(ind1,ind2):
            if ind2==m:
                return 1
            if ind1==n:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            not_taken=memorization(ind1+1,ind2)
            if s[ind1]==t[ind2]:
                not_taken +=memorization(ind1+1,ind2+1)
            dp[ind1][ind2]=not_taken
            return dp[ind1][ind2]
        return memorization(0,0)
    def tabularization(self,s1,s2):
         n=len(s1)
         m=len(s2)
         dp=[[0 for i in range(m+1)] for j in range(n+1)]
         for i in range(1,n+1):
               for j in range(1,m+1):
                   ...
s=Solution()
s1="babgbag"
s2="bag"
print(s.tabularization(s1,s2))