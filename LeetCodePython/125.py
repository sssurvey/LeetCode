# 125
# issues with extreme case, the test cases doesnt seems right

def isPalindrome(s):
    """
    s is a string
    return boolean
    """
    str_arr = list(s.lower())
    str_arr_cpy = str_arr[:]
    for char in str_arr:
        if ord(char) in range(97,122) or ord(char) in range(48,57): continue
        else: str_arr_cpy.remove(char)
    return str_arr_cpy[::-1] == str_arr_cpy



test_str = "A man, a plan, a canal: Panama"
test_str2 = "race a car"
print(isPalindrome(test_str2))
    
