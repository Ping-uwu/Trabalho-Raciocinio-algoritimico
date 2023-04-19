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
coin1_stock = 10
coin05_stock = 50
bill2_stock = 20
bill5_stock = 10
bill10_stock = 5

# EXECUTA O MENU
while True:
    print('\nBebidas')
    print('1 - Coca-cola')
    print('2 - Fanta')
    print('3 - Guaraná\n')
    drink_number = int(input('Digite o número da bebida ou senha de ADMIN: '))
    # DESLIGA A MAQUINA
    if drink_number == TURN_OFF_CODE:
        print('\nA maquina foi desligada.')
        break
    # ENTRA NO MODO ADMIN
    elif drink_number == ADMIN_PASSWORD:
        # MENU ADMIN
        while True:
            choice = int(input('\nDigite 1 para gerenciar as bebidas, 2 para gerenciar o dinheiro ou 3 para sair do modo ADMIN: '))
            if choice == 1:
                coca = int(input('\nDigite a alteração no estoque de Coca: '))
                if (coca_stock + coca) < 0:
                    print('\nValor inválido.')
                else:
                    coca_stock += coca
                    print(coca_stock)
                fanta = int(input('\nDigite a alteração no estoque de Fanta: '))
                if fanta_stock + fanta < 0:
                    print('\nValor inválido.')
                else:
                    fanta_stock += fanta
                    print(fanta_stock)
                guarana = int(input('\nDigite a alteração no estoque de Guaraná: '))
                if guarana_stock + guarana < 0:
                    print('\nValor inválido.')
                else:
                    guarana_stock += guarana
                    print(guarana_stock)
            elif choice == 2:
                coin1 = int(input('\nDigite a alteração no estoque de moedas de 1: '))
                if (coin1_stock + coin1) < 0:
                    print('\nValor inválido.')
                else:
                    coin1_stock += coin1
                    print(coin1_stock)
                coin05 = int(input('\nDigite a alteração no estoque de moedas de 0.5: '))
                if coin05_stock + coin05 < 0:
                    print('\nValor inválido.')
                else:
                    coin05_stock += coin05
                    print(coin05_stock)
                bill2 = int(input('\nDigite a alteração no estoque de notas de 2: '))
                if bill2_stock + bill2 < 0:
                    print('\nValor inválido.')
                else:
                    bill2_stock += bill2
                    print(bill2_stock)
                bill5 = int(input('\nDigite a alteração no estoque de notas de 5: '))
                if bill5_stock + bill5 < 0:
                    print('\nValor inválido.')
                else:
                    bill5_stock += bill5
                    print(bill5_stock)
                bill10 = int(input('\nDigite a alteração no estoque de notas de 10: '))
                if bill10_stock + bill10 < 0:
                    print('\nValor inválido.')
                else:
                    bill10_stock += bill10
                    print(bill10_stock)
            elif choice == 3:
                print('\nSaindo do modo ADMIN.')
                break
            else:
                print('\nValor invalido digite 1, 2 ou 3.')

    # SELECIONA A BEBIDA E VERIFICA SE O VALOR É VALIDO
    elif drink_number == COCA_INDEX:
        print('\nBebida selecionada: Coca - R$' + COCA_PRICE.__str__())
        if coca_stock == 0:
            print('\nTodas as Cocas acabaram :(')
        # stock logic
        # cash logic
    elif drink_number == FANTA_INDEX:
        print('\nBebida selecionada: Fanta - R$' + FANTA_PRICE.__str__())
        if fanta_stock == 0:
            print('\nTodas as Fantas acabaram :(')
        # stock logic
        # cash logic
    elif drink_number == GUARANA_INDEX:
        print('\nBebida selecionada: Guaraná - R$' + GUARANA_PRICE.__str__())
        if guarana_stock == 0:
            print('\nTodas os Guaranas acabaram :(')
        # cash logic
    else:
        print('\nBebida ' + str(drink_number) + ' indisponível.')
