# Importando o modulo math do python, para usar a função sqrt()
import math

# Essa função verifica se o numero passado a ela é um quadrado perfeito
def is_square(number):
    x = int(math.sqrt(number))
    return x * x == number

# Essa função verifica se o numero passado está em Fibonacci, usando a formula 5*N2 + 4 ou 5*N2 - 4
def number_in_fibonacci(number):
    positive = 5 * number * number + 4
    negative = 5 * number * number - 4
    # Aqui é passado o resultado das formulas acima para verificar se é um quadrado perfeito
    if is_square(positive) or is_square(negative):
        print(f"O numero {number} está na sequência de Fibonacci.")
    else:
        print(f"O numero {number} não está na sequência de Fibonacci.")

number = int(input("Digite um número inteiro: "))
number_in_fibonacci(number)
