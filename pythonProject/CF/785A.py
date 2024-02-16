a = ["Tetrahedron", "Cube", "Octahedron", "Dodecahedron", "Icosahedron"]
b = [4, 6, 8, 12, 20]
s = 0
for _ in range(int(input())):
    n = input()
    s += b[a.index(n)]
print(s)
