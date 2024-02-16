a = ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]
t = int(input())
h = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]
kol = 0
for _ in range(t):
    k = input()
    if k in a:
        kol += 1
    elif k in h:
        kol += 1
print(kol)
