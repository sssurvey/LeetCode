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
    mask = 0xffffffff
    maximum = 0x7fffffff
    
    while b != 0:
        temp = (a ^ b) & mask
        b = ((a & b) << 1) & mask
        a = temp
    
    if a <= maximum:
        return a
    else:
        return ~(a ^ mask)
    
    
    
    
test_a = -12
test_b = -8

print (fn1(test_a, test_b))