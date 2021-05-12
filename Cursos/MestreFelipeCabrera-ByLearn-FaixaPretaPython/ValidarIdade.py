"""
Exercício de Validar Idade / Definindo uma função
Python por ByLearn, Professor Felipe Cabrera.]
Feito por Rafael Tasinato
"""
#@bylearn  Professor Felipe Cabrera
"""
PythonFaixaPreta
"""

def validar_idade(idade): # cria função validar_idade

    if int(idade) < 18:
        print('\nDesculpe, você não tem idade para prosseguir.', nome, idade,'anos')
        return False
    else:
        print('Digite uma das opções abaixo:')
        return True

def escolher_cartacredito(): #cria a função Carta de Crédito
    print("Digite uma das opções abaixo:")
    print("1-Carro\n 2-Moto\n 3-Carro e Moto")

    return(int(input()))


def escolher_preco(escolha):  #cria função escolher_preço
    valor_carro = 1500
    valor_moto = 1000

    if int(escolha) == 1:
        return valor_carro
    elif int(escolha) == 2:
        return valor_moto
    else:
        return valor_carro + valor_moto

def desconto(valor): #cria função desconto
    int(valor)
    return valor -(valor*0.10)

#entrada de dados pelo usuário
nome  = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")

# Processamento das informações
if validar_idade(idade):
    escolha = escolher_cartacredito()

    print("\nPerfeito! Vamos calcular o valor")
    valor = escolher_preco(escolha)

    print(f'\n {nome} o valor total é de {valor} reais')
    print("Vamos verificar com o gerente se você ganha um desconto.")
    valor = desconto(valor)

    print(f"\n Com desconto e consigo fazer por {valor} em reais")

    interesse = int(input(f"Este valor te interessa?\n 1-Sim 2-Não: "))
    if interesse != 1: # se não interessar ou se o usuário digitar algo diferente de 1 entra neste código.
            print("\nTudo bem: (\n Me avise se mudar de ideia.")
    else:
          print("\nPerfeito! Começaremos amanhã!")