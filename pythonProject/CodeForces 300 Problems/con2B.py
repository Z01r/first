f = input()
m = input()
sh = input()
k = f + ' ' + m + ' ' + sh
a = [f, m, sh]
y = ['F', 'M', 'S']
if (k == 'rock scissors paper') or (k == 'rock paper scissors') or (k == 'scissors paper rock') or (
        k == 'scissors rock paper') or (k == 'paper scissors rock') or (k == 'paper rock scissors'):
    print('?')
if (k == 'rock rock rock') or (k == 'paper paper paper') or (k == 'scissors scissors scissors'):
    print('?')
if (k == 'rock scissors scissors') or (k == 'scissors rock scissors') or (k == 'scissors scissors rock'):
    for i in range(3):
        if a[i] == 'rock':
            print(y[i])
if (k == 'scissors paper paper') or (k == 'paper scissors paper') or (k == 'paper paper scissors'):
    for i in range(3):
        if a[i] == 'scissors':
            print(y[i])
if (k == 'paper rock rock') or (k == 'rock paper rock') or (k == 'rock rock paper'):
    for i in range(3):
        if a[i] == 'paper':
            print(y[i])
if (k == 'paper scissors scissors') or (k == 'scissors paper scissors') or (k == 'scissors scissors paper'):
    print('?')
if (k == 'paper paper rock') or (k == 'paper rock paper') or (k == 'rock paper paper'):
    print('?')
if (k == 'rock rock scissors') or (k == 'rock scissors rock') or (k == 'scissors rock rock'):
    print('?')
