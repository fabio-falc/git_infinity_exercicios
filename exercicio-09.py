# Faça um programa que pergunte o preço de três produtos e
# informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.

print('=== Programa Preço menor ===')

prod1 = float(input('Digite o preço do primeiro produto: '))
prod2 = float(input('Digite o preço do segundo produto: '))
prod3 = float(input('Digite o preco do terceiro produto: '))

if prod1 <= prod2 and prod1 <= prod3:
    menor = prod1
    produto = 'Primeiro'
elif prod2 <= prod1 and prod2 <= prod3:
    menor = prod2
    produto = 'Segundo'
else:
    menor = prod3
    produto = 'Terceiro'        

print(f'O produto a ser comprado é o {produto}, pois ele custa R$ {menor:.2f}')