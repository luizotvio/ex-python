def calculadora (numero1, numero2, operador):

    if operador == '+':
        return numero1 + numero2
    elif operador == '-':
        return numero1 - numero2
    elif operador == '*':
        return numero1 * numero2
    elif operador == '/':
        return numero1 / numero2
    elif operador != '+' '-' '*' '/':
        return 0

    
numero1 = 10
numero2 = 5
operador = '+'

resultado = calculadora(numero1, numero2, operador)
print(resultado)