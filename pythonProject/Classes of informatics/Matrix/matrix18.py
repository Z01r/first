n,m=map(int,input().split())
k=int(input())
mat=[[0 for i in range(n)] for j in range(m)]
s=0
for i in range(n):
    mat[i]=list(map(int,input().split()))
for t in mat:
    s+=t[k-1]
print(s)
