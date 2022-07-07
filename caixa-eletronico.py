print('='*39)
print('-----BEM VINDO AO CAIXA ELETRÔNICO-----')
print('='*39)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total = total - cedula
        totcedula = totcedula + 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R${cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('='*39)
print('Volte sempre!')