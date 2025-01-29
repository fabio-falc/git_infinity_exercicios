# 1.Faça um Programa que verifique se uma letra digitada é "F"
# ou
#    "M". Conforme a letra escrever:
#    F - Feminino,
#    M - Masculino,
#    Outra letra qualquer - Sexo Inválido.

print('\n=== Programa para verificar Sexo ===\n')

letra = str(input('Digite a letra do Sexo (F para Feminino , M para Masculino): ').upper())

if letra == 'F':
    sexo = 'FEMININO'
    print(f'O sexo digitado é {sexo}')
elif letra == 'M':
    sexo = 'MASCULINO'
    print(f'O sexo digitado é {sexo}')
else:
    sexo = 'INVÁLIDO'
    print(f'Sexo {sexo}, Digite apenas "F" ou "M" ')

print('\n====================================')    