#Função que recebe uma palavra, reverte e substitui as vogais por numeros
def encrypt(word):
	word = "".join(reversed(word))
	word = (word.translate({ord('a'): ord('0'), ord('e'): ord('1'), ord('o'): ord('2'), ord('u'): ord('3')}))
	word = word
	return word

#Recebe um texto e separa vogais e consoantes
def split(txt):
  lst = [x for x in txt if x in 'aeiou'] + ['-'] + [x for x in txt if x not in 'aeiou ']
  return "".join(lst)


#################################### Menu Teste #########################################

op=''
while( op != '3'):
  op=input("Digite a opção desejaada: 1- Cifrar , 2- Separar vogais e consoantes, 3- sair:\n")
    
  if op == '1':
    #teste função 1
    entrada = input("Digite a palavra que deseja cifrar:\n")
    saida = encrypt(entrada)
    print(f'A palavra digitada é {entrada}, cifrada é {saida}')

  elif op == '2':
    #teste função 2
    txt = input("Digite o texto o qual desejaa separar as vogais e consoantes:\n")
    txtSeparado=split(txt)
    print(f'O texto digitado é: {txt}\n texto com vagoas e consoante separados é: {txtSeparado}')

  elif op == '3':
    print("bye-bye")

  else:
    print("Opção invalida, tente novamente")
