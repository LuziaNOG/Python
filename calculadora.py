# Funções basicas de uma calculadora
def soma(num1, num2):
    try:
        return int(num1) + int(num2)
    except (ValueError) as err:
        return f'A operação não pode ser realizada: {err}'


def sub(num1, num2):
    try:
        return int(num1) + int(num2)
    except (ValueError) as err:
        return f'A operação não pode ser realizada: {err}'


def mult(num1, num2):
    try:
        return int(num1) * int(num2)
    except (ValueError) as err:
        return f'A operação não pode ser realizada: {err}'


def div(num1, num2):
    try:
        return int(num1) / int(num2)
    except (ValueError, ZeroDivisionError) as err:
        return f'A operação não pode ser realizada: {err}'


######################################### Menu basico para Teste ########################################################
print('Bem-vindo a calculadora basica em python !!!')
op = ''
while (op != '5'):
    # Recebendo dados do usuario e salvando a resposta
    op = input('Escolha a operação matematica que deseja realizar: 1- soma , 2 - subtração, 3- multiplicação, 4- divisão, 5-sair\n')

    if op == '1':
        num1 = input('digite o primeiro numero:')
        num2 = input('digite o segundo numero:')
        # Chamando a função e salvando o resultado
        result_soma = soma(num1, num2)
        # Imprimindo o resultado da função
        print(f'Resposta: {result_soma}')

    elif op == '2':
        num1 = input('digite o primeiro numero:')
        num2 = input('digite o segundo numero:')
        result_sub = sub(num1, num2)
        print(f'Resposta: {result_sub}')


    elif op == '3':
        num1 = input('digite o primeiro numero:')
        num2 = input('digite o segundo numero:')
        result_mult = mult(num1, num2)
        print(f'Resposta: {result_mult}')


    elif op == '4':
        num1 = input('digite o primeiro numero:')
        num2 = input('digite o segundo numero:')
        result_div = div(num1, num2)
        print(f'Resposta: {result_div}')

    elif op == '5':
        print('Bye Bye')

    else:
         print('Opção incorreta,tente novamente!')