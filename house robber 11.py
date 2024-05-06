def solution(nums):
    if len(nums)<=3:
        return max(nums)
    t1,t2=0,0
    for i in nums:
        temp=max(i+t1,t2)
        t1=t2
        t2=temp
    return t2
nums=[1,2,3,1]
print(solution(nums))
