#LeetCode problem 520
#Detect Capital

def fn (word):
    word_list = list(word)
    flag = False
    
    #some hotfix
    if len(word) == 1:
        return True
    
    if len(word) ==2:
        if word[0].isupper() == word[1].isupper():
            return True
        elif word[0].isupper() and word[1].islower():
            return True
        else:
            return False
    
    
    
    if word_list[0].islower() is True:
        for i in range(0, len(word_list)-1):
            if word_list[i].islower() and word_list[i+1].islower():
                flag = True
                print ("lower ^ lower, start with lower -> ", flag)
            else:
                flag = False
                return flag
        return flag
