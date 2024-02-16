d1, d2, d3 = map(int, input().split())
g = d1 + d2 + d3
s = min(d1, d2) + min(d1 + d2, d3) + min(max(d1, d2), min(d1, d2) + d3)
print(s)
