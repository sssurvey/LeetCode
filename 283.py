#LeetCode 283
#Move zeroes

def fn1 (nums): #this function failed, leetcode says its not in place modifications
    for i in range(0,len(nums)):
        if nums[i] == 0:
            nums.append(0)
            nums.remove(nums[i])
    return nums


def fn2 (nums): #passed
    temp = 0
    for i in range(0, len(nums)):
        if nums[i]:
            nums[i] = nums[temp]
            nums[temp] = nums[i]
            temp +=1
            
    return nums
    
    
test_1 = [1,0,2,3,0,0,0,4]
test_2 = [0,0,0,0,0,0,1]

print(fn1(test_1))
print(fn2(test_1))
