import math
import sys

def leia_numero(texto):
    while True:
        try:
            valor = input(texto).strip().replace(',', '.')
            return float(valor)
        except:
            print('Entrada inválida, tente novamente.')

def leia_percentual(texto):
    while True:
        v = leia_numero(texto)
        return v / 100.0

def soma():
    a = leia_numero('Primeiro número: ')
    b = leia_numero('Segundo número: ')
    print('Resultado:', a + b)

def subtracao():
    a = leia_numero('Minuendo: ')
    b = leia_numero('Subtraendo: ')
    print('Resultado:', a - b)

def multiplicacao():
    a = leia_numero('Primeiro número: ')
    b = leia_numero('Segundo número: ')
    print('Resultado:', a * b)

def divisao():
    a = leia_numero('Dividendo: ')
    b = leia_numero('Divisor: ')
    if b == 0:
        print('Erro: divisão por zero')
        return
    print('Resultado:', a / b)

def juros_simples():
    c = leia_numero('Capital (C): ')
    i = leia_percentual('Taxa anual (%) : ')
    t = leia_numero('Tempo (anos): ')
    j = c * i * t
    m = c + j
    print('Juros:', round(j, 6))
    print('Montante:', round(m, 6))

def juros_compostos():
    c = leia_numero('Capital (C): ')
    i = leia_percentual('Taxa por período (%) : ')
    n = int(leia_numero('Número de períodos: '))
    m = c * ((1 + i) ** n)
    print('Montante:', round(m, 6))

def valor_presente_composto():
    fv = leia_numero('Valor futuro (FV): ')
    i = leia_percentual('Taxa por período (%) : ')
    n = int(leia_numero('Número de períodos: '))
    pv = fv / ((1 + i) ** n)
    print('Valor presente (PV):', round(pv, 6))

def valor_futuro_anuidade():
    pmt = leia_numero('Pagamento periódico (PMT): ')
    i = leia_percentual('Taxa por período (%) : ')
    n = int(leia_numero('Número de períodos: '))
    if i == 0:
        fv = pmt * n
    else:
        fv = pmt * (((1 + i) ** n - 1) / i)
    print('Valor futuro da anuidade (FV):', round(fv, 6))

def valor_presente_anuidade():
    pmt = leia_numero('Pagamento periódico (PMT): ')
    i = leia_percentual('Taxa por período (%) : ')
    n = int(leia_numero('Número de períodos: '))
    if i == 0:
        pv = pmt * n
    else:
        pv = pmt * (1 - (1 + i) ** -n) / i
    print('Valor presente da anuidade (PV):', round(pv, 6))

def pmt_emprestimo():
    pv = leia_numero('Valor do empréstimo (PV): ')
    i = leia_percentual('Taxa por período (%) : ')
    n = int(leia_numero('Número de períodos: '))
    if i == 0:
        pmt = pv / n
    else:
        pmt = (i * pv) / (1 - (1 + i) ** -n)
    print('Parcela periódica (PMT):', round(pmt, 6))

def amortizacao_price():
    pv = leia_numero('Valor do empréstimo (PV): ')
    i = leia_percentual('Taxa por período (%) : ')
    n = int(leia_numero('Número de períodos: '))
    if i == 0:
        pmt = pv / n
        saldo = pv
        for perio in range(1, n + 1):
            amort = pmt
            juros = 0
            saldo -= amort
            print(perio, round(pmt, 2), round(amort, 2), round(juros, 2), round(max(saldo, 0), 2))
        return
    pmt = (i * pv) / (1 - (1 + i) ** -n)
    saldo = pv
    for perio in range(1, n + 1):
        juros = saldo * i
        amort = pmt - juros
        saldo -= amort
        print(perio, round(pmt, 2), round(amort, 2), round(juros, 2), round(max(saldo, 0), 2))

def amortizacao_sac():
    pv = leia_numero('Valor do empréstimo (PV): ')
    i = leia_percentual('Taxa por período (%) : ')
    n = int(leia_numero('Número de períodos: '))
    amort_const = pv / n
    saldo = pv
    for perio in range(1, n + 1):
        juros = saldo * i
        pmt = amort_const + juros
        saldo -= amort_const
        print(perio, round(pmt, 2), round(amort_const, 2), round(juros, 2), round(max(saldo, 0), 2))

def taxa_nominal_para_efetiva():
    r = leia_percentual('Taxa nominal anual (%): ')
    m = int(leia_numero('Número de capitalizações por ano: '))
    efetiva = (1 + r / m) ** m - 1
    print('Taxa efetiva anual:', round(efetiva * 100, 8), '%')

def taxa_efetiva_para_nominal():
    re = leia_percentual('Taxa efetiva anual (%): ')
    m = int(leia_numero('Número de capitalizações por ano: '))
    nominal = m * ((1 + re) ** (1 / m) - 1)
    print('Taxa nominal anual equivalente:', round(nominal * 100, 8), '%')

def reajuste_inflacao():
    valor = leia_numero('Valor atual: ')
    infl = leia_percentual('Taxa de inflação anual (%): ')
    anos = int(leia_numero('Anos: '))
    novo = valor * ((1 + infl) ** anos)
    print('Valor corrigido pela inflação:', round(novo, 6))

def retorno_sobre_investimento():
    ganho = leia_numero('Ganho obtido: ')
    investimento = leia_numero('Investimento inicial: ')
    if investimento == 0:
        print('Investimento inicial zero')
        return
    roi = (ganho - investimento) / investimento
    print('ROI:', round(roi * 100, 6), '%')

def menu():
    print('''
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Juros simples (Capital, Juros, Montante)
6 - Juros compostos (Montante)
7 - Valor presente (composto)
8 - Valor futuro de anuidade
9 - Valor presente de anuidade
10 - Parcela de empréstimo (PMT)
11 - Amortização Price (tabela)
12 - Amortização SAC (tabela)
13 - Taxa nominal → efetiva
14 - Taxa efetiva → nominal
15 - Reajuste pela inflação
16 - ROI (Retorno sobre investimento)
0 - Sair
''')

def main():
    while True:
        menu()
        op = input('Escolha uma opção: ').strip()
        if op == '1':
            soma()
        elif op == '2':
            subtracao()
        elif op == '3':
            multiplicacao()
        elif op == '4':
            divisao()
        elif op == '5':
            juros_simples()
        elif op == '6':
            juros_compostos()
        elif op == '7':
            valor_presente_composto()
        elif op == '8':
            valor_futuro_anuidade()
        elif op == '9':
            valor_presente_anuidade()
        elif op == '10':
            pmt_emprestimo()
        elif op == '11':
            amortizacao_price()
        elif op == '12':
            amortizacao_sac()
        elif op == '13':
            taxa_nominal_para_efetiva()
        elif op == '14':
            taxa_efetiva_para_nominal()
        elif op == '15':
            reajuste_inflacao()
        elif op == '16':
            retorno_sobre_investimento()
        elif op == '0':
            print('Saindo')
            sys.exit()
        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()