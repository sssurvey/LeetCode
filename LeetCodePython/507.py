#leetcode 507
#perfect number

def fn(num):
    div = 2
    total = 1 #one since there is always div 1

    while div *div <= num:
        if num % div == 0:
            total += div #increase total as adding divs
            if div *div != num:
                total += num /div
        div +=1
        
    if num > 1 and total == num:
        return True
    
    return False
    
            
    
    
    
test_1 = 28
print (fn(test_1))