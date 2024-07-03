from random import randint
itens = ('Pedra', 'Papel', 'Tesoura') 
computador = randint(0, 2) 
print('''Sua opções:
[0] PEDRA 
[1] TESOURA
[2] PAPEL
''') 

jogador = int(input('Qual é a sua jogada? '))
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')  

if computador == 0: #jogou PEDRA 
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2: 
        print('COMPUTADOR VENCE')
    else:
        print('[ERRO]')
elif computador == 1: #jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2: 
        print('JOGADOR VENCEU')
    else:
        print('[ERRO]')
elif computador == 2: #jogou  TESOURA 
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2: 
       print('EMPATE')
    else:
        print('[ERRO]')

