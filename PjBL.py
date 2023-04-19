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

coca_preco = 4
coca_stock = 10
fanta_preco = 3.5
fanta_stock = 10
guarana_preco = 5.5
guarana_stock = 10

valor_bebida = 0

while True:
    print("Selecione A1 para comprar uma coca-cola: R$", float(coca_preco))
    print("Selecione B2 para comprar uma fanta laranja: R$", float(fanta_preco))
    print("Selecione C3 para comprar um guaraná: R$", float(guarana_preco))
    print("Para entrar no modo adiministrador digite a senha.")
    print("Se deseja sair digite: 0")
    escolha_produto = (input("Digite aqui o código do produto que deseja: "))
    print()

    if (escolha_produto == "A1") or (escolha_produto == "B2") or (escolha_produto == "C3"):

        if(escolha_produto == "A1"):
            valor_bebida = coca_preco
        elif(escolha_produto == "B2"):
            valor_bebida = fanta_preco
        else:
            valor_bebida = guarana_preco
        
        while True:

            if(escolha_produto == "A1") and (coca_stock == 0):
                print("Produto indisponivel :(")
                break
            elif(escolha_produto == "B2") and (fanta_stock == 0):
                print("Produto indisponivel :(")
                break
            elif(escolha_produto == "C3") and (guarana_stock == 0):
                print("Produto indisponivel :(")
                break

            print("Sua escolha custa: R$", valor_bebida)
            print()

            while True:
                valor_pago = input("Digite o valor que você deseja adicionar em cédulas ou moedas: (Nota mais alta aceita R$20.00) (Digite '0' para finalizar a adição de valores)")
                print()

                if (valor_pago == '20'):
                    quant_cedulas20 += 1
                    valor_totalpago += 20
                elif (valor_pago == '10'):
                    quant_cedulas10 += 1
                    valor_totalpago += 10
                elif (valor_pago == '5'):
                    quant_cedulas5 += 1
                    valor_totalpago += 5
                elif (valor_pago == '2'):
                    quant_cedulas2 += 1
                    valor_totalpago += 2
                elif (valor_pago == '1'):
                    quant_moedas1 += 1
                    valor_totalpago += 1
                elif (valor_pago == '0.5'):
                    quant_moedas050 += 1
                    valor_totalpago += 0.5
                elif (valor_pago == '0.25'):
                    quant_moedas025 += 1
                    valor_totalpago += 0.25
                elif (valor_pago == '0.1'):
                    quant_moedas010 += 1
                    valor_totalpago += 0.1
                elif (valor_pago == '0.05'):
                    quant_moedas005 += 1
                    valor_totalpago += 0.05
                elif (valor_pago == '0'):
                    break
                else:
                    print()
                    print("Valor digitado invalido.")
                    print()

            print()
            print("Valor em maquina: R$", valor_totalpago)
            print()
            if valor_totalpago < valor_bebida:
                print("Você não inseriu dinheiro suficiente, compra negada.")
                print()
                print("Saldo em maquina atualizado: R$", valor_totalpago)
                print()
            elif valor_totalpago == valor_bebida:
                print("Compra realizada com sucesso! Retire sua bebida.")
                valor_totalpago = 0
                print("Saldo em maquina atualizado: R$", valor_totalpago)
                if(escolha_produto == "A1"):
                    coca_stock -= 1
                    break
                elif(escolha_produto == "B2"):
                    fanta_stock -= 1
                    break
                elif(escolha_produto == "C3"):
                    guarana_stock -= 1
                break
                
            else:

                valor_totalpago -= valor_bebida
                troco_user = valor_totalpago
                troco_total = valor_totalpago
                contador_cedulas_moedas = 0
                contador_troco = 0

                print("Troco: ")
                print()
                
                while True:

                    if ((troco_user/20) >= 1) and (quant_cedulas20 > 0):
                        contador_cedulas_moedas = int((troco_user)/20)
                        while (quant_cedulas20 > 0) and (contador_cedulas_moedas >= 1): 
                            contador_cedulas_moedas -= 1
                            quant_cedulas20 -= 1
                            troco_user -= 20
                            contador_troco += 1
                        print(contador_troco, " notas de R$ 20.00!")
                        contador_troco = 0

                    elif ((troco_user/10) >= 1) and (quant_cedulas10 > 0):
                        contador_cedulas_moedas = int((troco_user)/10)
                        while (quant_cedulas10 > 0) and (contador_cedulas_moedas >= 1):
                            contador_cedulas_moedas -= 1
                            quant_cedulas10 -= 1
                            troco_user -= 10
                            contador_troco += 1
                        print(contador_troco, " notas de R$ 10.00!")
                        contador_troco = 0

                    elif ((troco_user/5) >= 1) and (quant_cedulas5 > 0):
                        contador_cedulas_moedas = int((troco_user)/5)
                        while (quant_cedulas5 > 0) and (contador_cedulas_moedas >= 1):
                            contador_cedulas_moedas -= 1
                            quant_cedulas5 -= 1
                            troco_user -= 5
                            contador_troco += 1
                        print(contador_troco, " notas de R$ 5.00!")
                        contador_troco = 0

                    elif ((troco_user/2) >= 1) and (quant_cedulas2 > 0):
                        contador_cedulas_moedas = int((troco_user)/2)
                        while (quant_cedulas2 > 0) and (contador_cedulas_moedas >= 1):
                            contador_cedulas_moedas -= 1
                            quant_cedulas2 -= 1
                            troco_user -= 2
                            contador_troco += 1
                        print(contador_troco, " notas de R$ 2.00!")
                        contador_troco = 0

                    elif (troco_user >= 1) and (quant_moedas1 > 0):
                        contador_cedulas_moedas = int(troco_user)
                        while (quant_moedas1 > 0) and (contador_cedulas_moedas >= 1):
                            contador_cedulas_moedas -= 1
                            quant_moedas1 -= 1
                            troco_user -= 1
                            contador_troco += 1
                        print(contador_troco, " moedas de R$ 1.00!")
                        contador_troco = 0

                    elif (troco_user >= 0.5) and (quant_moedas050 > 0):
                        contador_cedulas_moedas = int((troco_user)/0.5)
                        while (quant_moedas050 > 0) and (contador_cedulas_moedas >= 1):
                            contador_cedulas_moedas -= 1
                            quant_moedas050 -= 1
                            troco_user -= 0.5
                            contador_troco += 1
                        print(contador_troco, " moedas de R$ 0.50!")
                        contador_troco = 0

                    elif (troco_user >= 0.25) and (quant_moedas025 > 0):
                        contador_cedulas_moedas = int((troco_user)/0.25)
                        while (quant_moedas025 > 0) and (contador_cedulas_moedas >= 1):
                            contador_cedulas_moedas -= 1
                            quant_moedas025 -= 1
                            troco_user -= 0.25
                            contador_troco += 1
                        print(contador_troco, " moedas de R$ 0.25!")
                        contador_troco = 0

                    elif (troco_user >= 0.10) and (quant_moedas010 > 0):
                        contador_cedulas_moedas = int((troco_user)/0.10)
                        while (quant_moedas010 > 0) and (contador_cedulas_moedas >= 1):
                            contador_cedulas_moedas -= 1
                            quant_moedas010 -= 1
                            troco_user -= 0.10
                            contador_troco += 1
                        print(contador_troco, " moedas de R$ 0.10!")
                        contador_troco = 0

                    elif (troco_user >= 0.05) and (quant_moedas005 > 0):
                        contador_cedulas_moedas = int((troco_user)/0.05)
                        while (quant_moedas005 > 0) and (contador_cedulas_moedas >= 1):
                            contador_cedulas_moedas -= 1
                            quant_moedas005 -= 1
                            troco_user -= 0.05
                            contador_troco += 1
                        print(contador_troco, " moedas de R$ 0.05!")
                        contador_troco = 0

                    elif (troco_user == 0):
                        print()
                        print("Sua bebida foi dispejada e seu troco é de: R$", troco_total, " por favor os retire de seu recipiente de entrega apropriado e tenha um bom dia.")
                        print()
                        valor_totalpago = 0
                        print("Saldo em maquina atualizado: R$", valor_totalpago)
                        print()
                        if(escolha_produto == "A1"):
                            coca_stock -= 1
                            break
                        elif(escolha_produto == "B2"):
                            fanta_stock -= 1
                            break
                        elif(escolha_produto == "C3"):
                            guarana_stock -= 1
                            break

                    else:
                        print("Compra cancelada!")
                        print("Troco em maquina insuficiente :(")
                        break
                break
            
    elif (escolha_produto == "ADM"):

        while True:
        
            print("Bem-Vindo chefe, como podemos ajuda-lo hoje")
            print("1 - Verificar quantidade de cedulas em maquina:")
            print("2 - Atualizar saldo da maquina:")
            print("3 - Verificar estoque de bebidas:")
            print("4 - Atualizar estoque de bebidas:")
            print("0 - Voltar")
            print()
            escolha_admin = input()
            print()

            if (escolha_admin == '1'):
                print(quant_cedulas20, " cédulas de R$20.00")
                print(quant_cedulas10, " cédulas de R$10.00")
                print(quant_cedulas5, " cédulas de R$5.00")
                print(quant_cedulas2, " cédulas de R$2.00")
                print(quant_moedas1, " moedas de R$1.00")
                print(quant_moedas050, " moedas de R$0.50")
                print(quant_moedas025, " moedas de R$0.25")
                print(quant_moedas010, " moedas de R$0.10")
                print(quant_moedas005, " moedas de R$0.05")
                print()

            elif (escolha_admin == '2'):
                while True:
                    escolha_att = input("Você deseja depositar(1) ou sacar(2): Para cancelar digite 0")
                    if (escolha_att == '1'):
                        while True:
                            print()
                            valor_deposito = input("Digite o valor da cedula ou moeda que você deseja depositar: (Valor mais alto aceita R$20.00 - valor mais baixo aceito R$0.05) (Digite '0' para voltar)")
                            print()
                            
                            if (valor_deposito == '20'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de cedulas de R$20.00 você deseja depositar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    quant_cedulas20 += quant_cedulas_moedas
                                    print("Deposito realizado com sucesso!")
                                    print("Quantidade de cedulas de R$20.00 em maquina atualmente: ", quant_cedulas20)
                                    
                            elif (valor_deposito == '10'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de cedulas de R$10.00 você deseja depositar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    quant_cedulas10 += quant_cedulas_moedas
                                    print("Deposito realizado com sucesso!")
                                    print("Quantidade de cedulas de R$10.00 em maquina atualmente: ", quant_cedulas10)
                                    
                            elif (valor_deposito == '5'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de cedulas de R$5.00 você deseja depositar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    quant_cedulas5 += quant_cedulas_moedas
                                    print("Deposito realizado com sucesso!")
                                    print("Quantidade de cedulas de R$5.00 em maquina atualmente: ", quant_cedulas5)
                                    
                            elif (valor_deposito == '2'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de cedulas de R$2.00 você deseja depositar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    quant_cedulas2 += quant_cedulas_moedas
                                    print("Deposito realizado com sucesso!")
                                    print("Quantidade de cedulas de R$2.00 em maquina atualmente: ", quant_cedulas2)
                                    
                            elif (valor_deposito == '1'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de moedas de R$1.00 você deseja depositar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    quant_moedas1 += quant_cedulas_moedas
                                    print("Deposito realizado com sucesso!")
                                    print("Quantidade de moedas de R$1.00 em maquina atualmente: ", quant_moedas1)
                                    
                            elif (valor_deposito == '0.5'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de moedas de R$0.50 você deseja depositar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    quant_moedas050 += quant_cedulas_moedas
                                    print("Deposito realizado com sucesso!")
                                    print("Quantidade de moedas de R$0.50 em maquina atualmente: ", quant_moedas050)
                                    
                            elif (valor_deposito == '0.25'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de moedas de R$0.25 você deseja depositar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    quant_moedas025 += quant_cedulas_moedas
                                    print("Deposito realizado com sucesso!")
                                    print("Quantidade de moedas de R$0.25 em maquina atualmente: ", quant_moedas025)
                                    
                            elif (valor_deposito == '0.1'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de moedas de R$0.10 você deseja depositar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    quant_moedas010 += quant_cedulas_moedas
                                    print("Deposito realizado com sucesso!")
                                    print("Quantidade de moedas de R$0.10 em maquina atualmente: ", quant_moedas010)
                                    
                            elif (valor_deposito == '0.05'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de moedas de R$0.05 você deseja depositar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    quant_moedas005 += quant_cedulas_moedas
                                    print("Deposito realizado com sucesso!")
                                    print("Quantidade de moedas de R$0.05 em maquina atualmente: ", quant_moedas005)
                                    
                            elif (valor_deposito == '0'):
                                break
                            else:
                                print()
                                print("Cédula/moeda escolhida para deposito inexistente em maquina!")
                                print()

                    elif (escolha_att == '2'):
                        while True:
                            valor_saque = input("Digite o valor da cedula ou moeda que você deseja sacar: (Valor mais alto aceita R$20.00 - valor mais baixo aceito R$0.05) (Digite '0' para voltar)")
                            
                            if (valor_saque == '20'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de cedulas de R$20.00 você deseja sacar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    if(quant_cedulas20 >= quant_cedulas_moedas):
                                        quant_cedulas20 -= quant_cedulas_moedas
                                        print("Saque realizado com sucesso!")
                                        print("Quantidade de cedulas de R$20.00 em maquina atualmente: ", quant_cedulas20)
                                    else:
                                        print("Quantidade de cedulas em maquina, insuficiente para o saque!")
                                    
                            elif (valor_saque == '10'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de cedulas de R$10.00 você deseja sacar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    if(quant_cedulas10 >= quant_cedulas_moedas):
                                        quant_cedulas10 -= quant_cedulas_moedas
                                        print("Saque realizado com sucesso!")
                                        print("Quantidade de cedulas de R$10.00 em maquina atualmente: ", quant_cedulas10)
                                    else:
                                        print("Quantidade de cedulas em maquina, insuficiente para o saque!")
                                    
                            elif (valor_saque == '5'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de cedulas de R$5.00 você deseja sacar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    if(quant_cedulas5 >= quant_cedulas_moedas):
                                        quant_cedulas5 -= quant_cedulas_moedas
                                        print("Saque realizado com sucesso!")
                                        print("Quantidade de cedulas de R$5.00 em maquina atualmente: ", quant_cedulas5)
                                    else:
                                        print("Quantidade de cedulas em maquina, insuficiente para o saque!")
                                    
                            elif (valor_saque == '2'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de cedulas de R$2.00 você deseja sacar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    if(quant_cedulas2 >= quant_cedulas_moedas):
                                        quant_cedulas2 -= quant_cedulas_moedas
                                        print("Saque realizado com sucesso!")
                                        print("Quantidade de cedulas de R$2.00 em maquina atualmente: ", quant_cedulas2)
                                    else:
                                        print("Quantidade de cedulas em maquina, insuficiente para o saque!")
                                    
                            elif (valor_saque == '1'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de moedas de R$1.00 você deseja sacar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    if(quant_moedas1 >= quant_cedulas_moedas):
                                        quant_moedas1 -= quant_cedulas_moedas
                                        print("Saque realizado com sucesso!")
                                        print("Quantidade de moedas de R$1.00 em maquina atualmente: ", quant_moedas1)
                                    else:
                                        print("Quantidade de moedas em maquina, insuficiente para o saque!")
                                    
                            elif (valor_saque == '0.5'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de moedas de R$0.50 você deseja sacar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    if(quant_moedas050 >= quant_cedulas_moedas):
                                        quant_moedas050 -= quant_cedulas_moedas
                                        print("Saque realizado com sucesso!")
                                        print("Quantidade de moedas de R$0.50 em maquina atualmente: ", quant_moedas050)
                                    else:
                                        print("Quantidade de moedas em maquina, insuficiente para o saque!")
                                    
                            elif (valor_saque == '0.25'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de moedas de R$0.25 você deseja sacar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    if(quant_moedas025 >= quant_cedulas_moedas):
                                        quant_moedas025 -= quant_cedulas_moedas
                                        print("Saque realizado com sucesso!")
                                        print("Quantidade de moedas de R$0.25 em maquina atualmente: ", quant_moedas025)
                                    else:
                                        print("Quantidade de moedas em maquina, insuficiente para o saque!")
                                
                            elif (valor_saque == '0.1'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de moedas de R$0.10 você deseja sacar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    if(quant_moedas010 >= quant_cedulas_moedas):
                                        quant_moedas010 -= quant_cedulas_moedas
                                        print("Saque realizado com sucesso!")
                                        print("Quantidade de moedas de R$0.10 em maquina atualmente: ", quant_moedas010)
                                    else:
                                        print("Quantidade de moedas em maquina, insuficiente para o saque!")
                                
                            elif (valor_saque == '0.05'):
                                quant_cedulas_moedas = int(input("Qual a quantidade de moedas de R$0.05 você deseja sacar?"))
                                if (quant_cedulas_moedas < 0):
                                    print()
                                    print("Não é possivel depositar uma quantidade negativa de cédulas/moedas!")
                                    print()
                                else:
                                    if(quant_moedas005 >= quant_cedulas_moedas):
                                        quant_moedas005 -= quant_cedulas_moedas
                                        print("Saque realizado com sucesso!")
                                        print("Quantidade de moedas de R$0.05 em maquina atualmente: ", quant_moedas005)
                                    else:
                                        print("Quantidade de moedas em maquina, insuficiente para o saque!")
                                
                            elif (valor_saque == '0'):
                                break
                            else:
                                print()
                                print("Cédula/moeda escolhida para deposito inexistente em maquina!")
                                print()
                        
                    elif(escolha_att == '0'):
                        print()
                        break

                    else:
                        print("Opção não compreendida! Por favor digite sua opção novamente.")
                        print()

            elif (escolha_admin == '3'):
                print(coca_stock, " latas de coca-cola.")
                print(fanta_stock, " latas de fanta laranja.")
                print(guarana_stock, " latas de guaraná.")
                print()

            elif (escolha_admin == '4'):
                while True:
                    print("Você deseja adicionar(1) ou retirar(2) bebidas do estoque? (Digite '0' para voltar)")
                    escolha_att = input()
                    quant_lata = 0
                    
                    if (escolha_att == '1'):
                        while True:
                            print("Você deseja adicionar bebidas de qual marca? (Digite '0' para voltar)")
                            print("1 - coca-cola")
                            print("2 - fanta laranja")
                            print("3 - guaraná")
                            escolha_bebida = input()
                            
                            if (escolha_bebida == '1'):
                                quant_lata = int(input("Quantas latas de coca-cola você deseja adicionar ao estoque?"))
                                print()
                                if (quant_lata >= 0):
                                    coca_stock += quant_lata
                                    print("Estoque atualizado com sucesso!")
                                    print("Quantidade atualizada de latas de coca-cola em estoque: ", coca_stock)
                                    print()
                                else:
                                    print("Impossivel adicionar um valor negativo de latas ao estoque!")
                                    print()
                                
                            elif (escolha_bebida == '2'):
                                quant_lata = int(input("Quantas latas de fanta laranja você deseja adicionar ao estoque?"))
                                print()
                                if (quant_lata >= 0):
                                    fanta_stock += quant_lata
                                    print("Estoque atualizado com sucesso!")
                                    print("Quantidade atualizada de latas de fanta laranja em estoque: ", fanta_stock)
                                    print()
                                else:
                                    print("Impossivel adicionar um valor negativo de latas ao estoque!")
                                    print()

                            elif (escolha_bebida == '3'):
                                quant_lata = int(input("Quantas latas de guaraná você deseja adicionar ao estoque?"))
                                print()
                                if (quant_lata >= 0):
                                    guarana_stock += quant_lata
                                    print("Estoque atualizado com sucesso!")
                                    print("Quantidade atualizada de latas de guaraná em estoque: ", guarana_stock)
                                    print()
                                else:
                                    print("Impossivel adicionar um valor negativo de latas ao estoque!")
                                    print()

                            elif (escolha_bebida == '0'):
                                print()
                                break
                                
                            else:
                                print()
                                print("Opção não compreendida por favor digite sua opção novamente.")
                                print()

                    elif (escolha_att == '2'):
                        while True:
                            print("Você deseja retirar bebidas de qual marca? (Digite '0' para voltar)")
                            print("1 - coca-cola")
                            print("2 - fanta laranja")
                            print("3 - guaraná")
                            escolha_bebida = input()
                            
                            if (escolha_bebida == '1'):
                                quant_lata = int(input("Quantas latas de coca-cola você deseja retirar ao estoque?"))
                                print()
                                if (coca_stock >= quant_lata) and (quant_lata >= 0):
                                    coca_stock -= quant_lata
                                    print("Estoque atualizado com sucesso!")
                                    print("Quantidade atualizada de latas de coca-cola em estoque: ", coca_stock)
                                    print()
                                elif (quant_lata < 0):
                                    print("Numeros negativos não são aceitos!")
                                    print()
                                else:
                                    print("Quantidade de latas insuficientes em estoque! Retire uma quantidade valida")
                                    print()
                                
                            elif (escolha_bebida == '2'):
                                quant_lata = int(input("Quantas latas de fanta laranja você deseja retirar ao estoque?"))
                                print()
                                if (fanta_stock >= quant_lata) and (quant_lata >= 0):
                                    fanta_stock -= quant_lata
                                    print("Estoque atualizado com sucesso!")
                                    print("Quantidade atualizada de latas de fanta laranja em estoque: ", fanta_stock)
                                    print()
                                elif (quant_lata < 0):
                                    print("Numeros negativos não são aceitos!")
                                    print()
                                else:
                                    print("Quantidade de latas insuficientes em estoque! Retire uma quantidade valida")
                                    print()

                            elif (escolha_bebida == '3'):
                                quant_lata = int(input("Quantas latas de guaraná você deseja retirar ao estoque?"))
                                print()
                                if (guarana_stock >= quant_lata) and (quant_lata >= 0):
                                    guarana_stock -= quant_lata
                                    print("Estoque atualizado com sucesso!")
                                    print("Quantidade atualizada de latas de guaraná em estoque: ", guarana_stock)
                                    print()
                                elif (quant_lata < 0):
                                    print("Numeros negativos não são aceitos!")
                                    print()
                                else:
                                    print("Quantidade de latas insuficientes em estoque! Retire uma quantidade valida")
                                    print()

                            elif (escolha_bebida == '0'):
                                print()
                                break
                                
                            else:
                                print()
                                print("Opção não compreendida por favor digite sua opção novamente.")
                                print()
                                
                    elif (escolha_att == '0'):
                        print()
                        break
                    
                    else:
                        print("Opção não compreendida! Por favor digite sua opção novamente.")
                        print()
                                    
            elif (escolha_admin == '0'):
                break

            else:
                print("Opção não compreendida! Por favor digite sua opção novamente.")
                print()

    elif (escolha_produto == '0'):
        print("Volte sempre!")
        break
        
    else:
        print("Opção não compreendida por favor digite sua opção novamente.")
        print()
