# 137
# [2,2,2,1,0,0,0] return 1
# or [2,2,3,2] return 2

def singleNumberII(nums):
    # very slow 900ms +
    num_dict_keyL = []
    num_dict = {}
    for number in nums:
        if number not in list(num_dict.keys()):
            num_dict_keyL.append(number)
    for number in num_dict_keyL:    num_dict[number] = 0
    for number in nums:             num_dict[number] += 1
    for key, value in num_dict.items():
        if value == 1:              return key


def singleNumberIIver2(nums):
    # still slow 900ms +
    nums_unique_list, nums_dict = [],{}
    for number in nums:
        if number not in nums_unique_list:
            nums_unique_list.append(number)
            nums_dict[number] = 1
        else:
            nums_dict[number] += 1
    for key, value in nums_dict.items():
        if value == 1:
            return key

def singleNumberIIver3(nums):
    # faster, still slow, 50ms
    nums = sorted(nums)
    current = nums[0]
    current = nums[0]
    if len(nums) == 1:
        return nums[0]
    elif nums[0] != nums[1]:
        return nums[0]
    elif nums[len(nums)-1] != nums[len(nums)-2]:
        return nums[len(nums)-1]
    for index in range(1, len(nums)-1):
        if nums[index] != nums[index-1] and nums[index] != nums[index+1]:
            return nums[index]



            

test_num = [3,3,3,4,2,2,2]
print(singleNumberIIver3(test_num))
