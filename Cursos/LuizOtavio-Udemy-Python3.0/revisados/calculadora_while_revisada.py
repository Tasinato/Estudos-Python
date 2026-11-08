"""Revisão didática do exercício LacosdeRepeticao.py.

Contexto original: curso de Luiz Otávio (Luiz Miranda), Udemy.
Estudante: Rafael Tasinato. O arquivo original foi preservado.
Objetivo: praticar while, break, continue, condicionais e validação de entrada.
"""

from math import isfinite


while True:
    sair = input("Deseja sair? Digite [s] para sim ou [n] para não: ").strip().lower()
    if sair == "s":
        print("Tudo bem, até mais!")
        break
    if sair != "n":
        print("Digite apenas s ou n.")
        continue

    # float aceita negativos e decimais; ValueError trata entradas não numéricas.
    try:
        num_1 = float(input("Digite o primeiro número (use ponto para decimais): "))
        num_2 = float(input("Digite o segundo número (use ponto para decimais): "))
    except ValueError:
        print("Entrada inválida. Digite dois números usando ponto para decimais.")
        continue

    if not isfinite(num_1) or not isfinite(num_2):
        print("Digite números finitos.")
        continue

    operador = input("Digite um operador (+, -, *, /): ").strip()
    if operador == "+":
        resultado = num_1 + num_2
    elif operador == "-":
        resultado = num_1 - num_2
    elif operador == "*":
        resultado = num_1 * num_2
    elif operador == "/":
        if num_2 == 0:
            print("Erro: divisão por zero não é permitida.")
            continue
        resultado = num_1 / num_2
    else:
        print("Operador inválido. Utilize +, -, * ou /.")
        continue

    if not isfinite(resultado):
        print("O resultado excedeu a capacidade numérica desta calculadora.")
        continue
    print(f"Resultado: {resultado}")
