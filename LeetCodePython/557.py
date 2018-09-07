#LeetCode problem 557
#reverse words in a string III

def fn (s):
    temp_list = s.split()
    final_list = []
    for i in range (0, len(temp_list)):
        final_list.append(temp_list[i][::-1])
        #print (final_list)
        
    final_str = " ".join(final_list)
    return final_str


test_str = "Let's take LeetCode contest"

print(fn(test_str))
