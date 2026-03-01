'''
HAVYNER JALLES SIQUEIRA
RU 5079616

Atividade 3 Engenharia de Software

Desenvolver um sistema simples de controle de estoque em Python, 
com funcionalidade de entrada e saída de produtos, Conforme a História de Usuário fornecida.
'''

estoque = {}

#Criando o menu para o funcionário
def menu():
    while True:
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
            elif op == 5:
                ver_movimentacoes()
            elif op == "0":
                print("Obrigado!!")
                break
            else:
                print("Opção inválida!")
        
        except ValueError:
            print("Valor inválido, tente novamente!")