class solution:
   def tabularization(self,array):
      sumation=sum(array)
      if sumation%2!=0:
         return -1
      target=sumation//2
      dp=[[False for i in range(target+1)]for j in range(len(array))]
      if array[0]<=target:
         dp[0][array[0]]=True
      for i in range(1,len(array)):
         for j in range(1,target+1):
            not_pick=dp[i-1][j]
            pick=False
            if array[i]<=j:
                 pick = dp[i - 1][j - array[i]]
            dp[i][j] = not_pick or pick
      return target if dp[len(array)-1][target]==True else -1
s=solution()
array=[2,3,3,3,4,5]
print(s.tabularization(array))