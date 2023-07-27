def MinElem(a, n):
    n = min(a)
    return n

n=int(input())
a = list(map(int, input().split()))
print(MinElem(a,n))