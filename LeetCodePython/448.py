#leetcode 448
#find all numbers disappeared in an Array

def fn (nums):
    for n in nums:
        nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
    
    return [i+1 for i, n in enumerate(nums) if n > 0]


    
test_1 = [4,3,2,7,8,2,3,1]
print(fn(test_1))
