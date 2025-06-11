

menu = """

-------- BEM-VINDO ---------
  
   [1] - DEPOSITAR
   [2] - SACAR
   [3] - EXTRATO
   [4] - SAIR

----------------------------
DIGITE A OPÇÃO DESEJADA:

"""

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = (float(input("Informe o valor a ser depositado:")))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("--------------------------------------------")
            print(f"Depósito realizado no valor de R${deposito}")
            print("--------------------------------------------")
        else:
            print("Valor inválido para depósito.")


    elif opcao == 2:
        saque = float(input("Informe o valor desejado:"))
        if saque > saldo:
            print(f"Saldo insuficiente \nSeu saldo é de R$ {saldo}")
        elif saque > limite:
            print(f"O valor excede o limte de saque de R${limite}")
        elif numero_saques >= limite_saques:
            print(f"Limite de saque diário excedido. Volte amanhã!")
        elif saque <= 0:
            print("Valor inválido para saque")
        else:
            print("--------------------------------------")
            print(f"Saque realizado no valor de R${saque}")
            print("--------------------------------------")
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1


    elif opcao == 3:
        print("-------- EXTRATO ---------")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("--------------------------")


    elif opcao == 4:
        print("-----------------------------------------------------------")
        print("Finalizando operação. Muito obrigado por ser nosso cliente!")
        print("-----------------------------------------------------------")


    else:
        print("--------------------------------")
        print("Opção inválida. Tente novamente.")
        print("--------------------------------")











