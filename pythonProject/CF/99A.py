a,b=input().split('.')
a,b=int(a),int(b[0])
l=a%10
if b>4 and l<9:
    print(int(a)+1)
elif l==9:
    print('GOTO Vasilisa.')
elif b<5:
    print(int(a))
