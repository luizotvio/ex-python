def calculadora():

    while True:
        print("\nMenu de Operações")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número para a operação correspondente: ")

        if opcao == "0":
            print("Saindo da calculadora.")
            break
        elif opcao in ['1', '2', '3', '4']:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                resultado = numero1 + numero2
                print("Resultado da soma:", resultado)
            elif opcao == '2':
                resultado = numero1 - numero2
                print("Resultado da subtração:", resultado)
            elif opcao == '3':
                resultado = numero1 * numero2
                print("Resultado da multiplicação:", resultado)
            elif opcao == '4':
                if numero2 != 0:
                    resultado = numero1 / numero2
                    print("Resultado da divisão:", resultado)
                else:
                    print("Não é possível dividir por zero.")
        else:
            print("Opção inválida. Por favor, tente novamente.")

calculadora()