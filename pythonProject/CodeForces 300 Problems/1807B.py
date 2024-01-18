for i in range(int(input())):
     n=int(input())
     l=list(map(int,input().split()))
     b=[i for i in l if i%2]
     m=[i for i in l if i%2==0]
     if sum(m)>sum(b):
         print('YES')
     else:
        print('NO')
