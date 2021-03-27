from random import randint
from time import sleep

def comeco():
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(1,3)
    print('''\nSuas opções:
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA''')
    jogador = int(input('Qual sua jogada?: '))
    if jogador <= 3:
        print()

    else:
        print('\nEscreva corretamente')
        comeco()

    print('JO')
    sleep(1)
    print('KEM')
    sleep(1)
    print('PÔ')
    sleep(2)

    print('-=' * 60)

    print(f'Computador jogou: {itens[computador]}')
    print(f'Você jogou: {itens[jogador]}')

    print('-=' * 60)

    if computador == 1:
        if jogador == 1:
            print('EMPATE')

        elif jogador == 2:
            print ('JOGADOR VENCEU!!!')

        elif jogador == 3:
            print('COMPUTADOR VENCEU!')

        else:
            print('Por favor escreva corretamente')
            comeco()

    elif computador == 2:
        if jogador == 1:
            print('COMPUTADOR VENCEU!')

        elif jogador == 2:
            print('EMPATE')

        elif jogador == 3:
            print('VOCÊ VENCEU!!!')

        else:
            print('Por favor escreva corretamente')
            comeco()

    elif computador == 3:
        if jogador == 1:
            print('VOCÊ VENCEU!!!')

        elif jogador == 2:
            print('COMPUTADOR VENCEU!')

        elif jogador == 3:
            print('EMPATE')

        else:
            print('Por favor escreva corretamente')

    else:
        print('Por favor escreva corretamente')
        comeco()

    def sair():
        loop = int(input('''\n[1] - Continuar a jogar
[2] - Sair
Escreva aqui: '''))

        if loop == 1:
            comeco()

        elif loop == 2:
            print('Espero vê-lo novamente')

        else:
            print('Escreva corretamente')
            sair()
    sair()
comeco()