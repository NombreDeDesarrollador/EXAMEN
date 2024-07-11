import random, time, os

trabajadores = ['Juan Pérez',
            'María García',
            'Carlos López',
            'Ana Martínez',
            'Pedro Rodríguez',
            'Laura Hernández',
            'Miguel Sánchez',
            'Isabel Gómez',
            'Francisco Díaz',
            'Elena Fernández']

dec_salud = 0.07
desc_afp = 0.12

lista_detalle = []
lista_sueldos_aleatorios_menores = []
lista_sueldos_aleatorios_entre = []
lista_sueldos_aleatorios_mayores = []
lista_de_sueldos_para_ordenar = []

def asignar_sueldos_aleatorios():

    while True:
        print("\tASIGNACIÓN DE SUELDOS ALEATORIOS")
        if not trabajadores:
            print("\tNO EXISTEN MAS TRABAJADORES PARA ASIGNAR")
            break
        else:

                nombre_trabajador = random.choice(trabajadores)
                print(nombre_trabajador)

                sueldo_aleatorio = random.randint(300000, 2500000)
                print(sueldo_aleatorio)
                
                descuento_de_salud = sueldo_aleatorio * dec_salud
                descuento_de_afp = sueldo_aleatorio * desc_afp
                sueldo_líquido = sueldo_aleatorio - descuento_de_salud - descuento_de_afp

                if sueldo_aleatorio<800000:

                    lista_sueldos_aleatorios_menores.append(nombre_trabajador and sueldo_aleatorio and descuento_de_salud and descuento_de_afp and sueldo_líquido)
                
                elif sueldo_aleatorio>800000 and sueldo_aleatorio<2000000:

                    lista_sueldos_aleatorios_entre.append(nombre_trabajador and sueldo_aleatorio and descuento_de_salud and descuento_de_afp and sueldo_líquido)

                elif sueldo_aleatorio>2000000:
                    lista_sueldos_aleatorios_mayores.append(nombre_trabajador and sueldo_aleatorio and descuento_de_salud and descuento_de_afp and sueldo_líquido)

                else:
                    ("si")
                
                lista_de_sueldos_para_ordenar.append(sueldo_aleatorio)
                
                lista_detalle.append(["NOMBRE",nombre_trabajador,
                                "SUELDO BASE", sueldo_aleatorio,
                                "DESCUENTO SALUD", descuento_de_salud,
                                "DESCUENTO AFP", descuento_de_afp,
                                "SUELDO LÍQUIDO", sueldo_líquido])

        trabajadores.remove(nombre_trabajador)

        print("\tSUELDO ALEATORIO ASIGNADO CON ÉXITO!")
            
        

def mostrar_sueldos():
    print("\tLISTA DE SUELDOS")
    print("Sueldos menores a $800.000 TOTAL: ",len(lista_sueldos_aleatorios_menores))
    if not lista_sueldos_aleatorios_menores:
        print("NO HAY SUELDOS MENORES DE $800.000")
    else:
        print(lista_sueldos_aleatorios_menores)
    print("Sueldos entre $800.000 y $2.000.000 TOTAL: ",len(lista_sueldos_aleatorios_entre))
    if not lista_sueldos_aleatorios_entre:
        print("NO HAY SUELDOS ENTRE $800.000 Y $2.000.000")
    else:
        print(lista_sueldos_aleatorios_entre)
    print("Sueldos superiores a $2.000.000 TOTAL: ",len(lista_sueldos_aleatorios_mayores))
    if not lista_sueldos_aleatorios_mayores:
        print("NO HAY SUELDOS MAYORES DE $2.000.000")
    else:
        print(lista_sueldos_aleatorios_mayores)



def ver_estadisticas():
    print("\tVER ESTADÍSTICAS")
    lista_de_sueldos_para_ordenar.sort
    print("El sueldo mas alto es: ", lista_de_sueldos_para_ordenar[9])
    print("El sueldo mas bajo es: ", lista_de_sueldos_para_ordenar[0])
    print("El promedio de los sueldos es: ", )
    print("La media geométrica es: ", )


def reporte_sueldos():
    print(lista_detalle)

def salir():
    print("""Finalizando programa...
Desarrollado por Matías Miranda
RUT 22.044.111-3""")
    exit()
    


    