#Autor: ACO_626

import random
from datetime import datetime

numero_agente = random.randint(100,1000)
nombre_agente = "agente" + str(numero_agente)

print("¡Bienvenido Agente!")
nombre = input("Empecemos con las pruebas de capacidad de memoria, ¿cuál es su nombre? : ")


print("\n\nMmmmmmm veo que usted no recuerda bien las instruccines que se le dieron")
print(f"Clásico de los novatos, mira la respuesta a tu nombre es: {nombre_agente}")
print("no lo volveré a repetir, así que")
nombre_in =  input("¿Cuál es su nombre? : ")

if nombre_in == nombre_agente:

    print("\n\nExcelente, hora de que empieces tu viaje (jala una palanca)")
    print("ves borroso, te sientes mariado, pero ves una luz, estás en una cueva")
    print("el aire se siente bastante limpio, luces como un cavernícola")
    
    while True:

        print("Puedes salir de la cueva o quedarte a investigar qué prefieres")
        print("1) salir")
        print("2) investigar")

        opcion = input()

        if opcion == "2" or opcion == "investigar":

            print("\n\nDecidiste investigar y encuentras un trozo de carbón")
            
            while True:

                print("¿Qué decides hacer, indica con número?")
                print("1) Escribir en la cueva")
                print("2) Salir de la cueva")

                opcion = input()

                if opcion == "1":

                    while True:

                        print("¿Qué vas a escribir en la cueva?")
                        print("1) Tu nombre")
                        print("2) Un palito")
                        
                        opcion = input()
                        
                        if opcion == "1":
                            
                            print("\n\nHas cambiado la historia, tu realidad colapsa y mueres")
                            print("FIN DEL JUEGO")
                            exit()

                        elif opcion == "2":

                            print("\n\nFelicidades creaste el 1 en sistema unario")
                            print("Ahora eres transportado a otra realidad, te mareas")
                            

                            while True:

                                print("\n\nPareces estar en la antigua China, en una ceremónia")
                                print("Estábas a punto de dibujar algo en una pared, ¿Qué dibujas? ")
                                print("1) Un ave fenix")
                                print("2) Un ovni con un astronauta")
                                print("3) Un ying yang")
                                print("4) Un corazón")

                                opcion = input()

                                if opcion == "3":

                                    print("\n\nVaya, así que has creado el Ying y el Yang, la dualidad, bases de la lógica, felicidades")
                                    print("Eres transportado a una nueva era, parece ser el siglo XIX")
                                    print("Estabas escribiendo un libro llamado \n An Investigation of the Laws of Thought on Which are Founded the Mathematical Theories of Logic and Probabilities")
                                    print("Con qué nombre firmas: ")

                                    nombre_firma = input()

                                    if nombre_firma == "George Boole" or nombre_firma == "Boole" or nombre_firma == "boole" or nombre_firma == "george boole":
                                        
                                        print(f"\n\nVaya qué eres bueno {nombre_agente}")
                                        print("Vamos a tu penúltimo nivel")
                                        print("Estás frente a una computadora, más bien parece ser una terminal,\ntienes una instrucción printf(\"\") pero no sabes que poner entre comillas")

                                        while True:
                    
                                            print("¿Qué vas a escribir? ")

                                            cadena = input()
                                            
                                            if cadena == "Hola mundo" or cadena == "Hello world" or cadena == "Hello world!" or cadena == "Hello World" or cadena == "hola mundo":

                                                print(f"\n\nExcelente {nombre_agente} haz superado la prueba")
                                                print("Ahora vayamos al nivel final, una vez pasado puedes volver a casa\n\n")
                                                
                                                fecha_actual = datetime.now()
                                                
                                                print(f"Aparces frente a tu ordenador, esta vez no te sientes mareado,\nte haces llamar {nombre}, ves en el ordenador y es {fecha_actual.strftime("%H:%M")}")
                                                print("Parecías haber estado jugando un juego en python de Ficción interactiva,\n¿Qué vas a hacer ahora? : ")

                                                ultima_respuesta = input()

                                                print("En espera de resultados.....")
                                                print("LE DESEO SUERTE AGENTE")

                                                exit()
                                            
                                            else:

                                                print(f"\n\n{cadena} no era lo que debiste poner, parece que creaste una realidad alterna dónde hay una práctica llamada {cadena}, una tradición entre programadores al hacer su primer código")
                                                print("Has sido desconectado por el cuartel, fuiste eliminado")
                                                print("FIN DEL JUEGO")

                                                exit()

                                    else:

                                        print(f"\n\n{nombre_firma}, ¿es en serio?")
                                        print("Tal parece que olvidaste a quien no debe ser olvidado, mereces ser eliminado")
                                        print("(Todo se pone oscuro), has sido eliminado")
                                        print("FIN DEL JUEGO")

                                        exit()

                                elif opcion == "1":
                                 
                                    print("\n\nTe ha quedado horrible, nadie entendió y te abuchean")
                                
                                elif opcion == "2":

                                    print("\n\nFelicidades creaste un futuro con una religión de conspiranóicos, fallaste en tu misión")
                                    print("FIN DEL JUEGO")

                                    exit()
                                
                                elif opcion == "4":

                                    print("\n\nLa gente de la ceremonia te hace preguntas, pero tu no entiendes porque hablan chino, te abuchean y se van, vives una vida tranquila en la antigua china y mueres a los 58, fallaste en tu misión")
                                    print("FIN DEL JUEGO")

                                    exit()

                                else:

                                    print("Acción inválida")
                        else:
                            print("Acción invalida")

                elif opcion == "2":

                    print("\n\nSales estiras las piernas")
                    print("Ves lo que parece ser un mundo prehistórico un mundo nuevo")
                    print("Te sientes entusiasmado y de pronto, llega un dientes de sable y te come")
                    print("FIN DEL JUEGO")

                    exit()
                
                else:

                    print("Acción inválida")

        elif opcion == "salir" or opcion == "1":

            print("\n\nSales estiras las piernas")
            print("Ves lo que parece ser un mundo prehistórico un mundo nuevo")
            print("Te sientes entusiasmado y de pronto, llega un dientes de sable y te come")
            print("FIN DEL JUEGO")

            exit()
        
        else:

            print("Acción inválida")

else:

    print("\n\nEste no sirve, eliminalo")
    print("(sientes algo en la cabeza), usted ha sido eliminado")
    print("FIN DEL JUEGO")

