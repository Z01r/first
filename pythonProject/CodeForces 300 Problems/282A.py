n=int(input())
x=0
for i in range(n):
    h=input()
    a=h[0]
    b=h[1]
    c=h[2]
    if a=='X' and b=='-' and c=='-':
        x=x-1
    elif a=='X' and b=='+' and c=='+':
        x=x+1
    elif a=='-' and b=='-' and c=='X':
        x=x-1
    elif a=='+' and b=='+' and c=='X':
        x=x+1
print(x)
