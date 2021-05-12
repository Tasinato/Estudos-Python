"""
#Exercicio com Lista de Repetição com dados inseridos pelo usuário.

Python por ByLearn, Professor Felipe Cabrera.]
Feito por Rafael Tasinato

Seman Jornada - PythonFaixaPreta
@ByLearn
"""

#cria a lista e a variavel para onde vái;
animais = []
animal  = input("Digite o nome de seu animal de estimação, caso não tenha digite 0")

while animal != '0':
    especie =input("Digite a Espécie deste animal")
    animais.append([animal, especie])
    animal = input('Se tiver mais animais, digite o nome dele. OU digite 0 se não tiver: ')
if len(animais) == '0':
    print('\n\nVocê não tem Animais.')
else:
    print("\n\nVocê tem os seguintes animais: ")
    for animal in animais:
        print("- Nome:", animal[0],"Espécie:", animal[1] )