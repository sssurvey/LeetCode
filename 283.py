#LeetCode 283
#Move zeroes

def fn (nums):
    for i in range(0,len(nums)):
        if nums[i] == 0:
            nums.append(0)
            nums.pop(nums[i])
    
    
    
    
test_1 = [1,2,3,0,0,0,4]
test_1 = [0,0,0,0,0,0]