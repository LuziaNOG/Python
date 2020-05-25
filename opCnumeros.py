import math

#Retorna se o numero é simestrico, 212 = 212
def is_symmetrical(num):
	try:
		return list(str(num)) == list(reversed(str(num)))
	except:
		print ("Digite somente numeros positivos inteiros , tente novamente!")

#retorma lista contendo somente inteiros
def filter_list(l):
	try:
		return list(filter(lambda x: type(x) == int, l ))
	except:
		print("Erro!")

#retorna p fatorial de um numero positivo
def factorial(Z):
	try:
		Z = int(Z)
		return math.factorial(Z)
	except:
		print ("Digite somente numeros positivos inteiros , tente novamente!")

#retorna a soma de todos os numeros ate o numero (X), ex 3 = 3+2+1 = 6
def sum_numbers(n):
	try:
		n = int(n)
		if n <= 1:
			return n
		return n + sum_numbers(n - 1)
	except:
		print ("Digite somente numeros positivos inteiros , tente novamente!")

# retorna o primeiro numero da frase
def left_digit(num):
	try:
		lst = [n for n in num if n.isnumeric()]
		return (int(lst[0]))
	except:
		print ("Digite somente numeros positivos inteiros , tente novamente!")

########################################## MENU TESTE ############################################
print('Bem-vindo!!!')
op = ''
while (op != '5'):
    # Recebendo dados do usuario e salvando a resposta
	op = input('Escolha a opção desejada: 1- Numero simestrico , 2- Fatorial, 3- Somatoria ate o numero X, 4-Primeiro numero da frase, 5-sair\n')
	if op == '1':
		num = input('Digite o numero para verificar se é simestrico\n')
		resp = is_symmetrical(num)
		print(f'{resp}')
    
	elif op == '2':
		num = input('Digite o numero para saber seu fatorial\n')
		resp = factorial(num)
		print(f'{resp}')

	elif op == '3':
		num = input('Digite o numero para saber a somatoris dos seus anteriores ate ele\n')
		resp = sum_numbers(num)
		print(f'{resp}')

	elif op == '4':
		num = input('Digite uma frase para saber a primeira ocorrencia de numeral na mesma\n')
		resp = left_digit(num)
		print(f'{resp}')

	elif op == '5':
		print('Bye Bye')

	else:
		print('Opção incorreta,tente novamente!')