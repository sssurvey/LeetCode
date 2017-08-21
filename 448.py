#leetcode 448
#find all numbers disappeared in an Array

def fn (nums):
    list_1_sorted = sorted(nums)
    ans_list = []
    for i in range(1, len(list_1_sorted)):
        if i != list_1_sorted[i]:
            ans_list.append(i)
    return ans_list
    


    
test_1 = [4,3,2,7,8,2,3,1]
print(fn(test_1))
