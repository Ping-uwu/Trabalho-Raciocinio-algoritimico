while True:
    print("Selecione A1 para comprar uma coca-cola; 4,00 R$")
    print("Para entrar no modo adiministrador digite a senha.")
    print("Se deseja sair digite: exit")
    escolha_produto = (input("Digite aqui o código do produto que deseja: "))

    if escolha_produto == "A1" or "a1":
        coca = 4.0
        print("Sua escolha custa 4.00 R$")
        cédulas2 = 2.0 * int(input("Quantas cedulas de 2 você inseri: "))
        cédulas5 = 5.0 * int(input("Quantas cédulas de 5 você inseri: "))
        moedas1 = 1.0 * int(input("Quantas moedas de 1 você inseri: "))
        moedas50 = 0.5 * float(input("Quantas moedas de 50 você inseri: "))
        valorpago = (cédulas5 + cédulas2 + moedas1 + moedas50)
        if valorpago < coca:
            print("Você não inseriu dinheiro suficiente, compra negada.", valorpago, "R$ é devolvido")
        elif valorpago == coca:
            print("Sua bebida foi dispejada, por favor a retire do recipiente de entrega, e tenha um bom dia.")
            exit()
        elif valorpago > coca:
            valorbebida = (valorpago - coca) 
            print("Sua bebida foi dispejada e seu troco é de:", valorbebida, "R$ por favor os retires de seu recipiente de entrega apropriado e tenha um bom dia.")
            exit()
    elif escolha_produto == "ADM" or "adm":
        print("Bem-Vindo chefe, como podemos ajuda-lo hoje")
        print(" 1 Colocar dinheiro na maquina")
    elif escolha_produto == "exit" or "Exit":
        exit()
    else:
        print("Opção não compreendida por favor digite sua opção novamente.")
