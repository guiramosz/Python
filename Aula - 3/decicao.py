from os import system
system('cls')
numero = input('Informe um número:')
if (numero.isnumeric()==True):
    print('Isto é um número')    
    numero = int(numero)
    if print((numero %2) ==1): # % módulo (mod)
        print("Este número é impar")
    else:
        print("Este número é par")
else:
    print('Isto não é um número')
print('Final do código')
