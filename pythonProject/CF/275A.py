a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g, h, i = map(int, input().split())
print(str((a + b + d + 1) % 2) + str((a + b + c + e + 1) % 2) + str((b + c + f + 1) % 2))
print(str((a + d + e + g + 1) % 2) + str((b + d + e + f + h + 1) % 2) + str((c + e + f + i + 1) % 2))
print(str((d + g + h + 1) % 2) + str((e + g + h + i + 1) % 2) + str((f + h + i + 1) % 2))
