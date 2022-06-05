def e_bissexto(ano):
    if ano % 400 == 0:
        return True
    if ano % 100 == 0:
        return False
    if ano % 4 == 0:
        return True
    return False

def data_em_dias(data: tuple):
    dia, mes, ano = data
    if e_bissexto(ano):
        diasFev = 29
    else:
        diasFev = 28
    vetor = [31, diasFev, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dias = 0
    dias += dia
    for i in range(mes-1):
        dias += vetor[i]
    for i in range(ano):
        dias += 366 if e_bissexto(i) else 365
    return dias

data1 = tuple(int(i) for i in str(input('Data 1 >> ')).strip().split('/'))
data2 = tuple(int(i) for i in str(input('Data 2 >> ')).strip().split('/'))

resultado = data_em_dias(data2) - data_em_dias(data1)
print('Dias de diferença:', resultado if resultado > 0 else - resultado)
