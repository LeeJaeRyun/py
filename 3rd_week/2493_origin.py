def get_receiver_top_orders(heights):
    stack = []
    answer = [0] * len(heights)

    for i in range(len(heights)):
        while stack and stack[-1][1] <= heights[i]:
            stack.pop()
        if stack:
            answer[i] = stack[-1][0] + 1
        stack.append([i, heights[i]])

    return answer

n = int(input())
towers = list(map(int, input().split()))

result = get_receiver_top_orders(towers)
print(*result)
