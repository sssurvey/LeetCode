# all the arry will be sorted
# remove the duplicate
# [1,1,2] will be = [1,2]

# compile error on leetcode
# space complexity = 1

def removeDuplicates(nums):
    current = nums[0] # 1
    other = nums[0] # 1
    return_array = [] # empty
    for item in nums: # bigO N
        if item != other:
            return_array.append(other)
            other = item
        if item == nums[-1] and other not in return_array:
            return_array.append(item)
    return return_array
            
def main():
    test_arr1 = [1,1,1,1,1,1,1,1,222,222,0]
    print(removeDuplicates(test_arr1))

if __name__ == "__main__":
    main()

