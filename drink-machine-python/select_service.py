import variables as var
import stock


def select(number):
    if number == var.TURN_OFF_MACHINE:
        exit(0)
    elif number == var.ADMIN_PASSWORD:
        print('\nADMIN')
        # admin logic
        return
    elif number > var.MAX_POSITION or number < var.MIN_POSITION:
        print('\nBebida ' + str(number) + ' indisponível.')
        return
    print('\n' + stock.DRINK[number]['name'])
    # user logic
