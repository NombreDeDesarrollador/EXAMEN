from funciones import *


while True:
    os.system("cls")
    print("\tMENÚ")
    print("""1. Asignar sueldos aleatorios.
2. Clasificar sueldos.
3. Ver estadísticas.
4. Reporte de sueldos.
5. Salir del programa.""")
    try:
        opc = int(input("Ingrese una opción: "))
        if opc==(1, 2, 3, 4, 5):
            break
        else:
            print("\tLAS OPCIONES SOLO SON 1, 2, 3, 4 Y 5!")
    except:
            print("SOLO SE DEBE INGREAR UN NÚMERO ENTERO!")

    os.system("cls")
    if opc==1:
        asignar_sueldos_aleatorios()
    elif opc==2:
        mostrar_sueldos()
    elif opc==3:
        ver_estadisticas()
    elif opc==4:
        reporte_sueldos()
    else:
        salir()

    time.sleep(3)

