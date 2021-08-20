# Proyecto de Quién quiere ser millonario

# Agregar comodines de 50/50
# En el submenú de los comodines hay que agregar un mensaje por si ya se utilizó un comodín

import random
import time
import sys

juego = 1
contador_premio = 1
opciones = []

millonario = [
    ["Qué se celebra el 25 de julio en Costa Rica? ", "\nA. La Anexión del Partido de Nicoya",
        "\nB. La Independencia de Costa Rica", "\nC. Batalla de Rivas", "\nD. Día del niño", "A", "\nA. La Anexión del Partido de Nicoya"],
    ["En qué año llegó el hombre a la Luna? ",
        "\nA. 1960", "\nB. 1957", "\nC. 1985", "\nD. 1969", "D", "\nD. 1969"],
    ["De las siguientes selecciones de fútbol, cuál ha ganado más mundiales? ",
        "\nA. Argentina", "\nB. Brasil", "\nC. Alemania", "\nD. Italia", "B", "\nB. Brasil"],
    ["A qué país pertenece la isla de Creta? ", "\nA. Grecia",
        "\nB. Italia", "\nC. Portugal", "\nD. España", "A", "\nA. Grecia"],
    ["Cuál filósofo creó 'El mito de la caverna'? ", "\nA. Sócrates",
        "\nB. Platón", "\nC. Aristóteles", "\nD. Heráclito", "B", "\nB. Platón"],
    ["Cómo se llama el caballo de Don Quijote de la Mancha? ",
        "\nA. Bruno", "\nB. Sancho", "\nC. Pedro", "\nD. Rocinante", "D", "\nD. Rocinante"],
    ["Qué número viene después del 14 en los decimales de Pi? ",
        "\nA. 3", "\nB. 1", "\nC. 6", "\nD. 2", "B", "\nB. 1"],
    ["Qué elemento está presente en todas las moléculas orgánicas? ",
        "\nA. Carbono", "\nB. Hierro", "\nC. Calcio", "\nD. Sodio", "A", "\nA. Carbono"],
    ["Cuál es el continente mas grande del mundo? ", "\nA. Asia ",
        "\nB. Europa ", "\nC. África ", "\nD. América ", "D", "\nD. América"],
    ["Cuál de estos animales no pone huevo? ", "\nA. Ornitorrinco ",
        "\nB. Serpiente", "\nC. Foca", "\nD. Salamandra", "C", "\nC. Foca"],
    ["Los delfines son de sangre...? ", "\nA. Caliente",
        "\nB. Fria", "\nC. Azul", "\nD. Gris", "A", "\nA. Caliente"],
    ["Quién dirigió 'Ciudadano Kane'? ", "\nA. Charles Chaplin",
        "\nB. Orson Welles", "\nC. Steven Spielberg", "\nD. Martin Scorsese", "B", "\nB. Orson Welles"],
    ["Cuántos segundos tiene dos dias? ", "\nA. 172600",
        "\nB. 275800", "\nC. 172800", "\nD. 182700", "C", "\nC. 172800"],
    ["Entre que años se dessarrollo la Segunda Guerra Mundial? ",
        "\nA. 1939-1945", "\nB. 1940-1950", "\nC. 1910-1916", "\nD. 1937-1943", "A", "\nA. 1939-1945"],
    ["Cómo se llamaba Muhammad Ali antes de adoptar este nombre? ",
        "\nA. Victor Stone", "\nB. John Williams", "\nC. Ethan Hunt", "\nD. Cassius Clay", "D", "\nD. Cassius Clay"]
]
premios = ["0", "100000", "250000", "500000", "750000", "1000000", "2000000", "2500000",
                "3000000", "5000000", "7500000", "10000000", "12000000", "15000000", "20000000", "30000000"]


def preguntar():
    global numero_pregunta
    numero_pregunta = random.randint(0, 14)
    while numero_pregunta in opciones:
        numero_pregunta = random.randint(0, 14)
    opciones.append(numero_pregunta)
    formato_pregunta = millonario[numero_pregunta][0:5]
    pregunta = " ".join(map(str, formato_pregunta))
    print(pregunta)
    comodines()
    


def responder():
    global respuesta
    definitiva = "NO"
    while definitiva == "NO":
        respuesta = str(input("\nDigite su respuesta: ")).upper()
        definitiva = str(input("Respuesta definitiva? ")).upper()


def comodines():  # Se puede agregar un contador para que indique si ya se usó o no un comodín
    op = str(input("Desea utilizar un comodín? ")).upper()
    if op == "SI":
        print("\n1. 50/50")
        print("2. Videollamada")
        print("3. No usar comodin")
        opc = int(input("Seleccione el comodín que desea: "))
        if(opc == 1):
            cincuenta()
            responder()
        elif(opc == 2):
            videollamada()
            responder()
        elif opc == 3:
            responder()
    elif op == "NO":
        retirarse()
    else:
        print("Opción inválida\n")
        comodines()


