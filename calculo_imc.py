import time
import datetime
import emoji
at = datetime.date.today().year
e = emoji.emojize(':arrow_forward:', use_aliases=True)
e1 = emoji.emojize(':fast_forward:', use_aliases=True)
e2 = emoji.emojize(':black_small_square:', use_aliases=True)
fri1 = '=' * 14
fri = f'{fri1} Índice de Massa Corporal {fri1}'
print(f'\033[1;30m{fri:^50}')
nome = str(input(f'\033[1;35m{e} Digite o seu nome completo: ')).strip().title()
print('')
print(f'\033[1;30mOlá, {nome.split()[0]} {nome.split()[-1]}!')
print('')
a = int(input(f'\033[1;35m{e} Informe o ano de seu nascimento: '))
h = float(input(f'{e} Informe a sua altura (m): '))
p = float(input(f'{e} Informe o seu peso (kg): '))
imc = (p / h ** 2)
i = at - a
cor = msg = ''
print('')
print('\033[1;30mCalculando...')
time.sleep(1)
print('')
if imc < 18.5:
    msg = 'Abaixo do Peso'
    cor = '\033[1;31m'
elif 18.5 <= imc < 25:
    msg = 'Peso Ideal'
    cor = '\033[1;32m'
elif 25 <= imc < 30:
    msg = 'Sobrepeso'
    cor = '\033[1;33m'
elif 30 <= imc < 40:
    msg = 'Obesidade'
    cor = '\033[1;33m'
else:
    msg = 'Obesidade Mórbida'
    cor = '\033[1;31m'
print('¨' * 55)
print(f'{e1} Nome Completo: {nome}')
print(f'{e1} Idade: {i} anos')
print(f'{e1} Altura: {h:.2f} m')
print(f'{e1} Peso: {p} kg')
print('')
print(f'{cor}{e2} IMC: {imc:.1f}')
print(f'{e2} Status: {msg}')
print('\033[1;30m¨' * 55)
