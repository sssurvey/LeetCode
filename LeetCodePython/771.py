# 771 jewels and stones

# solution beat 100% python submissions jul, 5, 2018
# no idea how lol...

def solution(testj, tests):
    counter = 0
    for char in testj:
        for char_s in tests:
            if char == char_s:
                counter+=1
    return counter


j = "aA"
s = "aAABBcccdea"
print(solution(j,s))