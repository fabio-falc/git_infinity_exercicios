#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print('\n=== Programa valor Positivo ou Negativo ===\n')

valor = int(input('Digite um numero: '))

if valor > 0:
    print('O valor digitado é Positivo.')
elif valor < 0:
    print('O valor digitado é Negativo.')    
else:
    print('O valor digitado é Neutro.')
    
print('\n===========================================')