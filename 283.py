#LeetCode 283
#Move zeroes

def fn (nums):
    for i in range(0,len(nums)):
        if nums[i] == 0:
            nums.append(0)
            nums.remove(nums[i])
    return nums
    
    
    
test_1 = [1,0,2,3,0,0,0,4]
test_2 = [0,0,0,0,0,0,1]

print(fn(test_1))
