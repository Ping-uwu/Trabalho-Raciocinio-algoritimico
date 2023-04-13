import select_service as service
import stock


def print_drinks():
    print('\nBebidas:')
    for key, value in stock.DRINK.items():
        print(str(key) + ': ' + value['name'] + ' - qnt: ' + str(value['stock']))
    print()


def main():
    print()
    # menu
    while True:
        print_drinks()
        try:
            service.select(int(input("Digite o número da bebida: ")))
        except:
            print('A maquina foi desligada ou ocorreu algum erro.')
            return


if __name__ == '__main__':
    main()
