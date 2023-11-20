"""Primera parte. Importamos módulos y utilidades necesarias para el programa."""
import os
import random
    # Importa la utilidad random para elegir el número aleatorio.
import sys
    # Importa la utilidad sys para tratar las excepciones.
from entrada.menu import nivel
from entrada.jugar import *

"""Segunda parte. Define la función (jugar_ia) que recibe una variable (dificultad)
    y devuelve otra (intentos_ia) o (intentos_jugador) dependiendo del ganador"""

def jugar_ia(dificultad):
    os.system("cls")
    print("************************************************")
    print("********** ¡VAS A JUGAR CONTRA LA IA! **********")
    print("**************EN EL NIVEL ",dificultad+1,"******")

    """Valores necesarios para el programa"""

    if dificultad==0:
        max=100
    elif dificultad==1:
        max=1000
    elif dificultad==2:
        max=1000000
    else:
        max=1000000000000
    #En función del número aportado (dificultad) se marca el número máximo del juego.
    aleatorio = random.randint(0,max)
    #Almacenamos en la variable (aleatorio) el número elegido al azar entre 0 y el máximo que debemos adivinar. 
    os.system("cls")
    print(aleatorio)
    #Imprime el número a adivinar para controlar la funcionalidad del juego. 
    #En el juego final se escribe una almohadilla (#) delante de print para ocultar el número.
    min_ia = 0
    max_ia = max
    #En estas variables recoge el intervalo de números que la IA utilizará para dar su número.
    intentos_jugador = 0
    intentos_ia = 0
    # Variables para sumar los intentos del jugador (intentos_jugador) y de la IA (intentos_ia).
    
    """Bucle con las opciones del juego."""
    while True:
        print("Ahora elige número la IA")
        intento_ia=(min_ia + max_ia)//2
        #Comienza jugando la IA. El mejor número para este juego siempre es el que está en el centro del intervalo,
        #porque va eliminando la mitad de los números que quedan para seleccionar.
        print("La IA ha seleccionado este número ->",intento_ia,"<-.")
        #Enseña al jugador el número elegido por la IA
        intentos_ia += 1
        #Suma un intento a la variable que controla los intentos de la IA.
        if intento_ia != aleatorio:
            if intento_ia > aleatorio:
                print("Numero de IA demasiado grande")
                max_ia = intento_ia-1
                #Redefine el intervalo ajustando el valor máximo a este intento fallido menos uno, porque es muy grande.
            else:
                print("Numero de IA demasiado pequeño")
                min_ia = intento_ia+1
                #Redefine el intervalo ajustando el valor mínimo a este intento fallido más uno, porque es muy pequeño.
        else:
            print("Ha ganado la Inteligencia Artificial en ",intentos_ia," intentos")
            return intentos_ia
            #La función (jugar_ia) devolverá el número de intentos de la IA porque ha acertado el número.

        print("Es su turno para elegir número")
        intento_jugador = tunumero(max)
        #Asigna a la variable (intento) el valor devuelto por la función tunumero(max) correspondiente al intento del jugador
        intentos_jugador += 1
        #Suma uno a la variable (intentos) que recoge el número de intentos del jugador
        if intento_jugador != aleatorio:
        #Si el intento del jugador (intento) es distinto del número aleatorio (numero), volverá al primer bucle.
            if intento_jugador > aleatorio:
            #Si el intento del jugador (intento) es mayor que el número aleatorio (numero), aparece el mensaje siguiente.
                print("Fallaste. El número es demasiado grande")
                max_ia = intento_jugador-1
                #Redefine el intervalo de la IA ajustando el valor máximo a este intento fallido menos uno.
            else:
                #En caso contrario el intento es menor que el número aleatorio y aparece el mensaje siguiente.
                print("Fallaste. El número es demasiado pequeño")
                min_ia = intento_jugador+1
                #Redefine el intervalo de la IA ajustando el valor mínimo a este intento fallido más uno.
        else:
        #Se ejecuta en caso de que el jugador acierte el número. Se termina el juego.
            print("Ganaste. Has utilizado ",intentos_jugador," intentos")
            return intentos_jugador
            #La función (jugar_ia) devolverá el número de intentos del jugador porque es el vencedor.
