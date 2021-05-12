"""
Professor: Luiz Otávio
Aluno: Rafael Tasinato
Plataforma - Udemy.
Matéria: Iterando strings com while em Python 
... continua.
"""

#                   Índices
#                0123456789------------------------
frase         = "O Rato roeu a roupa do Rei de Roma"
tamanho_frase = len(frase)
contador = 0  # variável de controle
# Variavel Exemplo 2
nova_string = ''
"""
while contador < tamanho_frase :
    print(frase[contador],contador)
    contador += 1


#Exemplo 2
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    nova_string += frase[contador]
    contador += 1
print(nova_string)
"""

#Exemplo 3 Iteração: ato de percorrer cada um dos elementos.
input_do_usuario = input("Qual letra deseja colocar maiúscula: ")

while contador < tamanho_frase:
    letra = input_do_usuario
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper() #define que a letra que o usuário digitar irá para maiuscula.
    nova_string += frase[contador]
    contador += 1
print(nova_string)