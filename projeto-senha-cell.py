
print('=== Configuração inicial do Celular ===')

senha = input('\nDigite uma senha: ')

confirmacao = input('\nDigite a sua senha: ')

while True:

    if confirmacao == senha:
        print('\nSenha correta. Bem-vindo. ')
        break
    else:
        print('\nSenha incorreta. Tente novamente. ')
        confirmacao = input('\nDigite a sua senha: ')    