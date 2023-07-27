import os
a, b, c, d = map(str, input().split())
kola = 0
kolb = 0
kolc = 0
kold = 0
for filename in os.listdir("."):
    if filename == a:
        kola += 1
    elif filename == b:
        kolb += 1
    elif filename == c:
        kolc += 1
    elif filename == d:
        kold += 1
print(kola, kolb, kolc, kold)
