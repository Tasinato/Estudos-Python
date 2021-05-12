"""
#Laços de Repetição com Validadores Lógicos.

#Exercicio com Lista de Repetição com dados inseridos pelo usuário.

Python por ByLearn, Professor Felipe Cabrera.]
Feito por Rafael Tasinato

Seman Jornada - PythonFaixaPreta
@ByLearn
"""

#Variáveis 
horario     = "Manhã"
clima       = "Ensolarado"
temperatura = "Quente"

#Inicio dos laços e operadores lógicos, and, or.
if horario == "Manhã" or horario == 'Tarde':
    if clima == "Ensolarado" and temperatura == "Quente":
        print("Uma pisina cairia bem, vou para pisina.")
    if (clima == "Ensolarado" and temperatura == "nublado") and (temperatura == "Amena" or temperatura == "frio"):
        print("Vamos Praticar algum esporte")
    if clima == "chuvoso":
        print("Vamos praticar Python")
else:
    if clima == "Chuvoso":
        print("Que tal um filme, serie ou exercícios físicos?")
    else:
        print("Um jantar fora parece interessante...")