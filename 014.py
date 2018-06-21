# 014
# Longest Common prefix

def solution(temp_strs_list):
    """
    para 0: strs is an array of String

    this function will return the common longest prefix these string
    in the strs[] is sharing

    return a string contains the prefix
    """
    return_str = ""
    current_char = ""
    # only use one string as the sample
    # leetcode seems to have some issus, have to put another try except outside
    # ugly, but beat 97.87% of other submission Jan 21, 2018
    try:
        for index in range(len(temp_strs_list[0])):
            try:
                current_char = temp_strs_list[0][index]
                for other_str in temp_strs_list[1:]:
                    if current_char == other_str[index]:
                        continue
                    elif current_char != other_str[index]:
                        return return_str
                return_str = return_str + current_char
            except (IndexError):
                return return_str
    except (IndexError):
        return return_str
    return return_str


print(solution(["h", "haa", "haa"]))
