def permute(nums):
    if len(nums) == 1:
        return [nums]
    permutations = []
    for i in range(len(nums)):
        current_num = nums[i]
        remaining_nums = nums[:i] + nums[i + 1:]
        lokesh = permute(remaining_nums)
        for lokesh in lokesh:
            permutations.append([current_num] + lokesh)
    return (set(permutations))
nums = [1,1,2]
result = permute(nums)
print(result)
