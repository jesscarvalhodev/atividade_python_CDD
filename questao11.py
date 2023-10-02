idade_anos = int(input('Digite a sua idade: '))
idade_meses = int(input('Digite o mês atual: '))
idade_dias = int(input('Digite o dia atual: '))

dias_totais = idade_dias + (idade_meses * 30) + (idade_anos * 365)

print(f'O total de dias que você viveu foi {dias_totais}')
