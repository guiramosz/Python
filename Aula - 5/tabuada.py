from os import system, name
#if ternario (if escrito em uma linha só não pode ter elif)
system('cls') if(name == 'nt') else system('clear')
#igual ao comando de cima
if(name == 'nt'):
    system('cls')
else:
    system('clear')
tabuada = 6
for i in range(11):
    #print('{} x {} = {}'.format(tabuada, i, tabuada *i))
    print(f"{tabuada: >2} x {i: >2} = {(tabuada * i):>3}")
    #print(tabuada, 'x', i, '=', tabuada * i)