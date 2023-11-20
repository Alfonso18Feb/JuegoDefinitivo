"""Primera parte. Importamos módulos y utilidades necesarias para el programa."""
import os
import random
    # Importa la utilidad random para elegir el número aleatorio.
import sys
    # Importa la utilidad sys para tratar las excepciones.

"""Función jugar(dificultad). Toma el numero del nivel de dificultad elegido (dificultad)
    Devuelve el número de intentos necesarios para averiguar el número (intentos)"""
def jugar(dificultad):

    if dificultad==0:
        max=100
    elif dificultad==1:
        max=1000
    elif dificultad==2:
        max=1000000
    else:
        max=1000000000000
    aleatorio = random.randint(0,max)
    #Seleccionamos el número aleatorio en función de la dificultad elegida.
    intentos = 0
    # Variable para sumar los intentos del jugador.
 
    #Imprime el número a adivinar para controlar la funcionalidad del juego.
    # print(aleatorio)
    #En el juego final se escribe una almohadilla (#) delante de print para ocultar el número.

    """Bucle con las opciones del juego."""
    while True:
    #Iniciamos el primer bucle para contabilizar el número de intentos que necesita el jugador para adivinar el número.
        intento = tunumero(max)
        #Asigna a la variable (intento) el valor devuelto por la función tunumero(max) correspondiente al intento del jugador
        intentos += 1
        #Suma uno a la variable (intentos) que recoge el número de intentos del jugador
        if intento != aleatorio:
         #Si el intento del jugador (intento) es distinto del número aleatorio (numero), volverá al primer bucle.
            if intento > aleatorio:
             #Si el intento del jugador (intento) es mayor que el número aleatorio (numero), aparece el mensaje siguiente.
                print("Fallaste. El número es demasiado grande")
            else:
             #En caso contrario el intento es menor que el número aleatorio y aparece el mensaje siguiente.
                    print("Fallaste. El número es demasiado pequeño")
        else:
        #Se ejecuta en caso de que el jugador acierte el número. Se termina el juego.
            print("Ganaste. Has utilizado ",intentos," intentos")
            return intentos
            #En esta ocasión en lugar de salir del bucle con "break" lo hacemos asignando el valor "True"  la variable booleana "acierto".


"""Función tunumero(max). Toma el máximo valor del intervalo seleccionado (max)
    Devuelve el número elegido por el jugador (intento)"""
def tunumero(max):
    while True:
    # Iniciamos el segundo bucle para recoger el valor de cada intento y analizar que cumple las condiciones.
        try:
            intento = int(input("Adivina el número aleatorio  ¿Cual crees que es?"))
            #Asociamos el valor introducido por el jugador a la varible numérica "intento".
        except:
            print ("!Cuidado¡ No has escrito un número entero.")
            #Si por error el jugador escribe algo que no sea un número entero sale este mensaje.
            pass
            #Con "pass" se repite el segundo bucle apareciendo la pregunta del principio de nuevo.
        else:
        #Se ejecuta esta parte cuando el jugador introduce un número entero.
            if 0 <= intento <= max:
            #Se ejecuta si el numero introducido está entre 0 y max.
                break  # Salimos del segundo bucle.
            else:
            #Se ejecuta si el número introducido NO está entre 0 y 99.
                print("¡Error! El número que has escrito NO está entre 0 y ",max)
                #Devuelve este mensaje indicando del error y se inicia el segundo bucle de nuevo.
    return intento

"""Función jugardenuevo(). No recibe ningún valor.
    Devuelve el valor (False) si el jugador quiere abandonar el juego
    Devuelve el valor (True) si el jugador quiere seguir jugando """
def jugardenuevo():
    while True:
        juego=input("¿Quieres jugar de nuevo? (S/N)")
        if juego == "N" or juego == "n":
            print("Hasta la próxima partida.")
            return False
        elif juego == "S" or juego == "s":
            return True
        else:
            print("No es una opción válida. Contesta S,s o N,n")
            #Sólo en caso de que el jugador no seleccione bien aparece este mensaje.

