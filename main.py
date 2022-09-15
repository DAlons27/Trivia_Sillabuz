#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime
import time
import random

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

#Estado de la trivia
start_trivia = True

#Numero de Intentos
attempt_number = 0

#Meses del Año
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

#Colores de los textos
RED = '\033[31m'
RESET = '\033[39m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'

print(MAGENTA + "Bienvenido a mi trivia\n" + RESET)

print("Cargando...")

for i in range(5, 0, -1):
    time.sleep(1)
    print(i)

print(MAGENTA + "\nHola, cual es tu nombre: " + RESET)

name = input()
time.sleep(1)

print(MAGENTA + "\n!Que tal {}!... Siendo el {} de {}  demos inico a la trivia, SUERTE!\n".format(name, now.day, meses[now.month-1]) + RESET)

time.sleep(2)

print(MAGENTA + "Antes de comenzar, deseas algunos consejos, responde con si o no: " + RESET)

response = str(input()).lower()
count_1 = 0
time.sleep(1)

while count_1 == 0 and response == "si":
    print(MAGENTA + "\nTodos empezamos con un puntaje al azar, cada pregunta que contestes bien te dara 20 puntos, pero si contestas mal te restaran 20 puntos" + RESET)

    time.sleep(3)
    
    print(MAGENTA + "\nA continuacion debes responder las preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:" + RESET)

    time.sleep(3)
    count_1 += 1

time.sleep(1)
points = random.randint(50, 100)

print(YELLOW + "\nPuntaje actual: {}".format(points) + RESET)

print(MAGENTA + "Comencemos con las preguntas...\n" + RESET)
print("Cargando...")

for i in range(5, 0, -1):
    time.sleep(1)
    print(i)

while start_trivia == True:

    attempt_number += 1
    print(CYAN + "\nIntento número: {} ".format(attempt_number) + RESET)

    print("\n1) ¿Quién pintó Las meninas?: \n")
    print("a) Francisco de Goya")
    print("b) Diego Velázquez")
    print("c) Salvador Dalí")
    print("d) Diego Morey\n")

    response_1 = str(input("Tu respuesta: "))

    while response_1 not in ("a", "b", "c", "d"):
        response_1 = str(input("Debes responder a,b,c,d\n"))
    if response_1 == "b":
        time.sleep(1)
        print(GREEN + "Tu respuesta es correcta\n" + RESET)
    else:
        time.sleep(1)
        print(RED + "Tu respuesta es incorrecta\n" + RESET)

    if response_1 == "b":
        points += 20
    else:
        points -= 20

    time.sleep(2)

    print(YELLOW + "{}, tu puntaje actual es : {}\n".format(name, points) + RESET)

    time.sleep(2)

    print("Siguiente pregunta\n")

    print("2) ¿Cuál es la capital de Hungría? \n")
    print("a) Viena")
    print("b) Praga")
    print("c) Budapest")
    print("d) Estambul\n")

    response_2 = str(input("Tu respuesta: "))
    while response_2 not in ("a", "b", "c", "d"):
        response_2 = str(input("Debes responder a,b,c,d\n"))
    if response_2 == "c":
        time.sleep(1)
        print(GREEN + "Tu respuesta es correcta\n" + RESET)
    else:
        time.sleep(1)
        print(RED + "Tu respuesta es incorrecta\n" + RESET)

    if response_2 == "c":
        points += 20
    else:
        points -= 20

    time.sleep(2)

    print(YELLOW + "{}, tu puntaje actual es : {}\n".format(name, points) + RESET)

    time.sleep(2)

    print("Siguiente pregunta\n")

    print("3) Si P = M+N, ¿cuál de las siguientes fórmulas es correcta?\n")
    print("a) M = P + N")
    print("b) N = P + M")
    print("c) N = P / M")
    print("d) M = P - N\n")

    response_3 = str(input("Tu respuesta: "))
    while response_3 not in ("a", "b", "c", "d"):
        response_3 = str(input("Debes responder a,b,c,d\n"))
    if response_3 == "d":
        time.sleep(1)
        print(GREEN + "Tu respuesta es correcta\n" + RESET)
    else:
        time.sleep(1)
        print(RED + "Tu respuesta es incorrecta\n" + RESET)

    if response_3 == "d":
        points += 20
    else:
        points -= 20

    time.sleep(2)

    print(YELLOW + "{}, tu puntaje final en este intento es : {}\n".format(name, points) + RESET)

    print("¿Deseas intentar la trivia nuevamente?")
    repeat_trivia = str(input("Ingresa si para repetir, o presiona enter para finalizar: ")).lower()

    if repeat_trivia != "si":  
        print("\nEspero {} que lo hayas pasado bien, hasta pronto!".format(name))
        start_trivia = False
