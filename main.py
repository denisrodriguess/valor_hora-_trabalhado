# 15 dias 12 horas

horas = int(input('Quantas horas você trabalha por dia ?  '))
dias = int(input('Quantos dias você trabalhou esse mês ?  '))
salario = int(input('Quanto foi seu salario esse mês ?  '))

horas_trabalhadas = horas * dias
# Quantas horas foram trabalhadas 
valor_hora = salario / horas_trabalhadas
print(f'Esse e o seu valor hora do mês passado R$ {valor_hora}')

