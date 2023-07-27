s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
s = s.split()
z = []
for i in s:
    p = i.index(':')
    z.append((i[:p],i[p+1:]))
result = {int(j[0]): j[1] for j in z}
print(result)
