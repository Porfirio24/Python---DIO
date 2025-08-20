saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
    print("""
          ==== Bem Vindo ao Pybank ====
          [1] Entrar
          [0] Sair
          =============================
          """)
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        while True:
            print("""
            ====== MENU ======

            [2] Deposito 
            [3] Saque
            [4] Extrato
            [5] Sair

            ================
            """)
            opcao = input("Escolha uma Opção: ")

            if opcao == "2":
                valor = float(input("Qual o valor deseja depositar: "))
                if valor > 0:
                    saldo += valor
                    extrato += f"Depósito R$: {valor:.2f}\n"
                    print("Depósito Realizado com Sucesso!")
                else:
                    print("Erro ao Depositar")

            elif opcao == "3":
                valor = float(input("Digite o valor do Saque: "))

                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saque = numero_saque >= limite_saque

                if excedeu_saldo:
                    print("Saldo Insuficiente!")
                elif excedeu_limite:
                    print(f"O limite de saque é de R${limite:.2f}")
                elif excedeu_saque:
                    print("Número máximo de saques já realizado!")
                elif valor > 0:
                    saldo -= valor
                    extrato += f"Saque R$: {valor:.2f}\n"
                    numero_saque += 1
                    print("Saque Realizado com Sucesso!")
                else:
                    print("Valor de Saque Inválido!")

            elif opcao == "4":
                print("==== Extrato ====")
                print("Não houve movimentação na sua Conta!" if not extrato else extrato)
                print(f"Saldo: R${saldo:.2f}\n")
                print("=================")

            elif opcao == "5":
                print("Obrigado por sua Preferência!")
                break

            else:
                print("Escolha uma opção Válida!")

    elif opcao == "0":
        print("Saindo do PyBank... Obrigado por usar nossos serviços!")
        break

    else:
        print("Escolha uma opção válida!")