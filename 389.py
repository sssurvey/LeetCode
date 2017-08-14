#LeetCode 389
#Find the Difference

def fn (s, t):
    list_s = list(s)
    list_t = list(t)
    
    #list_s.sort()
    #list_t.sort()
    
    #print (list_s)
    #print (list_t)
    
    for i in range(0, len(list_t)):
        if list_t[i] not in list_s:
            return list_t[i]
        elif list_t[i] in list_s:
            list_s.remove(list_t[i])
        
    
    

sss = "abcdee"
ttt = "abxcdee"


sss1 = "a"
ttt1 = "aa"

print(fn(sss1,ttt1))