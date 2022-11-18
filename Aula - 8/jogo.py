from os import system, name
import random
jogo = 's'
while(jogo.lower() == 's'):
    system("cls") if(name=='nt') else system('clear')
    print('JOGO: Papel,pedra e tesoura'.center(80,'*'))
    print('\nEscolha a sua opção de jogada:')
    print('[0] Papel\n[1] Pedra\n[2] Tesoura\n')
    jogada = input('->')
    jogada = int(jogada)
    computador = random.randint(0,2)
    opcoes = ["Papel", "Pedra", "Tesoura"]
    resultado = [["Empate","Você ganhou","Você perdeu"],
                 ["Você perdeu","Empate","Você ganhou"],
                 ["Você ganhou","Você perdeu","Empate"]]
    print(resultado[jogada][computador])
    print(f'Você -> {opcoes[jogada]} X {opcoes[computador]} <-Computador')

    jogo = input('\nDeseja jogar novamen? aperte S para continuar:')