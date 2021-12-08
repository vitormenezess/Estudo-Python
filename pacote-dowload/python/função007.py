from datetime import date

def valorPagamento (prestacao, dias):
    total = 0
    juros = (prestacao * (dias * 0.1))/100
    multa = (prestacao * 3) / 100
    if dias == 0:
        return prestacao
    else:
        total = prestacao + multa + juros
        return total


relatorio = list()
dados = list()
while True:
    prest = float(input('Valor da pretação: '))
    if prest == 0:
        break
    dias = int(input('Dias em atrasso: '))
    dados.append(valorPagamento(prest, dias))
    dados.append(dias)
    relatorio.append(dados[:])
    dados.clear()
total = 0
for v in relatorio:
    total += v[0]
print(f'No dia {date.today()} foram pagas {len(relatorio)} pretações totalizando um valor de R${total:.2f}')