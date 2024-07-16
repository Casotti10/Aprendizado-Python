print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Digite um número: ')) 
razao = int(input('Digite a razão: ')) 
termo = primeiro 
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end= ' ')
        termo += razao
        cont += 1 
    print('PAUSA') 
    mais = int(input('Quantos termos você quer mostrar a mais? ')) 
print('FIM')

    
