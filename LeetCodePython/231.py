#leetcod 231
#power of two

def fn(n):
    return n > 0 and n & (n -1) == 0
    
    
    
test_1 = 128
test_2 = 1
test_3 = 6

print(fn(test_1))