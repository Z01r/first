n = int(input())
a = sorted(list(map(int, input().split())))
ans1 = max(a) - min(a)
if max(a) != min(a):
    ans2 = (a.count(max(a))) * (a.count(min(a)))
else:
    ans2 = n * (n-1) // 2
print(ans1, ans2)
