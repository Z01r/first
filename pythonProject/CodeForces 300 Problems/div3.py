def order_of_problems(n, k):
    order = []

    for i in range(n, n - k, -1):
        order.append(i)

    for i in range(1, n - k + 1):
        order.append(i)

    return order


for _ in range(int(input())):
    n, k = map(int, input().split())
    result = order_of_problems(n, k)
    result.reverse()
    print(*result)
