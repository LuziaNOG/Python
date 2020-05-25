import math

def cone_volume(h, r):
  if (h>0 and r>0):
    return round((math.pi*(r**2)*h)/3, 2)
  else:
    return 0

####################################### MENU TESTE ###############################################
print("Bem-vindos a função que calcula o volume de um cone")
op = ''
while(op != '0'):
  op = input('Digite a opção desejada: 1- Volume do cone, 0- sair ')

  if (op == '1'):
    try:
      h = float(input ('Digite a altura do cone:'))
      r = float(input ('Digite o raio do cone:'))
      resp = cone_volume(h,r)
      print (f'O volume é {resp}')
    except:
      flat = input("Digite apenas numeros\n 1-Tentar novamente, 0- Sair")
  elif (op == '0'):
    print ('Bye-Bye')
  else:
    print('Digite uma opção valida')