
class solution:
   def memorization(self,ind1:int,ind2:int,s1:str,s2:str,dp:list[list[int]]) ->int:
      if ind1==len(s1) or ind2==len(s2):
         return 0
      if dp[ind1][ind2]!=-1:
         return dp[ind1][ind2]
      not_pick=max(self.memorization(ind1+1,ind2,s1,s2,dp),self.memorization(ind1,ind2+1,s1,s2,dp))
      pick=0
      if s1[ind1]==s2[ind2]:
         pick=1+self.memorization(ind1+1,ind2+1,s1,s2,dp)
      dp[ind1][ind2]=max(pick,not_pick)
      return dp[ind1][ind2]
   def tabularization(self,s1:str,s2:str) ->int :
      dp=[[0 for i in range(len(s1)+1)]for j in range(len(s2)+1)]
      for i in range(1,len(s2)+1):
         for j in range(1,len(s1)+1):
            not_pick=dp[i][j-1]
            pick=0
            if s2[i-1]==s1[j-1]:
               pick=1+dp[i-1][j-1]
            dp[i][j]=max(pick,not_pick)
      for i in dp:
         print(i)
      return dp[len(s1)][len(s2)]

s=solution()
s1="adebc"
s2="dcadb"
dp=[[-1 for i in range(len(s1))] for j in range(len(s2))]
res="adb"
print(s.memorization(0,0,s1,s2,dp))
print(s.tabularization(s1,s2))
