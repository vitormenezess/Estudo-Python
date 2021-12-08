# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.


def soma(n):
    total = 0
    for v in n:
        total += v
    print(f'A soma dos termos é: {total}')


lista = {}
for i in range(0, 1):
    lista['a'] = int(input('A = '))
    lista['b'] = int(input('B = '))
    lista['c'] = int(input('C = '))
print(lista)
soma(lista.values())