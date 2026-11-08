"""Revisão didática do exercício IterandoStringWhile.py.

Contexto original: curso de Luiz Otávio (Luiz Miranda), Udemy.
Estudante: Rafael Tasinato. O arquivo original foi preservado.
Objetivo: percorrer uma frase com while e colocar a letra escolhida em maiúscula.
"""

frase = "O Rato roeu a roupa do Rei de Roma"

while True:
    letra_escolhida = input("Qual letra deseja colocar em maiúscula? ").strip()
    if len(letra_escolhida) == 1 and letra_escolhida.isalpha():
        break
    print("Digite somente uma letra.")

contador = 0
nova_string = ""

while contador < len(frase):
    letra_atual = frase[contador]
    # Compara a letra da frase com a escolha, ignorando maiúsculas/minúsculas.
    if letra_atual.lower() == letra_escolhida.lower():
        nova_string += letra_atual.upper()
    else:
        nova_string += letra_atual
    contador += 1

print(nova_string)
