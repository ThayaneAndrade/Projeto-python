
cpf=("1234")
usuario=("Thayane")

while True:
     print("★ LOGIN")
     usuario1 = input("★ Usuário:")
     senha1 = input("★ Senha:")
     if usuario == usuario1 and senha1==cpf:
         print("Login efetuado!")
         break
     elif usuario != usuario1 and senha1!=cpf:
         print("Senha e Usuário incorretos!")
     elif usuario != usuario1 and cpf == senha1:
         print("Senha correta usuário incorreto!")
     elif usuario == usuario1 and cpf != senha1:
         print("Usuário correto senha incorreta!")
    
     
     
    
    
def saldo ():
    print("☆ Saldo")

def extrato():
    print("☆ Extrato")

def deposito():
    print("☆ Depositar")

def sacar():
    print("☆ Saque")

def compra():
    print("☆ Compra")

def venda():
    print("☆ Venda")

def atualizar():
    print("☆ Atualizar cotação")

print("★ Menu")
saldo()
extrato()
deposito()
sacar()
compra()
venda()
atualizar()
   
    


       
        


