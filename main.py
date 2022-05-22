ru=0
print('Bem vindo a loja da Lívia')
valorProduto = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))
subtotal = valorProduto * quantidade
if quantidade < 9:
 desconto = 0 # Valor final do produto sem o desconto.
elif 10 <= quantidade < 99:
 desconto = 0.5 # Valor final do produto com 5% de desconto.
elif 100 <= quantidade < 999:
 desconto = 0.10 # Valor final do produto com 10% de desconto.
else: # Caso a quantidade seja acima de 1000, entrará no próximo passo e usará o else.
 desconto = 0.15 # Valor final do produto com 15% de desconto.
semDesconto = valorProduto * quantidade # Calcula o valor do produto total, sem desconto aplicado.
comDesconto = semDesconto - semDesconto * desconto # Calcula o valor do produto total, com desconto aplicado.
print('O valor do produto sem desconto foi de R$ {:.2f}'.format(semDesconto))
print('O valor do produto com desconto foi de R$ {:.2f}'.format(comDesconto, desconto))
print('A loja da Lívia agradece a sua preferência!')