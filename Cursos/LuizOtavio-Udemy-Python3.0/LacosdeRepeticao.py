"""
Código baseado nas orientações do Professor Luiz Miranda. - Udemy.
"""

while True: # laço 4
    print()
    sair = input('Deseja Sair? Ou digite [s]-SIM ou [n]-NÃO: ') # informação #laço 3
    num_1 = input('Digte um número: ') # informação vai para Laço 2 e 1
    num_2 = input('Digite outro número: ')  # informação vai para laço 2 e 1
    operator = input('Digite um dos peradores *,/,-.+: ' ) # informação vai para laço 1

    if sair =='s': #laço 3
        print('Tudo bem, até a mais. :-(')
        break # Para o Programa

    elif sair=='n' : #laço 3
        print('Vamos Calcular! :-)')

        if num_1.isnumeric() and num_2.isnumeric(): #valida se o campo preenchido é número #laço 2
            num_1 = (int(num_1)) # faz o cast
            num_2 = (int(num_2)) # faz o cast
            if operator == '+': #laços de repetição # laço 1
                print(num_1 + num_2)
            elif operator == "-":
                print(num_1 - num_2)
            elif operator == "*":
                print(num_1 * num_2)
            elif operator == "/":
                print(num_1 / num_2)
            else: # fim laço 1
                print('Digite um operador dentre as opções')
        else: # fim laço 2 
            print(f"Os dois campos precisam ser números, e não {num_1} e {num_2}")
            print("Tente novamente.")
    else: # fim laço 3
        print('Por favor, Ou digite a letra  [s] para SIM, Ou [n] para Não.')
        continue # direciona para o Inicio do Programa.