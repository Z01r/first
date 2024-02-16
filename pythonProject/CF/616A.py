n = input()
m = input()
l = max(len(n), len(m))
dn = len(n) - l
dm = len(m) - l
for i in range(l):
    vn = '0'
    if dn + i >= 0:
        vn = n[dn + i]
    vm = '0'
    if dm + i >= 0:
        vm = m[dm + i]
    if vn < vm:
        print("<")
        exit()
    else:
        if vn > vm:
            print(">")
            exit()
print("=")
