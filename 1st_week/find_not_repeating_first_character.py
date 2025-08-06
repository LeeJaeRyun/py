input = "abadabac"

def find_not_repeating_first_character(string):
    array = [0] * 26
    for i in string:
        array[ord(i)-ord('a')]+=1
    for i in string:
        if array[ord(i)-ord('a')] == 1:
            return i
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))