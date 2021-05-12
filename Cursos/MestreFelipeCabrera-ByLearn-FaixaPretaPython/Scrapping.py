"""
Expressões Regulares 
Python por ByLearn, Professor Felipe Cabrera.
Feito por Rafael Tasinato
Exemplo de Busca: a palavra no texto
# Obs: na Busca é case sensitive ou seja ela procura a palvra como está escrita e irá diferenciar Maiuscula de Minuscula.
Exercícios da apostila do 1 ao 4
@ByLearn
"""

#ATENÇÃO \\ São 4 exercicios e todos precisam desta Biblioteca.  //ATENÇÃO 
import re

#Exercício 1

#Variáveis
texto  = "Venha se Tornar um ByLearner!"  #texto a ser pesquisado.
padrao = "ByLearner"                      #padrão que será buscado no texto. 

resultado = re.search(padrao,texto) #resultado do cálculo.

# Condicional e saida da informação.
if resultado:  
    print(f"Encontramos o padrão no texto, entre os índices,{resultado.start()} e {resultado.end()} ")
else:
    print("Não encontramos o padrão no texto")



#Exercício 2

texto01  = "O Rato roeu a Roupa do Rei de Roma" #texto no qual será procurado
padrao01 = r"Rato|Roupa|Rei"  #o que será procurado

ocorrencias = re.finditer(padrao01,texto01) #Calculo

#laço de busca.
for ocorrencias in ocorrencias:
    print(f"Encontrei:{ocorrencias.group()} entre os índices {ocorrencias.span()}")

#Exercício 3
#variáveis. 
texto02  = "O Rato roeu a Roupa do Rei de Roma"
padrao02 = r"R|r"
substituicao = r"g"

# neste exemplo cria um texto novo substituindo o R pelo G.
#                 (Lido,Substituição,Texto oriinal)
novo_texto = re.sub(padrao02,substituicao,texto02)
print(novo_texto)

#Exercício 4

#variáveis. 
texto03  ="Felipe Cabrera"
padrao03 =r"Felipe Cabrera" 
#chamdno os parámetros
regex=re.fullmatch(padrao03,texto03)

#Condicional.
if regex:
    print("Valido")
else:
    print("Inválido")