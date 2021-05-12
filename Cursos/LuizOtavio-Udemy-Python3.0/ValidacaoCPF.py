"""
Desafio: Validando CPF
Professor Luiz Otavio / Luiz Miranda
Python - Curso Udemy - Início: 11/05/2021 - 19:47 Termino: 12/05/2021 01:31
Aluno: Rafael Tasinato.

Usando somente coneceitos vistos do Python Básico.

cpf: 168.995.350-09
----------------------------------------------------------
1 * 10 = 10                       #      1  * 11 = 11  <-- Início em 11.
6 * 9  = 54                       #      6  * 10 = 60
8 * 8  = 64                       #      8  *  9 = 72
9 * 7  = 63                       #      9  *  8 = 72
9 * 6  = 54                       #      9  *  7 = 63
5 * 5  = 25                       #      5  *  6 = 30
3 * 4  = 12                       #      3  *  5 = 15
5 * 3  = 15                       #      5  *  4 = 20
0 * 2  =  0                       #      0  *  3 =  0
                                  # -->  0  *  2 =  0 <<< adiciona o primeiro digito obtido no calculo
           297                    #                 343
11 - (297%11) = 11                #   11-(343%11) = 9
11 >= 9 = 0                        #
Digito 1 = 0                      #  Digito 2 = 9

1 tira a pontuação
2 multiplica pela contagem regressiva e salva em algum local os 9 primeiros digitos.
3 soma-se todo o resultado dos 9 primeiros números do CPF.
4 11 -(resultado modulo por 11) 11
print( 11 - ( 'somadasmultiplicações' %11))

Orientação do professor:
# código de validação após o calçulo

#if novo_cpf == cpf:
#    print(f'{cpf}valido')
#else:
#    print(f'{cpf}Invalido')


"""

#Resolução do Exercício;

cpf = input('Digite o CPF sem pontos ou digito para que seja verificado : ')


# Validação da str digitada se é número e certifica que consta os 11 digitos do cpf usando função len.
if cpf.isnumeric() and len(cpf) == 11:
    #declara variável lista.
    lista_cpf = []
    #separa cada número do cpf criando uma lista com base no na str CPF.
    for n_cpf in cpf:
        # append adiciona cada elemento dentro da lista, int(n_cpf) transforma a str em INT.
        lista_cpf.append(int(n_cpf))
    # print(f'controle da Validação {len(lista_cpf)}') #verificação de controle
    # print(f'{cpf} variavel cpf digitada em str') #verificação de controle
    # print(f'{lista_cpf} lista criada com o cpf digitado e alterado para int') #verificação de controle]

    ### Criando um laço para o caculo do CPF.
        # multiplicar os nove primeiros elementos da lista_cpf por 10 e regredindo o multiplicador de 1 em 1
        # multiplicar os 10 primeiros números da lista_cpf iniciando em 2 aumentando o multiplicardor de 1 em 1 até 11.

    # 1 Calculo da validação CPF
    L_calc_1 = lista_cpf[:-2] # retira os dois últimos digitos do cpf.
     # print(f'{L_calc_1} criado a lista para o primeiro calculo do CPF') #verificação do calculo
    # laço for para calculo de cada int
    cont_1 = 11
    mult_calc1 = []
    for n_mult in L_calc_1:
        cont_1 -= 1
        # print(cont_1) variavel de controle para visualização da informação.
        Valor_calc1 = n_mult*cont_1 # calulo da multiplicação inicia em 10.
        mult_calc1.append(int(Valor_calc1))

    # print(f'{mult_calc1} lista de valor multiplicado do primeiro calculo') #verificação do calculo

    Soma_Calculo1 = 0
    for soma in mult_calc1:
        Soma_Calculo1 = Soma_Calculo1 + soma
    # print(f'Soma da Multiplicação calulo {Soma_Calculo1}') #verificação do calculo
    # calculo do modulo do calculo 1
    modulo_cal1 = 11 - (Soma_Calculo1 % 11)
    # print(f'{modulo_cal1} modulo do cálculo 1') #verificação do calculo
    # Orientação para Validar resultado do Primeiro Digito.
    if modulo_cal1 > 9:
        Primeiro_Digito = 0
    else:
        Primeiro_Digito = modulo_cal1

    # # # # # Segundo Calculo da Validação do CPF. # # # # #

    # adiciona na lista do calculo1 o resultado do primeiro Digito.
    L_calc_1.append(Primeiro_Digito)
    #print(L_calc_1) # Print de controle de calculo.
    cont_2 = 12
    mult_calc2 = []
    for n_calc2 in L_calc_1:
        cont_2 -= 1
        Valor_Calc2 = n_calc2*cont_2
        mult_calc2.append(int(Valor_Calc2))
    # print(f'{mult_calc2} checagem da multiplicação calculo 2.') #verificação do calculo
    # Calculando a Soma do Segundo Calculo.
    Soma_Calculo2 = 0 # zerando a Variavel
    for n_soma2 in mult_calc2:
        Soma_Calculo2 = Soma_Calculo2 + n_soma2
    # print(f'Resultado da soma{Soma_Calculo2}') #verificação do calculo
    # Calculo do modulo do segundo digito.
    modulo_cal2 = 11-(Soma_Calculo2 % 11)
    #  print(f'Validando o segundo digito {modulo_cal2}') #verificação do calculo
    if modulo_cal2 > 9:
        Segundo_Digito = 0
    else:
        Segundo_Digito = modulo_cal2
    # Validando o CPF com o digitado,
    # Neste calculo monta a lista com os digitos do validador do CPF.
    # Está adicionando apenas o segundo digito neste momento pois para o calculo do segundo já foi
    # adicionao o primeiro digito.
    L_calc_1.append(Segundo_Digito)
    novo_cpf = L_calc_1
    #print(f'{novo_cpf} lista do novo CPF') #verificação do calculo
    # está comparando as duas listas a digitada pelo usúario e a do cálculo.
    if novo_cpf == lista_cpf:
        print(f'O CPF {cpf} é valido')
    else:
        print(f'O CPF {cpf} é invalido')

else:
    print('Por favor digite 11(onze) números sendo apenas números do cpf sem pontos ou digitos.')