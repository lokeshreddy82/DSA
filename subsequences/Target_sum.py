#Target sum
"""
We are given an array ‘ARR’ of size ‘N’ and a number ‘Target’. 
Our task is to build an expression from the given array where 
we can place a ‘+’ or ‘-’ sign in front of an integer. 
We want to place a sign in front of every integer of the array and get our required target. 
We need to count the number of ways in which we can achieve our required target
"""
class solution():
    def memorization(self,ind,arr,target,dp,curr):
        if ind<0:
            if curr==target:
                return 1
            return 0
        plus=self.memorization(ind-1,arr,target,dp,curr+arr[ind])
        minus=self.memorization(ind-1,arr,target,dp,curr-arr[ind])
        return plus+minus
    def tabularization(self,arr,target):
        n=len(arr)
        dp=[[0 for i in range(target+1)]for j in range(n)]
        if arr[0]==0:
            dp[0][0]=2
        else:
            dp[0][0]=1
        if arr[0]!=0 and arr[0]<=target:
            dp[0][arr[0]]=1
        for i in range(1,n):
            for j in range(target+1):
                not_pick=dp[i-1][j]
                take=0
                if arr[i]<=j:
                    take=dp[i-1][j-arr[i]]
                dp[i][j]=take+not_pick
        return dp[len(arr)-1][target]
    def main_function(self,arr,target):
        summ=sum(arr)
        if summ-target<0 or (summ-target)%2:
            return 0
        return self.tabularization(arr,(summ-target)//2)
arr=[1,2,3,1]
target=3
dp=[[-1 for i in range(target+1)]for j in range(len(arr))]
s=solution()
print(s.memorization(len(arr)-1,arr,target,dp,0))
print(s.main_function(arr,target))