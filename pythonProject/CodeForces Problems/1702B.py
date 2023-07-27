t=int(input())
for i in range(t):
    sr=input()
    res=0
    s=set()
    for c in sr:
        s.add(c)
        if len(s)==4:
          res+=1
          s={c}
    print(res+1)
