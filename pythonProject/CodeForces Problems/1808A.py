for s in[*open(0)][1:]:
 l,r=map(int,s.split());m=-1
 while m<9and l<=r:
  a=*map(ord,str(l)),;t=max(a)-min(a)
  if t>m:m=t;p=l
  l+=1
 print(p)
