#leetCode 387
#First Unique Char in a Str

def fn (s): #done
    temp_list = list(s)
    if s == 1:
        return 0
    for i in range(0, len(temp_list)):
        if temp_list[i] in temp_list[i+1:len(temp_list)]:
            pass
        elif temp_list[i] in temp_list[0:i]:
            pass
        else:
            return temp_list.index(temp_list[i])
    return -1
             

str_t = "dasfasfdsaf" 

print (fn(str_t))
