valor = float(input('valor do item: '))
qtd = int(input('quantidade: '))
total = valor*qtd
desconto = total * 0.10
total_final = total - desconto
print (f'Total com desconto: R$ {total_final:.2f}')
