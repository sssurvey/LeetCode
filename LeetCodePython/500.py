#leetCode problem 500
#Keyboard Row

r1 = list('qwertyuiopQWERTYUIOP')
r2 = list('asdfghjklASDFGHJKL')
r3 = list('zxcvbnmZXCVBNM')
#print (r1[10])


def fn1 (l):
    list_char = []
    flag = False
    final = []
    print (l)
    for i in range (0, len(l)):
        list_char.append(list(l[i]))
        
        
    x = 0
        
    print(list_char)
    for i in range(0, len(l)):
            if list_char[i][0] in r1:
                while x in range(0, len(list_char[i])):
                    if list_char[i][x] in r1:
                        x += 1
                        print ("list_char",i,"check", "fit")
                        flag = True
                    else:
                        print ("NOT working")
                        flag = False
                        break
                if flag == True:
                    final.append(l[i])
                    flag = False
                x = 0
                
                    
                
            if list_char[i][0] in r2:
                while x in range(0, len(list_char[i])):
                    if list_char[i][x] in r2:
                        x += 1
                        print ("list_char",i,"check", "fit")
                        flag = True
                    else:
                        print ("NOT working")
                        flag = False
                        break
                if flag == True:
                    final.append(l[i])
                    flag = False
                x = 0
                    
                    
                
            if list_char[i][0] in r3:
                 while x in range(0, len(list_char[i])):
                    if list_char[i][x] in r3:
                        x += 1
                        print ("list_char",i,"check", "fit")
                        flag = True
                    else:
                        print ("NOT working")
                        flag = False
                        break
                 if flag == True:
                    final.append(l[i])
                    flag = False
                 x = 0
                    
    #print (len(l))
    return final                
    
                
             
            
    #return final

test_list = ["qwwerwq","dafsasfda","Zcxvzxcxzv","zxc"]

print(fn1(test_list))
