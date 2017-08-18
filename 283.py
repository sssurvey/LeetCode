#LeetCode 283
#Move zeroes

def fn1 (nums): #this function failed, leetcode says its not in place modifications
#I understand the instruction wrong, both function passes the test, both function works, just do not return anything. leetcode prob.283 does not accept function that return objects
    for i in range(0,len(nums)):
        if nums[i] == 0:
            nums.append(0)
            nums.remove(nums[i])
    return nums #this line is not needed when answering


def fn2 (nums): #passed
    temp = 0
    for i in range(0, len(nums)):
        if nums[i]:
            nums[i] = nums[temp]
            nums[temp] = nums[i]
            temp +=1
            
    return nums #this line is not needed when answering
    
    
test_1 = [1,0,2,3,0,0,0,4]
test_2 = [0,0,0,0,0,0,1]

print(fn1(test_1))
print(fn2(test_1))
