m=int(input())
mat=[[0 for i in range(m)] for j in range(m)]
for l in range(m):
    mat[l]=list(map(int,input().split()))
sch=1
p=list()
while m>sch:
    for z in mat[sch-1]:
        p.append(z)
    mat[sch].clear()
    for i in range(0,m-1-sch):
        mat[i].append(p[i])
    print(*mat[i])
    for i in range(sch,m-1):
        print(mat[i][m])
    sch+=1
