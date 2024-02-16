n=int(input())
st=0
ob=0
s=input().split()
ob=len(s)*100
for j in s:
    st+=int(j)
print((st/ob)*100)
