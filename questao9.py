while menu != '3':
    num = int(input('Digite um número: '))
    menu = input('Digite o número 1 para antecessor e 2 para sucessor e 3 para sair: ')

    if menu == '1':
        antecessor = num - 1
        print(f'O antecessor é {antecessor}')

    if menu == '2':
        sucessor = num + 1
        print(f'O sucessor é {sucessor}')
