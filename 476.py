test1 = 321
test2 = 32141
test3 = 453

def fn1 (n):
    b ="{0:b}".format(n)
    #int_b = int(b)
    
    #print (type(b))
    #print (type(int_b))
    final = 0
    
    list_b = list(map(int,b))
    #print (list_b)
    
    for i in range(0, len(list_b)):
        if list_b[i] == 0:
            list_b[i] = 1
        else:
            list_b[i] = 0
        #print (list_b)
    i = len(list_b)
    
    for i in range(0, len(list_b)):
        final += list_b[len(list_b)-1-i]*(2**i)
        print (list_b[i],"the current bin")
        print (final,'after addition')
    
    
    return final

fn1(test2)
