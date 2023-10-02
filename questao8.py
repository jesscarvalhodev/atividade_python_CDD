qtdNotas = int(input('Digite a quatidade de notas a serem digitadas: '))

soma = 0
for x in range(qtdNotas):
    soma += int(input('Digite uma nota: '))

media = soma / qtdNotas

print(f'A média das notas é {media}')
