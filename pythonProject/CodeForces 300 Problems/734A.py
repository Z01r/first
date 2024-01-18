k=int(input())
n=input()
kolA=0
kolD=0
for i in n:
    if i=='A':
        kolA+=1
    else:
        kolD+=1
if kolA>kolD:
    print('Anton')
if kolA<kolD:
    print('Danik')
if kolA==kolD:
    print('Friendship')
