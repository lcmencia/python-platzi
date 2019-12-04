
def foreign_exchange_calculator(ammount):
    usd_to_gs_rate = 6360

    return usd_to_gs_rate * ammount

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte dolares a guaranies.')
    print('')
    ammount = float(input('Ingresa la cantidad de dolares que quieres convertir'))

    result = foreign_exchange_calculator(ammount)

    print('${} dolares son ${} guaranies'.format(ammount, result))
    print('')
if __name__ == '__main__':
    run()