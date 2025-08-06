input = 20


def find_prime_list_under_number(number):
    result = []
    for num in range(2, number+1): #2부터 number까지 반복
        for i in result:#소수로만 구성, num=2일 경우 result는 비었기 때문에 바로 result 리스트에 2값이 추가됌
            if num%i == 0:
                break
        else:
            result.append(num)

    return result


result = find_prime_list_under_number(input)
print(result)