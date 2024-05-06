def solution(nums):
    nums.sort()#xor works hear
    for i in range(len(nums)):
        if nums[i]==nums[i+1]:
            continue
        else:
            return nums[i]
nums=[4,1,2,1,2]
print(solution(nums))
