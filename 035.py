# 035
# An array of number [1,3,4,6] will be called nums
# A number 5, will be called target
# return should be 2, since in an array
# [ 1 , 3 , 4 , 6 ] // BTW array is sorted
#   0   1   2   3  //position
# thus return 2 since 5 is >3 and <4, thus should be added to pos 2

def solution(nums, target):
    if target > nums[-1]: return len(nums)
    elif target <= nums[0]: return 0
    for index in range(len(nums)):
        if target > nums[index-1] and target <= nums[index]: return index

def solution2(nums, target):
    return len([i for i in nums if i < target])
        
testcase1_arr = [1, 3, 4, 8, 9]
testcase2_arr = [6]
testcase3_arr = [2,3]

print(solution(testcase2_arr, 3))
print(solution2(testcase2_arr, 3))
