class solution:
   def memorization(self,ind1:int,ind2:int,s1:str,s2:str,dp:list[list[int]]) ->int:
      if ind1<0 or ind2<0:
         return 0
      if dp[ind1][ind2]!=-1:
         return dp[ind1][ind2]
      not_pick=max(self.memorization(ind1-1,ind2,s1,s2,dp),self.memorization(ind1,ind2-1,s1,s2,dp))
      pick=0
      if s1[ind1]==s2[ind2]:
         pick=1+self.memorization(ind1-1,ind2-1,s1,s2,dp)
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
   def main(self,s1:str,s2:str) ->None :
      dp=[[-1 for i in range(len(s1))] for j in range(len(s2))]
      length=self.memorization(len(s1)-1,len(s2)-1,s1,s2,dp)
      for i in dp:
         print(i)
      res=""
      i=len(s2)
      j=len(s1)
      while i>0 and j>0:
         if s2[i-1]==s1[j-1]:
            res +=s2[i-1]
            i -=1
            j -=1
         elif s2[i-1]>s1[j-1]:
            i-=1
         else:
            j-=1
      return res[::-1]
s=solution()
s1="adebc"
s2="dcadb"
print(s.main(s1,s2))

