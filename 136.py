#LeetCode 136
#Single Number

def fn (nums):
    
    #temp_list2 = nums
    #print (len(nums))
    
    for i in range (0, len(nums)): #this function exceeded time limit
        
        temp_list = nums[:]
        
        
        #print ("fresh ",temp_list)
        
        temp_list.pop(i)
        
        #print (temp_list)
        #print ("this is:",nums[i])
        
        if nums[i] in temp_list:
            #print ("not unique:", nums[i])
            pass
        else:
            #print ("unique:", nums[i])
            return nums[i]
        
    return -1


    
test_case = [1,1,2,2,3,3,4,4,5,5,6,6,7,8,10,10,8]
print ("Function 1.0:", fn(test_case))
print ("Function 2.0:",fn2(test_case))
