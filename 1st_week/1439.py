input = input().strip()


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_0_group = 0
    count_1_group = 0
    prev = None
    for char in string:
        if char!=prev:
            if char == '0':
                count_0_group += 1
            else:
                count_1_group += 1
        prev = char
    return min(count_0_group,count_1_group)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)