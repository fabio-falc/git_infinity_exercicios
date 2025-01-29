# No Python existe uma forma concisa de se testar valores com apenas uma
# linha de código.
# São os chamados if-ternários, ou condições ternárias, ou operadores ternários.



velocidade = int(input('Digite uma Velocidade: '))

resultado = 'Multado' if velocidade > 60 else 'Dentro do limite'
print(f'Sua velocidade foi de {velocidade} Km/h e o resultado é {resultado}')