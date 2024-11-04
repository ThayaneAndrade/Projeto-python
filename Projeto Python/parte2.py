
import datetime
cpf=""
senha=""
saldoReal=0.0
saldoBit=0.0
saldoEt=0.0
saldoRi=0.0
lista1=[]
lista2=[]
lista3=[]
lista4=[]




#FUNÇÃO 'LOGIN' CONTÉM TODAS AS INFORMAÇÕES PARA VERIFICAÇÃO DO CPF DO USUÁRIO
def login ():
    # INSERIDO LAÇO DE REPETIÇÃO QUE: VERFIFICA SE O CPF ESTÁ CERTO (CONTÉM APENAS NÚMEROS)
    while True:
        print("★ LOGIN")
        #AVISA QUE A VARIÁVEL UTILIZADA É GLOBAL 
        global cpf 
        cpf= input("Insira o cpf:")
        if cpf.isdigit() and len(cpf)==11:
            ("CPF cadastrado com sucesso!")
            break
        else:
            print("CPF inválido")
            
    
#FUNÇÃO 'SENHA1' CONTÉM TODAS AS INFORMAÇÕES PARA VERIFICAÇÃO DO CPF DO USUÁRIO 
def senha1 ():
    global senha 
    #LAÇO DE REPETIÇÃO QUE: VERIFICA SE A SENHA ESTÁ CERTA(CONTÉM APENAS 6 DIGITOS)
    while True:
        senha = input("Insira a senha:")
        if len(senha) == 6:
            ("Senha cadastrada com sucesso!")
            break
        else:
            print("Senha Inválida")

def saldo ():
    senha1()
    print("☆ Saldo")
    print(f"Reais: R$ {saldoReal:.2f}")
    print(f"Bitcoin: BTC {saldoBit:.4f}")
    print(f"Ethereum: ETH {saldoEt:.4f}")
    print( f"Ripple: XRP {saldoRi:.4f}")
    voltar=input("Deseja voltar ao MENU (1- sim 2-não)?")
    if voltar == 1:
        consultar()
    elif voltar==2: 
        saldo() 

def extrato():
    senha1()
    print("☆ Extrato")
    print("Real:", lista1)
    print("BTC:", lista2)
    print("ETH:", lista3)
    print("XRP:", lista4)




def deposito():
    global saldoReal, saldoBit, saldoEt, saldoRi
    senha1()
    print("☆ Depositar")
    print("1- Reais:")
    print("2- Bitcoin:")
    print("3- Ethereum")
    print("4- Ripple")
    op =int(input("Onde deseja depositar (1-4)?"))
    if op == 1 :
        print("1- Reais")
        valor= float(input("Quanto deseja depositar?"))
        saldoReal = valor 
        print(f"Valor de {valor:.2f} depositados em Reais")
        transacao = (datetime.datetime.now(), valor)
        lista1.append(transacao)
        
    elif op == 2 :
        print("2- Bitcoin")
        valor= float(input("Quanto deseja depositar?"))
        saldoBit = valor 
        print(f"Valor de {valor:.4f} depositados em Bitcoin")
        transacao = (datetime.datetime.now(), valor)
        lista2.append(transacao)
        
    elif op == 3:
        print("3- Ethereum")
        valor= float(input("Quanto deseja depositar?"))
        saldoEt = valor
        print(f"Valor de {valor:.4f} depositados em Ethereum")
        transacao = (datetime.datetime.now(), valor)
        lista3.append(transacao) 
        
    elif op == 4:
        print("4- Ripple")
        valor= float(input("Quanto deseja depositar?"))
        saldoRi = valor 
        print(f"Valor de {valor:.4f} depositados em Ripple")
        transacao = (datetime.datetime.now(), valor)
        lista4.append(transacao)
        

def sacar():
    global saldoReal, saldoBit, saldoEt, saldoRi
    senha1()
    print("☆ Saque")
    print("1- Reais:")
    print("2- Bitcoin:")
    print("3- Ethereum")
    print("4- Ripple")
    op =int(input("Onde deseja sacar (1-4)?"))
    if op == 1 :
        print("1- Reais")
        valor= float(input("Quanto deseja sacar?"))
        if valor <= saldoReal:
            saldoReal = saldoReal - valor 
            print(f"Valor de {valor:.2f} sacado em Reais")
            lista1.append(saldoReal)
        else: 
            print("Saldo insuficiente!")
            
    elif op == 2 :
        print("2- Bitcoin")
        valor= float(input("Quanto deseja depositar?"))
        if valor<= saldoBit:
            saldoBit = saldoBit - valor
            print(f"Valor de {valor:.4f} sacado em Bitcoin")
            lista2.append(saldoBit)
        else:
            print("Saldo insuficiente!")
            
    elif op == 3:
        print("3- Ethereum")
        valor= float(input("Quanto deseja depositar?"))
        if  valor <= saldoEt:
            saldoEt = saldoEt - valor 
            print(f"Valor de {valor:.4f} sacado em Ethereum") 
            lista3.append(saldoEt)
        else:
            print("Saldo insuficiente!")
            
    elif op == 4:
        print("4- Ripple")
        valor= float(input("Quanto deseja depositar?"))
        if  valor<=saldoRi:
            saldoRi = saldoRi - valor 
            print(f"Valor de {valor:.4f} sacado em Ripple")
            lista4.append(saldoRi)
        else: 
             print("Saldo insuficiente!")


def compra():
    print("☆ Compra")


def venda():
    print("☆ Venda")


def atualizar():
    print("☆ Atualizar cotação")


def consultar ():

    while True:
        print("★ MENU")
        print("1- Saldo")
        print("2- Extrato")
        print("3- Deposito")
        print("4- Sacar")
        print("5- Compra")
        print("6- Venda")
        print ("7- Atualizar")
        escolha= input("O que deseja consultar(1-7)?")
        if escolha == '1':
            saldo()
        elif escolha == '2':
            extrato()
        elif escolha == '3':
            deposito()
        elif escolha == '4':
            sacar()
        elif escolha == '5':
            compra()
        elif escolha == '6':
            venda()
        elif escolha == '7':
            atualizar()
        else:
            print("Opção inválida. Tente novamente.")

login()
senha1()
consultar()


    


        
