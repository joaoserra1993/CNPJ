"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""

import re

cnpj_av = input('Insira o CNPJ a validar: ')
cnpj_av2 = (re.sub(r'[^0-9]', '', cnpj_av))

cnpj_av2 = [int(x) for x in str(cnpj_av2)]
num = cnpj_av2[0:12:1]
cnpj = cnpj_av2

fac1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
fac2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

f1 = sum([x * y for x, y in zip(num, fac1)])
n1 = 1 if 11 - (f1 % 11) <= 9 else 0
num1 = num + [n1]

f2 = sum([x * y for x, y in zip(num1, fac2)])
n2 = 1 if 11 - (f2 % 11) <= 9 else 0
num2 = num1 + [n2]

print('Validado.') if num2 == cnpj else print('Não validado.')
