from funciones import *
import time, os, random, re
while True:

    print("Bienvenido a la automotora Auto Seguro")
    print("Para iniciar, seleccione una opción")
    print("1. Grabar datos de un vehículo")
    print("2. Buscar datos de un vehículo mediante la patente")
    print("3. Imprimir certificados")
    print("4. Salir")

    try:
        opcion = int(input("ingrese opción: "))
        if opcion == 1:
            limpiar_pantalla()
            grabar()
            time.sleep(10)
            limpiar_pantalla()

        elif opcion == 2:
            limpiar_pantalla()
            buscar_vehiculo()
            time.sleep(10)
            limpiar_pantalla()

        elif opcion == 3:
            limpiar_pantalla()
            imprimir_certificados()
            time.sleep(10)
            limpiar_pantalla()

        elif opcion == 4:
            limpiar_pantalla()
            salir()
            break
                
    except:
        print("opción ingresada no valida")