def cincuentaxcincuenta():  # Hay que validar que no elimine la respuesta correcta
    global respuesta_correcta
    respuesta_correcta = millonario[numero_pregunta][6]
    cincuenta1 = random.choice(millonario[numero_pregunta][1:5])
    cincuenta2 = random.choice(millonario[numero_pregunta][1:5])
    if cincuenta1 != respuesta_correcta and cincuenta2 != respuesta_correcta and cincuenta1 != cincuenta2:
        # es una prueba, se puede eliminar
        print("///////////////////////"+cincuenta1)
        # es una prueba, se puede eliminar
        print("///////////////////////"+cincuenta2)
        cincuenta1_index = millonario.index(cincuenta1)
        cincuenta2_index = millonario.index(cincuenta2)
        millonario[cincuenta1_index] = ""
        millonario[cincuenta2_index] = ""
        millonario[numero_pregunta].remove(cincuenta1)
        millonario[numero_pregunta].remove(cincuenta2)
    else:
        while cincuenta1 == respuesta_correcta or cincuenta2 == respuesta_correcta:
            cincuenta1 = random.choice(millonario[numero_pregunta][1:5])
            cincuenta2 = random.choice(millonario[numero_pregunta][1:5])
            if cincuenta1 != respuesta_correcta and cincuenta2 != respuesta_correcta:
                print("///////////////////////"+cincuenta1)
                print("///////////////////////"+cincuenta2)
                cincuenta1_index = millonario.index(cincuenta1)
                cincuenta2_index = millonario.index(cincuenta2)
                millonario[cincuenta1_index] = ""
                millonario[cincuenta2_index] = ""
                # lista[n].remove(cincuenta1)
                # lista[n].remove(cincuenta2)
                break
    formato_pregunta = millonario[numero_pregunta][0:5]
    pregunta = " ".join(map(str, formato_pregunta))
    print(pregunta)

def cincuenta():
    global respuesta_correcta
    respuesta_correcta = millonario[numero_pregunta][6]
    cincuenta1 = random.choice(millonario[numero_pregunta][1:5])
    cincuenta2 = random.choice(millonario[numero_pregunta][1:5])
    if cincuenta1 != respuesta_correcta and cincuenta2 != respuesta_correcta and cincuenta1 != cincuenta2:
        borrar = {cincuenta1, cincuenta2}
        millonario[numero_pregunta] = [ele for ele in millonario[numero_pregunta] if ele not in borrar]
    # else:
    #     while cincuenta1 == respuesta_correcta or cincuenta2 == respuesta_correcta or cincuenta1 == cincuenta2:
    #         cincuenta1 = random.choice(millonario[numero_pregunta][1:5])
    #         cincuenta2 = random.choice(millonario[numero_pregunta][1:5])
    #         if cincuenta1 != respuesta_correcta and cincuenta2 != respuesta_correcta:
    #             borrar = {cincuenta1, cincuenta2}
    #             millonario[numero_pregunta] = [ele for ele in millonario[numero_pregunta] if ele not in borrar]
    formato_pregunta = millonario[numero_pregunta][0:3]
    pregunta = " ".join(map(str, formato_pregunta))
    print("\n" + pregunta)

def videollamada():
    print("\nA cuál conocido desea llamar?")
    print("1. Pepe")
    print("2. Julio")
    print("3. Luisa")
    opc = int(input("Escoja a la persona para hacer la videollamada: "))

    if(opc == 1):
        opc_pepe = random.choice(millonario[numero_pregunta][1:5])
        print("Pepe considera que la respuesta correcta es:", opc_pepe)
    elif(opc == 2):
        opc_julio = random.choice(millonario[numero_pregunta][1:5])
        print("Julio considera que la respuesta correcta es:", opc_julio)
    elif(opc == 3):
        opc_luisa = random.choice(millonario[numero_pregunta][1:5])
        print("Luisa considera que la respuesta correcta es:", opc_luisa)

def retirarse():
    opcion = str(input("Desea retirarse del juego? ")).upper()
    if opcion == "SI":
        print("\nSu premio es:", premios[contador_premio - 1], "colones")
        print("Gracias por jugar!")
        sys.exit()
    elif opcion == "NO":
        responder()
    else: 
        print("Opción inválida")
        retirarse()


print(time.strftime('%d-%m-%Y %H:%M', time.localtime()))
print("¡Bienvenido a Quien quiere ser millonario!")
print("-----------------Escalera de premios---------------------")
print("Pregunta 15: 30.000.000")
print("Pregunta 14: 20.000.000")
print("Pregunta 13: 15.000.000      (Zona segura 3)")
print("Pregunta 12: 12.000.000")
print("Pregunta 11: 10.000.000")
print("Pregunta 10: 7.500.000       (Zona segura 2)")
print("Pregunta 9: 5.000.000")
print("Pregunta 8: 3.000.000")
print("Pregunta 7: 2.500.000")
print("Pregunta 6: 2.000.000")
print("Pregunta 5: 1.000.000        (Zona segura 1)")
print("Pregunta 4: 750.000")
print("Pregunta 3: 500.000")
print("Pregunta 2: 250.000")
print("Pregunta 1: 100.000 \n")

preguntar()

while juego < 16:

    if millonario[numero_pregunta] in millonario:
        if respuesta == millonario[numero_pregunta][5]:
            print("\nRespuesta correcta!\nPremio:",
                (premios[contador_premio]), "colones\n")
        else:
            print("\nRespuesta incorrecta! \nRespuesta correcta:",
                millonario[0][5])
            if(premios.index(premios[contador_premio - 1]) < 5):
                print("Premio:", premios[0], "colones\n")
                print("----------------------------------------------------------")
                break
            elif (premios.index(premios[contador_premio - 1]) < 10):
                print("Premio:", premios[5], "colones\n")
                print("----------------------------------------------------------")
                break
            elif (premios.index(premios[contador_premio - 1]) < 13):
                print("Premio:", premios[10], "colones\n")
                print("----------------------------------------------------------")
                break
            elif (premios.index(premios[contador_premio - 1]) < 15):
                print("Premio:", premios[13], "colones\n")
                print("----------------------------------------------------------")
                break

    contador_premio = contador_premio + 1
    juego = juego + 1
    if juego != 16:
        preguntar()
