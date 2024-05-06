class solution:
   def memorization(self,arr):
      n=len(arr)
      dp=[[-1 for i in range(n)] for j in range(n)]
      def dfs(ind,prev):
         if ind==n:
            return 0
         if dp[ind][prev]!=-1:
            return dp[ind][prev]
         not_pick=dfs(ind+1,prev)
         pick=0
         if arr[ind]>=arr[prev]:
            pick=1+dfs(ind+1,ind)
         return max(pick,not_pick)
      return dfs(0,0)
s=solution()
arr=[10,9,2,5,3,7,101,18]
print(s.memorization(arr))
from sortedcontainers import sortedlist
t=[1,2,3,4]