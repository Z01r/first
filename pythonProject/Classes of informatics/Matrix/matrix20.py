for s in [*open(0)][1:]:
    a,b=map(int,s.split())
print((max(max(a,b),2*min(a,b)))**2)