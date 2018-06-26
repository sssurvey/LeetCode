# 137
# [2,2,2,1,0,0,0] return 1
# or [2,2,3,2] return 2

def singleNumberII(nums):
    current = nums[0]
    if len(nums) == 1:                              return nums[0]
    elif nums[0] != nums[1]:                        return nums[0]
    elif nums[len(nums)-1] != nums[len(nums)-2]:    return nums[len(nums)-1]
        
    for index in range(1, len(nums)-1):
        if nums[index] != nums[index-1] and nums[index] != nums[index+1]:
            return nums[index]

            

test_num = [3,3,3,0,2,2,2]
print(singleNumberII(test_num))
