# 035
# An array of number [1,3,4,6] will be called nums
# A number 5, will be called target
# return should be 2, since in an array
# [ 1 , 3 , 4 , 6 ] // BTW array is sorted
#   0   1   2   3  //position
# thus return 2 since 5 is >3 and <4, thus should be added to pos 2

def solution(nums, target):
    if len(nums) == 1 and nums[0] >= target:
        return 0
    elif len(nums) == 1 and nums[0] < target:
        return 1
    mid = int(len(nums)/2)
    if nums[mid] == target:
        return nums
    if nums[mid] > target:
        while True:
            
        
    
    
    
            
testcase1_arr = [1, 3, 4, 5, 6]
testcase2_arr = [6]
testcase3_arr = [2,3]

print(solution(testcase3_arr, 1))
