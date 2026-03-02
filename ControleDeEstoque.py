'''
HAVYNER JALLES SIQUEIRA
RU 5079616

Atividade 3 Engenharia de Software

Desenvolver um sistema simples de controle de estoque em Python, 
com funcionalidade de entrada e saída de produtos, Conforme a História de Usuário fornecida.
'''

#Biblioteca para registrar a data de entrada
from datetime import datetime

#Estoque vai começar vazio e será inclementado
estoque = {}
#Lista para registrar a movimentações
movimentacaoList = []


def cadastrar_produto():
    nome_produto = input("Digite o nome do produto: ").lower() #Usando a função lower para deixar tudo minusculo

    #Verificando se o produto já esta cadastrado
    if nome_produto in estoque:
        print("Produto já cadastrado!\n")
    else:
        #cadastrando produto novo no estoque
        estoque[nome_produto] = 0
        print("Produto cadastrado com sucesso!\n")

def entrada_produto():
    nome_produto = input("\nInforme o nome do produto: ").lower()

    #verificando se possui o produto em estoque
    if nome_produto not in estoque:
        print("Produto não encontrado!\n")
        return
    
    try:
        qnt = int(input("Informe a quantidade de entrada do produto: "))
        #Verificar se a quantidade é válida
        if qnt <= 0:
            print("Quantidade deve ser maior que zero\n")
            return
    except ValueError:
        print("\nDigite um número válido!")
        return
    #Registrando a entrada do produto
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    funcionario = input("Digite o nome do Funcionário responsável: ").lower()

    #Atualizando estoque
    estoque[nome_produto] += qnt

    movimentacaoList.append({
        "Tipo" : "Entrada",
        "Produto" : nome_produto,
        "Quantidade" : qnt,
        "Data" : data,
        "Responsável" : funcionario   
    })

    print("Registro realizado com sucesso!\n")

def saida_produto():
    nome_produto = input("\nInforme o nome do produto: ").lower()
    #Verificando se possui o produto em estoque
    if nome_produto not in estoque:
        print("Produto não encontrado!\n")
        return
    #Verificando se a quantidade informada é mior q zero
    try:
        qnt = int(input("Informe a quantidade que deseja retirar: "))
        if qnt <= 0:
            print("Quantidade deve ser maior que zero!\n")
            return
    except ValueError:
        print("Digite um número válido!\n")
        return
    #Verificanado se a quantidade esta disponível em estoque
    if qnt > estoque[nome_produto]:
        print("Estoque insuficiente!\n")
        return
    
    #Registrando saida
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    funcionario = input("Digite o nome do Funcionário responsável: ").lower()

    estoque[nome_produto] -= qnt

    movimentacaoList.append({
        "Tipo" : "Saída",
        "Produto" : nome_produto,
        "Quantidade" : qnt,
        "Data" : data,
        "Responsável" : funcionario   
    })

    print("Registro realizado com sucesso!\n")


def ver_estoque():
    print("-"*33)
    print("-"*12, "ESTOQUE", "-"*12)

    #Verificar se estoque ta vazio
    if not estoque:
        print("Estoque vazio!\n")
    else:
        for Produto, Quantidade in estoque.items():
            print(f"{Produto} : {Quantidade}")
    print("-"*33)


def ver_movimentacoes():
    print("-"*33)
    print("-"*9, "MOVIMENTAÇÕES", "-"*9)

    #Verificando se tem movimentações
    if not movimentacaoList:
        print("Nenhuma movimentação registrada!\n")
    else:
        for mov in movimentacaoList:
            print(f"{mov['Tipo']} | {mov['Produto']} | {mov['Quantidade']} | {mov['Data']} | {mov['Responsável']}")

    print("-"*33)
    
#Criando o menu para o funcionário (Main)
while True:
    print("\nHavyner Jalles Siqueira RU: 5079616")
    print("BEN-VINDO AO CONTROLE DE ESTOQUE")
    print("1 - CADASTRAR PRODUTO")
    print("2 - ENTRADA DE PRODUTO")
    print("3 - SAÍDA DE PRODUTO")
    print("4 - VER ESTOQUE")
    print("5 - VER MOVIMENTAÇÕES")
    print("0 - SAIR")
    # Verificando se a opção informada é válida
    try:
        op = input("Informe a opção desejada: ")
        if op == "1":
            cadastrar_produto()
        elif op == "2":
            entrada_produto()
        elif op == "3":
            saida_produto()
        elif op == "4":
            ver_estoque()
        elif op == "5":
            ver_movimentacoes()
        elif op == "0":
            print("Obrigado!!")
            break
        else:
            print("Opção inválida!\n")
     
    except ValueError:
        print("Valor inválido, tente novamente!\n")