m, n = map(int, input().split())

for num in range(m, n+1):
    if num < 2:
        continue
    if num == 2:
        print(2)
        continue
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
