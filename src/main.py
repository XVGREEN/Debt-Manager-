from divida import *
import os
cebola= Sujeito("Cebola",8756563)
agostinho= Sujeito("Agostinho",8755526)
emanuel=Sujeito("87255223",83000000)

dividas = [Divida(cebola,"20/08/2025",15),  
          Divida(agostinho,"20/08/2025",20000),
          Divida(emanuel,"20/08/2025",0.01)]


def listar():
    print("Listando todas dividas:")
    for i in dividas:
        print(i)
    input("pressione qualquer tecla pra prosseguir...")


def pesquisar():
    nome = input("Escreva o nome da pessoa que deve: ")        
    encontrou = False
    for divida in dividas:
        if divida.sujeito.nome == nome:
            print(divida)
            encontrou = True
        if not encontrou:
           print("Nenhuma dívida encontrada para esse nome.")
    
def cadastrar():
    nome = input("Escreva o nome da pessoa:")
    numero = input("Escreva o numero:")
    prazo = input("Escreva o prazo:")
    valor = int(input("Escreva o valor:"))
    s=Sujeito(nome,numero)
    d =Divida(s,prazo,valor)
    dividas.append(d)

      
def show_menu():
    print (".............MeuTaku..........\n")
    print("1.Listar dividas\n")
    print("2.Pesquisar \n")
    print("3.Cadastrar  Divida\n")
    print("4.Eliminar Divida\n")
    print("5.Sair\n")
    resposta = int(input("Escolha uma opcao:"))
    print("\033c", end="")
    if resposta==1:
        listar()
        print("\033c", end="")
        show_menu()           
    if resposta==2:
        pesquisas()
        input("Pressione qualquer tecla para prosseguir...")
        print("\033c", end="")
        show_menu()

    if resposta == 3:
        cadastrar()
        print("\033c", end="")
        show_menu()
    if resposta == 4:
         nome = input("Escreva o nome da pessoa:")
         encontrou = False
         for divida in dividas:
            if divida.sujeito.nome == nome:
               dividas.remove(divida)
               encontrou = True
         if not encontrou:
             print("Nenhuma dívida encontrada para esse nome.")
         input("Pressione qualquer tecla para prosseguir...")
         print("\033c", end="")
         show_menu()
        


show_menu();
