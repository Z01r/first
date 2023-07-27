n=int(input())
x=input().split()
y=input().split()
a=(x[1:]+y[1:])
a=set(a)
if(len(a)==n):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
    
