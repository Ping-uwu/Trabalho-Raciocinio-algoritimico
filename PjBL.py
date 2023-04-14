quant_cedulas20 = 10
quant_cedulas10 = 10
quant_cedulas5 = 10
quant_cedulas2 = 10
quant_moedas1 = 10
quant_moedas050 = 10
quant_moedas025 = 10
quant_moedas010 = 10
quant_moedas005 = 10

valor_pago = 0
valor_totalpago = 0

while True:
    print("Selecione A1 para comprar uma coca-cola; 4,00 R$")
    print("Para entrar no modo adiministrador digite a senha.")
    print("Se deseja sair digite: exit")
    escolha_produto = (input("Digite aqui o código do produto que deseja: "))

    if escolha_produto == "A1":
        coca = 4.0
        print("Sua escolha custa 4.00 R$")

        while True:
            valor_pago = input("Digite o valor que você deseja adicionar em cédulas ou moedas: (Nota mais alta aceita R$20.00) (Digite '0' para finalizar a adição de valores)")

            if (float(valor_pago) == 20):
                quant_cedulas20 += 1
                valor_totalpago += 20
            elif (float(valor_pago) == 10):
                quant_cedulas10 += 1
                valor_totalpago += 10
            elif (float(valor_pago) == 5):
                quant_cedulas5 += 1
                valor_totalpago += 5
            elif (float(valor_pago) == 2):
                quant_cedulas2 += 1
                valor_totalpago += 2
            elif (float(valor_pago) == 1):
                quant_moedas1 += 1
                valor_totalpago += 1
            elif (float(valor_pago) == 0.5):
                quant_moedas050 += 1
                valor_totalpago += 0.5
            elif (float(valor_pago) == 0.25):
                quant_moedas025 += 1
                valor_totalpago += 0.25
            elif (float(valor_pago) == 0.1):
                quant_moedas010 += 1
                valor_totalpago += 0.1
            elif (float(valor_pago) == 0.05):
                quant_moedas005 += 1
                valor_totalpago += 0.05
            elif (float(valor_pago) == 0):
                break
            else:
                print("Valor digitado invalido.")

        if valor_totalpago < coca:
            print("Você não inseriu dinheiro suficiente, compra negada.", valor_totalpago, "R$ é devolvido")
        elif valor_totalpago == coca:
            print("Sua bebida foi dispejada, por favor a retire do recipiente de entrega, e tenha um bom dia.")
            exit()
        elif valor_totalpago > coca:
            troco = (valor_totalpago - coca)
            print("Sua bebida foi dispejada e seu troco é de:", troco, "R$ por favor os retires de seu recipiente de entrega apropriado e tenha um bom dia.")
            break
    elif escolha_produto == "ADM":
        print("Bem-Vindo chefe, como podemos ajuda-lo hoje")
        print("1 - Verificar quantidade de cedulas em maquina:")
        escolha_admin = input()

        if (escolha_admin == '1'):
            print(quant_cedulas20, " cédulas de R$20.00")
            print(quant_cedulas10, " cédulas de R$20.00")
            print(quant_cedulas5, " cédulas de R$20.00")
            print(quant_cedulas2, " cédulas de R$20.00")
            print(quant_moedas1, " moedas de R$1.00")
            print(quant_moedas050, " moedas de R$0.50")
            print(quant_moedas025, " moedas de R$0.25")
            print(quant_moedas010, " moedas de R$0.10")
            print(quant_moedas005, " moedas de R$0.05")

    elif escolha_produto == "exit":
        exit()
    else:
        print("Opção não compreendida por favor digite sua opção novamente.")
