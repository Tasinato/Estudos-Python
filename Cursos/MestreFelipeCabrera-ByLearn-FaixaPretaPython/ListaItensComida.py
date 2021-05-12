"""
Exercicio Lista Comidas
Python por ByLearn, Professor Felipe Cabrera.]
Feito por Rafael Tasinato
@ByLearn
"""


# Varíaveis

frutas     = ['Maça','Banana','Pera','Uva']  #listc com o tipo string ou sejá é texto.
guloseimas = ['Bolacha','Batata','Fini','Chocolate']  #listc com o tipo string ou sejá é texto.
comidas    = ['Arroz', 'Feijão','Carne','Alface','Tomate']  #listc com o tipo string ou sejá é texto.
bebidas    = ['Refrigerante','Suco de Laranja','Aguá']  #listc com o tipo string ou sejá é texto.

categorias = ['Frutas', 'Guloseimas', 'Comidas', 'Bebidas']  #listc com o tipo string ou sejá é texto.
compras    = [frutas, guloseimas,comidas,bebidas]  # Criando uma lista com outras listas dentro.

for indice, categorias, in enumerate(categorias):
    print('Você precisa comprar' len(compras[indice]), categoria+ ':' )
    for compras in compras[indice]:
        print('-',compras)