h, m = list(map(int, input().split(':')))
n = int(input())
h += ((m + n) // 60)
h = h % 24
m = (m + n) % 60
print(f"{h:02d}:{m:02d}")