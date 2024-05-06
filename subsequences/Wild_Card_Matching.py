class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        m=len(p)
        dp=[[-1 for i in range(len(p))]for j in range(len(s))]
        def dfs(i,j):
            if i==n and j==m:
                return True
            if i==n:
                for k in range(j,m):
                    if p[k]!="*":
                        return False   
                return True
            if j==m:
                return False
            if dp[i][j]!=-1:
                return dp[i][j]
            taken=False
            not_taken=False
            if s[i]==p[j] or p[j]=="?":
                taken=dfs(i+1,j+1)
            elif p[j]=="*":
                taken=dfs(i+1,j)
                not_taken=dfs(i+1,j+1) or dfs(i,j+1)

            dp[i][j]=taken or not_taken
            return dp[i][j]
        dfs(0,0)
        for i in dp:
            print(i)
        
s=Solution()
print(s.isMatch("adceb","*a*b"))