input = 20


def find_prime_list_under_number(number):
    result = []
    if number < 2:
        return []
    if number == 2:
        return [2]
    for num in range(2, number+1): #2부터 number까지 반복
        is_prime = True
        for i in range(2,num):#2부터 num-1까지 반복
            if num%i == 0:
                is_prime = False
                break
        if is_prime == True:
            result.append(num)

    return result


result = find_prime_list_under_number(input)
print(result)