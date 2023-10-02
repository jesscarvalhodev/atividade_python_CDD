altura = float(input("Digite a altura: "))
while altura == 0:
    altura = float(input("Digite um valor diferente de 0 para a altura: "))

base = float(input("Digite a base: "))
while base == 0:
    base = float(input("Digite um valor diferente de 0 para a altura: "))

area = (base * altura) / 2
print(f'A área do triangulo é {area}')
