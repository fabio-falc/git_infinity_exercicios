# Faça um Programa que leia três números e mostre o maior deles.

print('=== Programa Maior Número ===\n')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 >= num2 and num1 >= num3:
    print(f'O maior número digitado é {num1}')
elif num2 >= num1 and num2 >= num3:
    print(f'O maior número digitado é {num2}')
else:
     print(f'O maior número digitado é {num3}')   