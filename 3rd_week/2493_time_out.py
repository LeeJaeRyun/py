def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights:
        height = heights.pop()
        for idx in range(len(heights) - 1, -1, -1):
            if height <= heights[idx]:
                answer[len(heights)] = idx + 1
                break
    return answer

n = int(input())
towers = list(map(int, input().split()))

result = get_receiver_top_orders(towers)
print(*result)