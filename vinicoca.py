
while True:
    print("Selecione A1 para comprar uma coca-cola: 4,00 R$")
    print("Selecione B2 para comprar uma fanta: 3,50 R$")
    print("Para entrar no modo adiministrador digite a senha:")
    print("Se deseja sair digite: sair")
    escolha_produto = (input("Digite aqui o código do produto que deseja: "))
    saida = "sair" or "Sair"
    if escolha_produto == "A1" or escolha_produto == "a1":
        coca = 4.0
        print("Sua escolha custa 4.00 R$")
        cédulas2 = 2.0 * int(input("Quantas cedulas de 2 você inseri: "))
        cédulas5 = 5.0 * int(input("Quantas cédulas de 5 você inseri: "))
        moedas1 = 1.0 * int(input("Quantas moedas de 1 você inseri: "))
        moedas50 = 0.5 * float(input("Quantas moedas de 50 você inseri: "))
        valorpago = (cédulas5 + cédulas2 + moedas1 + moedas50)
        if valorpago < coca:
            print("Você não inseriu dinheiro suficiente, compra negada.", valorpago, "R$ será devolvido")
        elif valorpago == coca:
            print("Sua bebida foi dispejada, por favor a retire do recipiente de entrega, e tenha um bom dia.")
            exit()
        elif valorpago > coca:
            valorbebida = (valorpago - coca) 
            print("Sua bebida foi dispejada e seu troco é de:", valorbebida, "R$ por favor os retires de seu recipiente de entrega apropriado e tenha um bom dia.")
            exit()
    elif escolha_produto == "B2" or escolha_produto == "b2":
        fanta = 3.50
        print("Sua escolha custa 3,50 R$")
        cédulas2 = 2.0 * int(input("Quantas cedulas de 2 você inseri: "))
        cédulas5 = 5.0 * int(input("Quantas cédulas de 5 você inseri: "))
        moedas1 = 1.0 * int(input("Quantas moedas de 1 você inseri: "))
        moedas50 = 0.5 * float(input("Quantas moedas de 50 você inseri: "))
        valorpago = (cédulas5 + cédulas2 + moedas1 + moedas50)
        if valorpago < fanta:
            print("Você não inseriu dinheiro suficiente, compra negada.", valorpago, "R$ será devolvido")
        elif valorpago == fanta:
            print("Sua bebida foi dispejada, por favor a retire do recipiente de entrega, e tenha um bom dia.")
            exit()
        elif valorpago > fanta:
            valorbebida = (valorpago - fanta) 
            print("Sua bebida foi dispejada e seu troco é de:", valorbebida, "R$ por favor os retires de seu recipiente de entrega apropriado e tenha um bom dia.")
            exit()
    elif escolha_produto == "ADM" or escolha_produto == "adm":
        print("Bem-Vindo chefe, como podemos ajuda-lo hoje")
        print(" 1 Colocar dinheiro na maquina")
    elif escolha_produto == saida:
        exit()
    else:
        print("Opção não compreendida por favor digite sua opção novamente.")
