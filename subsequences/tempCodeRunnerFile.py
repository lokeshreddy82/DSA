
      plus=self.memorization(ind-1,arr,target,dp,curr+arr[ind])
      minus=self.memorization(ind-1,arr,target,dp,curr-arr[ind])
      return plus+minus
arr=[1,1,1,1,1]
target=3