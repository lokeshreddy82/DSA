from functools import cache
class solution:
   def memorization(self,ind1 :int,ind2: int,s1 :str,s2 :str,hashing :dict[(int,int,int)],k :int) ->int:
      if ind1==len(s1) or ind2==len(s2):
         return 0
      if (ind1,ind2,k) in hashing:
         return hashing[(ind1,ind2,k)]
      not_pick=0
      if k==-1:
         not_pick=0+max(self.memorization(ind1+1,ind2,s1,s2,hashing,-1),self.memorization(ind1,ind2+1,s1,s2,hashing,-1))
      pick=0
      if s1[ind1]==s2[ind2]:
         n=k+1
         pick=1+self.memorization(ind1+1,ind2+1,s1,s2,hashing,n)
      hashing[(ind1,ind2,k)]=max(pick,not_pick)
      return hashing[(ind1,ind2,k)]
   def tabularization(self,s1 :str,s2 :str):
      dp=[[0 for i in range(len(s2)+1)]for j in range(len(s1)+1)]
      res=-1
      for i in range(1,len(s1)+1):
         for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
               dp[i][j]=1+dp[i-1][j-1]
               res=max(res,dp[i][j])
            else:
               dp[i][j]=0
      return res
s=solution()
s1="abcjklp"
s2="acjkp"
dp=[[-1 for i in range(len(s2))]for j in range(len(s1))]
k=0
hashing={}
print(s.memorization(0,0,s1,s2,hashing,-1))
print(s.tabularization(s1,s2))