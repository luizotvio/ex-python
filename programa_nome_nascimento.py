import datetime

while True:
    nome = input("Digite seu nome completo: ")
    
    while True:
        try:
            ano_nascimento = int(input("Por favor, digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                break
            else:
                print("Ano fora do intervalo válido. Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    idade = datetime.datetime.now().year - ano_nascimento
    ano_atual = datetime.datetime.now().strftime("%Y")
    print(f"Olá, {nome}! Você completou ou completará {idade} anos em {ano_atual}.")
    
    continuar = input("Deseja verificar a idade de outra pessoa? (S/N): ").upper()
    if continuar != "S":
        break