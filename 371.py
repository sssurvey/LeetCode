#leetCode 371
#Sum of two Integers

def fn (a, b): #not working, this has a mem problem when input 2147483647 and -2147483647
    if b>=0:
        for i in range(0,b):
            a +=1
        return a
    if b<0:
        for i in range(0, abs(b)):
            a -= 1
        return a
    
def fn1 (a, b):
    pass
    
    
    
    
    
test_a = -12
test_b = -8

print (fn(test_a, test_b))