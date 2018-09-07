# first approach Big O (N/2) = N
# test passed

def solution(number):
    """take in a number calculate if its palindrome"""
    if number < 0:
        return False
    str_arr = list(str(number))
    str_arr_len = len(str_arr)

    temp_arr_front = []
    temp_arr_back = []
    if str_arr_len ==  1:
        return True
    if str_arr_len == 2:
        return str_arr[0] == str_arr[1]

    if str_arr_len%2 == 1:
        midpoint = int(str_arr_len/2 -0.5 +1)
        temp_arr_front = str_arr[0:midpoint-1]
        temp_arr_back = str_arr[midpoint:str_arr_len]
        for i in range(len(temp_arr_front)):
            if temp_arr_front[i] == temp_arr_back[-i-1]:
                continue
            else:
                return False
    else:
        midpoint = int(str_arr_len/2)
        temp_arr_front = str_arr[0:midpoint]
        temp_arr_back = str_arr[midpoint:str_arr_len]
        for i in range(len(temp_arr_front)):
            if temp_arr_front[i] == temp_arr_back[-i-1]:
                continue
            else:
                return False
    return True

def solution2(number):
    number_str = str(number)
    return number_str == number_str[::-1]

def main():
    number = 101
    answer = solution(number)
    print(answer)
    answer = solution2(number)
    print(answer)

if __name__ == "__main__":
    main()
