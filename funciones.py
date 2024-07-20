import time, os, random, re

lista_vehiculos = []

def limpiar_pantalla():
    os.system("cls")

def salir():
    print("Programa finalizado")
    print("Escrito por Claudio Andres Mattos Mattos; Evaluación Recuperativa Prueba Numero 3; Version 1.0")
    time.sleep(5)

def validador_de_patente(patente):
    return bool(re.match(r'^[BCDFGHJKLPRSTVWXYZ]{4}\d{2}$', patente))

def validador_de_marca(marca):
    return 2 <= len(marca) <= 15

def grabar():
    tipo = input("Ingrese el tipo de vehículo. Las opciones son: AUTO, CAMION, CAMIONETA, MOTO (se deben respetar las mayusculas):\t")
    while tipo  not in ["AUTO","CAMION","CAMIONETA","MOTO"]:
        tipo = input("Datos ingresados no validos. Reingrese el tipo de vehículo; Las opciones son: AUTO, CAMION, CAMIONETA, MOTO:\t")
    #Fin del while

    patente = input("Ingrese la patente del vehículo, debe contener 4 letras y 2 números (EJ BBBB10): ")

    #En septiembre de 2007 se comenzó a utilizar el nuevo formato, que se conforma por 4 letras y 2 números (BB-BB·10). 
    #Este sistema utiliza 18 letras que son: B, C, D, F, G, H, J, K, L, P, R, S, T, V, W, X, Y, Z. 
    #No se emplean las letras M, N, Ñ, Q (por su parecido con la O y el número 0) y las vocales 
    #(para evitar combinaciones que forman palabras y así incomodar a los conductores de los vehículos).
    #https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_Chile#:~:text=No%20se%20emplean%20las%20letras,los%20conductores%20de%20los%20veh%C3%ADculos).
    
    while not validador_de_patente(patente):
        patente = input("Datos ingresados no validos. Reingrese la patente del vehículo: ")
    #Fin del while
    
    marca = input("Ingrese la marca del vehículo: ")
    while not validador_de_marca(marca):
        print("Marca no valida, debe contener entre 2 y 15 caracteres")
        marca = input("Ingrese la marca del vehículo: ")
    #Fin del while

    try:
        precio = int(input("Ingrese el precio del vehículo: "))
        if precio <= 5000000:
            print("Precio no valido")
            precio = int(input("Ingrese el precio del vehículo, deber ser mayor a $5.000.000: "))
    except:
        print("Datos ingresados no validos")

    multas = []

    try:
        cantidad_de_multas = int(input("Ingrese la cantidad de multas del vehículo: "))
    except:
        print("Datos ingresados no validos")

    for i in range(cantidad_de_multas):
        while True:
            try:
                monto = int(input("Ingrese el monto de la multa: "))
                if monto <=0:
                    print("Monto no valido, intente nuevamente: ")
                else:
                    while True:
                        while True:
                            try:
                                dia_multa = int(input("Ingrese el dia de la multa, debe ser entre 1 a 31: "))
                                if dia_multa <=0 or dia_multa > 31:
                                    print("Dia no valido, intente nuevamente")
                                else:
                                    break
                            except:
                                print("Datos ingresados no validos")
                        
                        while True:
                            try:
                                mes_multa = int(input("Ingrese el mes de la multa, debe ser entre 1 a 12: "))
                                if mes_multa <=0 or mes_multa > 12:
                                    print("Mes no valido, intente nuevamente")
                                else:
                                    break
                            except:
                                print("Datos ingresados no validos")
                        
                        while True:
                            try:
                                year_multa = int(input("Ingrese el año de la multa, debe ser entre 1970 y 2024: "))
                                if year_multa < 1970 or year_multa > 2024:
                                    print("Año no valido, intente nuevamente")
                                else:
                                    break
                            except:
                                print("Datos ingresados no validos")
                        
                        fecha_multa = f"{dia_multa:02d}-{mes_multa:02d}-{year_multa}"
                        print(f"La fecha de la multa registrada es: {fecha_multa}")
                        break       
                multas.append({"monto": monto, "fecha": fecha_multa})
                break
            except:
                print("Datos ingresados no validos")   
        #Fin del while
    #Fin del for

    while True:
        while True:
            try:
                dia = int(input("Ingrese el dia de registro del vehiculo, debe ser entre 1 a 31: "))
                if dia <=0 or dia > 31:
                    print("Dia no valido, intente nuevamente")
                else:
                    break
            except:
                print("Datos ingresados no validos")
        
        
        while True:
            try:
                mes = int(input("Ingrese el mes de registro del vehiculo, debe ser entre 1 a 12: "))
                if mes <=0 or mes > 12:
                    print("Mes no valido, intente nuevamente")
                else:
                    break
            except:
                print("Datos ingresados no validos")
        #Fin del while
        
        while True:
            try:
                year = int(input("Ingrese el año de registro del vehiculo, debe ser entre 1970 y 2024: "))
                if year < 1970 or year > 2024:
                    print("Año no valido, intente nuevamente")
                else:
                    break
            except:
                print("Datos ingresados no validos")
        #Fin del while
        
        fecha_de_registro_del_vehiculo = f"{dia:02d}-{mes:02d}-{year}"
        print(f"La fecha de registro del vehiculo es: {fecha_de_registro_del_vehiculo}")
        break

    nombre_del_dueno_del_vehiculo = input("Ingrese el nombre del dueño del vehiculo: ")
    while nombre_del_dueno_del_vehiculo.strip() == "":
        print("No se aceptan campos vacios, intente nuevamente")
        nombre_del_dueno_del_vehiculo = input("Ingrese el nombre del dueño del vehiculo: ")
    #validar que no este vacio

    vehiculo = {
        "tipo": tipo,
        "patente": patente,
        "marca": marca,
        "precio": precio,
        "multas": multas,
        "fecha de registro del vehiculo": fecha_de_registro_del_vehiculo,
        "nombre del dueño del vehiculo": nombre_del_dueno_del_vehiculo
                }
    lista_vehiculos.append(vehiculo)
    print("Datos registrados exitosamente")

def buscar_vehiculo():
    patente = input("Ingrese la patente del vehiculo a buscar: ")
    for vehiculo in lista_vehiculos:
        if vehiculo["patente"] == patente:
            print(f"Tipo: {vehiculo['tipo']}")
            print(f"Patente: {vehiculo['patente']}")
            print(f"Marca: {vehiculo['marca']}")
            print(f"Precio: {vehiculo['precio']}")
            print(f"Multas: {vehiculo['multas']}")
            print(f"Fecha de registro: {vehiculo['fecha de registro del vehiculo']}")
            print(f"Nombre del dueño: {vehiculo['nombre del dueño del vehiculo']}")
            return
    print("Vehiculo no encontrado.")

def imprimir_certificados():
    patente = input("Ingrese la patente del vehiculo para imprimir certificados: ")
    for vehiculo in lista_vehiculos:
        if vehiculo["patente"] == patente:
            certificados = ["Emisión de contaminantes", "Anotaciones vigentes", "Multas"]
            for certificado in certificados:
                valor = random.randint(1500, 3500)
                print(f"Certificado de {certificado}")
                print(f"Patente: {vehiculo['patente']}")
                print(f"Nombre del dueño: {vehiculo['nombre del dueño del vehiculo']}")
                print(f"Valor: {valor}\n")
            return
    print("Vehiculo no encontrado.")