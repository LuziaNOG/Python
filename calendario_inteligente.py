import datetime

def diaSemana(data):
    # recebe a data e diz qual vai ser o dia da semana
    try:
        semana = {'0': 'Segunda-feira', '1': 'Terca-feira', '2': 'Quarta-feira', '3': 'Quinta-feira', '4': 'Sexta-feira',
                '5': 'Sabado', '6': 'Domingo'}            
        data = datetime.datetime(int(data[2]), int(data[1]), int(data[0]))
        indice_da_semana = str(data.weekday())
        return (f'A data informada é um(a){semana[indice_da_semana]}')
    except:
        return ('Erro,verifique os dados informados e tente novamente')

def aniversarioFuturo(dataNasc, idade):
    # recebe a data de nascimento e a idade e retorna que dia da semana vai ser o aniversario da idade informada
    try:
        dataNasc = datetime.datetime(int(dataNasc[2]), int(dataNasc[1]), int(dataNasc[0]))
        dataFutura = [int(dataNasc.day),int(dataNasc.month), int (dataNasc.year + int(idade))]
        return diaSemana(dataFutura)
    except:
        return ('Erro,verifique os dados informados e tente novamente')


def contandoDias(dataFutura):
    #contas os dias que faltam do dia atual ate o dia do evento
    try:
        dataAtual= datetime.datetime.now()
        dataFutura = datetime.datetime(int(dataFutura[2]), int(dataFutura[1]), int(dataFutura[0]))
        qtd =  dataFutura-dataAtual
        return qtd.days
    except:
        return ('Erro,verifique os dados informados e tente novamente')

########################################################################################################################
############################################# Menu para teste ##########################################################
print('Bem-vindo ao calendario basica em python !!!')
op = ''
while (op != '4'):
    # Recebendo dados do usuario e salvando a resposta
    op = input('Escolha a opção desejada: 1- Que dia da semana é?!? , 2 - Em dia dia vai ser meu aniversario de X Anos ?!?!, 3- Faltam quantos para ...?!?!, 4-sair\n')
        
    if op == '1':
        data = []
        
        data.append(input('Digite a data:\ndia:'))        
        data.append(input('mes:'))        
        data.append(input('ano(ex:1994):'))
        
        # Chamando a função e salvando o resultado
        resp = diaSemana(data)
        # Imprimindo o resultado da função
        print(f'Resposta: {resp}')

    elif op == '2':
        data = []
        data.append(input('Digite a data de nascimento:\ndia:'))
        data.append(input('mes:'))
        data.append(input('ano (ex:1994):'))
        idade = input('Digite a idade:')
        resp = aniversarioFuturo(data,idade)
        print(f'Resposta: {resp}')


    elif op == '3':
        data = []
        data.append(input('Digite a data:\ndia:'))
        data.append(input('mes:'))
        data.append(input('ano (ex:1994):'))
        resp = contandoDias(data)
        print(f'Resposta: {resp}')

    elif op == '4':
        print('Bye Bye')

    else:
         print('Opção incorreta,tente novamente!')