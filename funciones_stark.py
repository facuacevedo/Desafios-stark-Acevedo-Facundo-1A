
# PUNTO B
def nombre_superheroe(lista):
    for personaje in lista:
        print(f"nombre del personaje: {personaje['nombre']}")


# PUNTO C
def nombre_y_altura_personaje(lista):
    for personaje in lista:
        print(f"nombre del personaje: { personaje['nombre'] } y su altura: {personaje['altura']}")

# PUNTO D
def superheroe_mas_alto(lista):
    flag_mas_alto = True
    mas_alto = 0
    lista_mas_alto = []

    for personaje in lista:
        if flag_mas_alto or float(personaje["altura"]) >= float(mas_alto["altura"]):
            mas_alto = personaje
            flag_mas_alto = False

    for personaje in lista:
        if float(personaje["altura"]) >= float(mas_alto["altura"]):
            lista_mas_alto.append(personaje)

    for personaje in lista_mas_alto:
        print(f"El personaje mas alto es { personaje['nombre'] } y mide { personaje['altura']} ")

# PUNTO E
def superheroe_mas_bajo(lista):
    flag_mas_bajo = True
    mas_bajo = 0
    lista_mas_bajo = []

    for personaje in lista:
        if flag_mas_bajo or float(personaje["altura"]) <= float(mas_bajo["altura"]):
            mas_bajo = personaje
            flag_mas_bajo = False

    for personaje in lista:
        if float(personaje["altura"]) <= float(mas_bajo["altura"]):
            lista_mas_bajo.append(personaje)

    for personaje in lista_mas_bajo:
        print(f"El personaje mas bajo es { personaje['nombre'] } y mide { personaje['altura']} ")

# PUNTO F
def promedio_alturas(lista):
    acumulador_alturas = 0

    for personaje in lista:
        acumulador_alturas += float(personaje["altura"])

    print(f"El promedio de altura es: {acumulador_alturas / len(lista)}")

# PUNTO G
# HECHO EN LOS ANTERIORES PUNTOS
def superheroes_mas_alto_mas_bajo(lista):
    superheroe_mas_alto(lista)
    superheroe_mas_bajo(lista)

# PUNTO H
def superheroe_mas_y_menos_pesado(lista):
    flag_mas_pesado = True
    mas_pesado = 0

    flag_menos_pesado = True
    menos_pesado = 0

    lista_mas_pesado = []
    lista_menos_pesado = []

    for personaje in lista:
        if flag_mas_pesado or float(personaje["peso"]) >= float(mas_pesado["peso"]):
            mas_pesado = personaje
            flag_mas_pesado = False
        
        if flag_menos_pesado or float(personaje["peso"]) <= float(menos_pesado["peso"]):
            menos_pesado = personaje
            flag_menos_pesado = False

    for personaje in lista:
        if float(personaje["peso"]) >= float(mas_pesado["peso"]):
            lista_mas_pesado.append(personaje)

    for personaje in lista:
        if float(personaje["peso"]) <= float(menos_pesado["peso"]):
            lista_menos_pesado.append(personaje)

    for personaje in lista_mas_pesado:
        print(f"El personaje mas pesado es { personaje['nombre'] } y pesa { personaje['peso']} ")

    for personaje in lista_menos_pesado:
        print(f"El personaje menos pesado es { personaje['nombre'] } y pesa { personaje['peso']} ")

# PUNTO J
def funcion_menu_stark(lista):
    import os

    while True:
        os.system("cls")
        print("*********                MENU DE OPCIONES                 *********")
        print("-------------------------------------------------------------------")
        print("1. Nombre de los SuperHéroes.")
        print("2. Nombre y altura de los SuperHéroes.")
        print("3. Determinar cual es el SuperHéroes mas alto.")
        print("4. Determinar cual es el SuperHéroes mas bajo.")
        print("5. Determinar la altura promedio de los SuperHéroes.")
        print("6. Informar cual es el Nombre del SuperHéroe mas bajo y mas alto.")
        print("7. Informar cual es el SuperHéroe más pesado y el mas liviano.")
        print("8. Salir.")

        opcion_ingresada = input("Ingrese una opcion: ")

        if opcion_ingresada == "1":
            nombre_superheroe(lista)
        elif opcion_ingresada == "2":
            nombre_y_altura_personaje(lista)
        elif opcion_ingresada == "3":
            superheroe_mas_alto(lista)
        elif opcion_ingresada == "4":
            superheroe_mas_bajo(lista)
        elif opcion_ingresada == "5":
            promedio_alturas(lista)
        elif opcion_ingresada == "6":
            superheroes_mas_alto_mas_bajo(lista)
        elif opcion_ingresada == "7":
            superheroe_mas_y_menos_pesado(lista)
        elif opcion_ingresada == "8":
                auxConfirm = input("Desea salir del menu? s/n: ")
                if auxConfirm == "s":
                    break
        
        os.system("pause")



