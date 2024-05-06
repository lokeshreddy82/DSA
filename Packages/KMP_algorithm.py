class solution:
   def kmp_algo(self,s1,s2):
      n=len(s1)
      m=len(s2)
      kmp=[0]*m
      j=0
      def dfs(m,kmp,s2):
         length=0
         i=1
         while i<m:
            if s2[i]==s2[length]:
               length +=1
               kmp[i]=length
               i +=1
            else:
               if length!=0:
                  length =kmp[length-1]
               else:
                  i+=1
      dfs(m,kmp,s2)
      i=0
      res=0
      print(kmp)
      while i<n:
         if s1[i]==s2[j]:
            i +=1
            j +=1
         if j==m:
            res +=1
            j=kmp[j-1]
         elif i<n and s1[i]!=s2[j]:
            if j!=0:
               j=kmp[j-1]
            else:
               i+=1
      return res
s=solution()
s1 = "ABABDABACDABABCABAB"
s2 = "ABABCABAB"
print(s.kmp_algo(s1,s2))