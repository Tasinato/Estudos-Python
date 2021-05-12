"""
Exercício de Estrutura de Repetição: Professor Luiz Otávio. - Udemy.

While / Else - Aula 19.1
Contadores
Acumuladores

contador = 50 # inicia em 50.
ex: Básico.
while contador <= 1000:
    print(contador)
    contador += 1 # soma + 1 em contador
"""
#Exemplo comentado. 

#Varíaveis
contador   = 1
acumulador = 1

#laço de repetição.

while contador <= 10:
    print(contador, acumulador)
    if contador >5:   # if condicional para executar o break
        break         # break foi adiconado para sair do laço de repetição e pular o else.
    acumulador = acumulador + contador
    contador += 1 # += é igual a contador = x + 1 
else:  # só executa quando esta opção do laço de repetição for falsa.
    print('Cheguei no else. só se for executado dentro do laço de repetição') # só ira participar 
# print que executa fora do laço de repetição.
print('Isso será executado. quando sai do laço de repetição ')