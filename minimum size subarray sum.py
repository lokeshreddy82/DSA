#minimum size subarray sum
def solution(nums,target):
    if target in nums:
        return 1
    elif sum(nums)<target:
        return 0
    listt=[]
    min_length=len(nums)
    for i in range(len(nums)):
        listt.append(nums[i])
        low=0
        high=len(listt)
        while low<=high:
            if sum(listt)>=target:
                min_length=min(min_length,len(listt))
                listt.pop(0)
                low+=1
            else:
                low +=1
    return min_length
nums=[1,2,3,4,5]
target=11
print(solution(nums,target))

nums=[2,3,1,2,4,3]
target=7
c=solution()
print(c.minsubarraylen(nums,target))
