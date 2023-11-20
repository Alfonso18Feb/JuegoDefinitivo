import os
import time
def nivel(control):
    os.system("cls")
    #Limpiamos la pantalla para comenzar el juego
    while True:
        print("************************************************")
        print("*********** JUEGO ADIVINAR EL NUMERO ***********")
        print("********* Elije un nivel de dificultad *********")
        print("* 1. Nivel SIMPLE entre 0 y 100 ****************")
        print("* 2. Nivel INTERMEDIO entre 0 y 1.000 **********")
        print("* 3. Nivel AVANZADO entre 0 y 1.000.000 ********")
        print("* 4. Nivel EXPERTO entre 0 y 1.000.000.000.000 *")
        print("* 5. Juega contra la INTELIGENCIA ARTIFICIAL ***")
        print("************************************************")
        opcion=int(input("¿SELECCIONE EL NIVEL DE JUEGO?"))
        if 1 <= opcion <=4:
            opcion = opcion -1
            #Resta uno para que las opciones vayan de 0 a 4 y exista concordancia 
            #con la forma de almacenar los datos que comienza con la posición cero.
            return opcion
        elif opcion == 5 and control == 0:
         #Si en la primera selección el juegador a decidido la opción 5 el valor de (control) tiene valor cero del juego principal.
            os.system("cls")
            print("************************************************")
            print("********** ¡VAS A JUGAR CONTRA LA IA! **********")
            print("******SELECCIONA UN NIVEL DE DIFICULTAD*********")
            control=1
            #Suma uno a la variable (control) por si en la petición de nivel se vuelve a pulsar el nivel 5 de nuevo.

        elif opcion==5 and control==1:
         #Se ejecuta cuando pulsa la opción 5 en repetidas ocasiones.
            os.system("cls")
            print("TIENES QUE ELEGIR UN NUMERO ENTRE 1 Y 4")
            time.sleep(3)
        else:
         #Se ejecuta en acso de que el usuario pulse algo que no sea 1,2,3,4 o 5.
            os.system("cls")
            print("---->OPCIÓN INCORRECTA<----")
            print("ELIJA UN NÚMERO ENTRE 1 Y 5")
            time.sleep(3)
                 