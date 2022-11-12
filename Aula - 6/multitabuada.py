from os import system
system('cls')
tabuada = 11
largura = tabuada * 6
print('Multitabuada'.center(largura,"*"))
for i in range(1, tabuada, 1):
    linha = f"{i:>3} |"
    for j in range(1, 11, 1):
        linha+=f" {j*i:>3} |"
    print(linha)
print(''.center(65,'*'))