#Faça um Programa que peça dois números e imprima o maior deles.


print('=== Programa para imprimir o mair número ===\n')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 >= num2:
    print(f'\nO maior número digitado foi: {num1}')
else:
    print(f'\nO maior número digitado foi: {num2}')
print('===========================================')    