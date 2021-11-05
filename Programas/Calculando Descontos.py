preço = float(input('Digite o valor do preço de um produto da sua loja: '))
desconto = preço - (preço * 5 / 100)
print('Seu produto com 5% de desconto custara R${:.2f}'.format(desconto))
