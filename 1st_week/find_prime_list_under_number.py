input = 20


def find_prime_list_under_number(number):
    result = []
    for num in range(2, number+1): #2부터 number까지 반복
        for i in range(2,num):#2부터 num-1까지 반복
            if num%i == 0:
                break
        else:
            result.append(num)

    return result


result = find_prime_list_under_number(input)
print(result)