def exercicio_1(n):
    for j in range(1, n+1):
        for i in range(1, j+1):
            print(f'{str(i)} ', end='')
        print()

num = int(input('Informe um numero: '))
exercicio_1(num)
