"""Primera parte. Importar. Importa módulos y utilidades necesarias para el programa."""
import os
import time
import pickle
#Importa la utilidad (pickle) para almacenar las mejores puntuaciones
from entrada.menu import nivel
#Importa la función (nivel) alojada en el modulo (menu) dentro de la carpeta (entrada)
from entrada.jugar import *
from entrada.jugar_ia import jugar_ia

"""Segunda parte. Almacenar. Dentro de pickle.dump escribe el objeto con los niveles (niveles) 
y el objeto donde quiere escribir las mejores puntuaciones (mejor_puntuacion)"""

niveles=[100,1000,1000000,1000000000000]
#En (niveles) define los niveles de juego
pickle.dump(niveles,open("mejor_marca","wb"))
#Abre y crea el archivo (mejor_marca) par almacenar las mejores puntuciones.

"""Tercera parte. Jugar. Ejecuta el juego según la dificultad elegida con la función (nivel)
    contra la IA con la función (jugar_ia) o sólo el jugador con la función (jugar).
    De ambas funciones recibe la puntuación y la compara con el último récord.
    Termina preguntando siquiere jugar de nuevo con la función (jugardenuevo) que devuelve la respuesta del jugador,
    transformando la variable (jugando) en "False" si no quiere jugar más. """
control=0
 #Variable para controlar a un jugador torpe que pulse más de una vez la opción 5 del menú jugar con la IA.
jugando=True
 #Variable booleana para controlar la salida o no del juego.
while jugando:
 #Este bucle se repite hasta que el jugador decida salir del juego.
    record=pickle.load(open("mejor_marca","rb"))
    #Lee las mejores puntuaciones guardadas en el archivo mejor_puntuacion
    dificultad=nivel(control)
    #En la variable (dificultad) guarda el nivel seleccionado por el jugador.
    if dificultad == 4:
     #Nivel correspondiente al 5 para jugar con la IA
        dificultad=nivel(control)
        #A continuación debe seleccionar el nivel para jugar con la IA
        intentos=jugar_ia(dificultad)
        #Recoge en la variable (intentos) los intentos que ha necesitado para acertar el número.
    else:
     #Niveles del 1 al 4 jugador individual sin la IA
        intentos=jugar(dificultad)
        #Ejecuta la función (jugar) con los datos de dificultad actuales.
        #Guarda en la variable (intentos)  los intentos que ha necesitado para acertar el número.
    if intentos<record[dificultad]:
     #Comparamos los intentos utilizados en ganar con la mejor puntuación almacenada en en el nivel correspondiente.
     #Aquí la varible (dificultad) toma valor 0,1,2 o 3 correspondiente con las posiciones de Pickle.
        record[dificultad]=intentos
        #El nuevo récord en este nivel son los (intentos) que hemos necesitado.
        pickle.dump(record,open("mejor_marca","wb"))
        #Abrimos el archivo (mejor_marca) para escribir (wb) el nuevo récord.
        print("¡¡FELICIDADES HAY UN NUEVO RECORD!!")
        #Mensaje cuando se obtiene un nuevo récord.
    print("La mejor puntuación hasta ahora es de",record[dificultad],"intentos en este nivel")
    #Mensaje que sale siempre para indicar el récord actual.
    jugando=jugardenuevo()
    #Ejecuta la función (jugardenuevo) que devuelve el valor "True" o "False" para seguir jugando o salir del juego.
            