#leetCode 371
#Sum of two Integers

def fn (a, b):
    if b>=0:
        for i in range(0,b):
            a +=1
        return a
    if b<0:
        for i in range(0, abs(b)):
            a -= 1
        return a
    
    
    
    
    
test_a = -12
test_b = -8

print (fn(test_a, test_b))