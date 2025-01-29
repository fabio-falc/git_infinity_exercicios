# Faça um Programa que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
# Salário bruto
# Quanto pagou ao INSS.
# Quanto pagou ao sindicato.
# O salário líquido.

# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# Salário Bruto : R$
# IR (11%) : R$
# INSS (8%) : R$
# Sindicato ( 5%) : R$
# Salário Liquido : R$

print('=== Programa para cálculo de salário por hora ===\n')

ganho_hora = float(input('Qual o valor da hora trabalhada: '))
horas_trabalhadas = int(input('Quantidade de  horas trabalhadas este mês: '))
salario_bruto = ganho_hora * horas_trabalhadas

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

desconto = imposto_renda + inss + sindicato
salario_liquido = salario_bruto - desconto

print('\n========= Folha de Pagamento =========')
print(f'Salário Bruto      : R$ {salario_bruto:.2f}')
print(f'IR (11%)           : R$ {imposto_renda:.2f}')
print(f'INSS (8%)          : R$ {inss:.2f}')
print(f'Sindicato (5%)     : R$ {sindicato:.2f}')
print(f'Total de descontos : R$ {desconto:.2f}')
print(f'Salário Liquido    : R$ {salario_liquido:.2f}')
print('=======================================')
