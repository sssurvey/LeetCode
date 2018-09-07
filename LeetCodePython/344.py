#LeetCode 344
#reverse String

def fn (s):
    list_s = list(s)
    reversed_list = list_s[::-1]
    return "".join(reversed_list)
    
test_1 = "hello"

print(fn(test_1))