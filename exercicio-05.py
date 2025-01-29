# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

print('=== Programa para verificar Vogal ou Consoante ===')
letra = str(input('Digite uma letra: ').lower())

vogal = 'aeiou'

if letra in vogal:
    print('A letra digitada é uma vogal')
else:
    print('A letra digita é uma consoante')    