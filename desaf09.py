print('=== LOJA CASOTTIN ===') 

preco = float(input('Preço das compras: R$')) 
print(''' FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque 
[ 2 ] a vista no cartão
[ 3 ] 2x no cartao 
[ 4 ] 3x ou mais no cartao''')

opcao = int(input('Qual é a opção?: ')) 

if opcao == 1: 
    total = preco - (preco * 10 / 100)  
elif opcao == 2:
    total = preco - (preco * 5 / 100) 
elif opcao == 3:
    total = preco 
elif opcao == 4:
   adicional = preco * 0.20
   total = preco + adicional 
   total_parcela = int(input('Quantas parcelas?'))
   total_parcela = total / total_parcela
   print(f'Sua compra sera parcelada em {total_parcela:.2f}x de R${total}') 

print(f'Sua compra de R${preco} vai custar {total} no final.')