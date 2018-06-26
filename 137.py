# 137
# [2,2,2,1,0,0,0] return 1
# or [2,2,3,2] return 2

def singleNumberII(nums):
    # very slow
    num_dict_keyL = []
    num_dict = {}
    for number in nums:
        if number not in num_dict_keyL:
            num_dict_keyL.append(number)
    for number in num_dict_keyL:    num_dict[number] = 0
    for number in nums:             num_dict[number] += 1
    for key, value in num_dict.items():
        if value == 1:              return key
            

test_num = [1,3,3,3,2,2,2]
print(singleNumberII(test_num))
