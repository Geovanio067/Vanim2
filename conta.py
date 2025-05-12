from Conta import ContaBancaria

numero = input('informe o numero da conta: ')
titular = input('informe o nome do titular da conta: ')
limite = float('informe o limite da conta: ')
conta1 = ContaBancaria(numero, titular, limite)

conta1.saque()

while True:
    print("\n--- MENU ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        conta1.depositar()
    elif opcao == "2":
        conta1.sacar()
    elif opcao == "3":
        conta1.ver_saldo()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
