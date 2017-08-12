#LeetCode 485
#Max consecutive ones

def fn(nums):
    counter = 0
    sumValue = 0
    sumList = []
    #flag = False
    
    
    
    
    for i in range(0, len(nums)):
        sumValue += nums[i]
        counter += 1
        
        if sumValue +1 == counter and nums[i] == 0:
            counter = 0
            sumList.append(sumValue)
            sumValue = 0
            
        elif sumValue == counter:
            sumList.append(sumValue)
        
            
    return max(sumList)
    
    
test_1 = [0,0,0,0,1]
test_2 = [1,0,1,1,1,1,0]
test_3 = [0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1]

print (fn(test_3))