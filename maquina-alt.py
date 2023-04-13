# VARIÁVEIS, LETRA MAIÚSCULA INDICA  SER UMA CONSTANTE
coca_stock = 10
COCA_INDEX = 1
COCA_PRICE = 5
fanta_stock = 5
FANTA_INDEX = 2
FANTA_PRICE = 4
guarana_stock = 3
GUARANA_INDEX = 3
GUARANA_PRICE = 3
MAX_OPTION = 3
MIN_OPTION = 1
ADMIN_PASSWORD = 1234
TURN_OFF_CODE = 9999

# EXECUTA O MENU
while True:
    print('\nBebidas')
    print('1 - Coca-cola')
    print('2 - Fanta')
    print('3 - Guaraná\n')
    drink_number = int(input('Digite o número da bebida: '))
    # DESLIGA A MAQUINA
    if drink_number == TURN_OFF_CODE:
        print('A maquina foi desligada.')
        break
    # ENTRA NO MODO ADMIN
    elif drink_number == ADMIN_PASSWORD:
        print('\nADMIN')
        # admin logic
        continue
    # VERIFICA SE O VALOR É VALIDO
    elif drink_number > MAX_OPTION or drink_number < MIN_OPTION:
        print('\nBebida ' + str(drink_number) + ' indisponível.')
        continue
    # SELECIONA A BEBIDA
    if drink_number == COCA_INDEX:
        print('\nCoca')
        # stock logic
        # cash login
    elif drink_number == FANTA_INDEX:
        print('\nFanta')
        # stock logic
        # cash login
    else:
        print('\nGuaraná')
        # cash login
