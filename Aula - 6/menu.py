from os import system
system('cls')
print('Faça o seu pedido:\n')
print('1 - Hamburguer')
print('2 - Batata frita')
print('3 - Salada')
print('4 - Refrigerante')
print('x - Para finalizar')
item = ''
pedido = ''
while(item.lower() != 'x'):
    print('\nEscolha o item pelo número')
    item = input('->').lower()
    if(item == '1' or item == '2' or item == '3' or item == '4'):
        pedido+= item + ','
    elif(item=='x'):
        print('Pedido finalizado itens:', pedido)
    else:
        print('Você escolheu um item fora do cardapio')