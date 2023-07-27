n=int(input())
a,b=zip(*(input().split()for i in ' '*n))
print(sum(a.count(x)for x in b))
