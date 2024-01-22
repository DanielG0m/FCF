
#Daniel Camilo Gomez Ortiz 

import os
from tabulate import tabulate
os.system('cls')

titulo = """
#################################################
#      Federedacion Colombiana de Futbol        #
#################################################
"""

opciones = "1. Registra un equipo \n2. Registra los partidos \n3. Reporte\n4. Salir"
tg=0
equipos = []
pj=0 
pg=0
pp=0
pe=0
gf=0
gc=0
tp=0

while True:
    os.system('cls')
    print(titulo)
    print(opciones)
    print("Selecciona una opcion: ")
    op = int(input(">. "))

    if op == 1:
        name = input("Ingrese el nombre del equipo : ")
        ex=False
        for item in equipos:
            if name in item:
                ex=True
                break
        if ex:
            print("El equipo ya esta registrado. ")
            os.system('pause')
        else:
            id = str(len(equipos)).zfill(0)
            equipos.append([name, 0, 0, 0, 0, 0, 0, 0])
            os.system('pause')

    elif op == 2:
        l = input("Ingrese el equipo que jugo de local: ")
        lexist=False
        for item in equipos:
             if l in item[0]:
                  lexist=True
                  break
        if lexist == False:
             print("El equipo no ha sido registrado ")
             os.system('pause')
        else:
            v = input("Ingrese el equipo que jugo de visitante: ")
            vexist=False
            for item in equipos:
                 if v in item[0]:
                      vexist=True
                      break
            if vexist==False:
                print("El equipo no ha sido registrado ")
                os.system('pause')
            if l==v:
                 print("El equipo no puede jugar contra si mismo")
                 os.system('pause')
            else:
                marcadorlocal = int(input("Ingrese la cantidad de goles del equipo local: "))
                if marcadorlocal<0:
                    print("No puedes ingresar valores negativos")
                    os.system('pause')
                else:    
                    marcadorvisitante = int(input("Ingrese la cantidad de goles del equipo visitante: "))
                    if marcadorvisitante<0:
                        print("No puedes ingresar valores negativos")
                        os.system('pause')
                    else:
                        tg += marcadorlocal + marcadorvisitante
                        tp += 2
                        for i,item in enumerate (equipos):
                            if(l in item):
                                equipos[i][1] += 1
                                equipos[i][5] += marcadorlocal
                                equipos[i][6] += marcadorvisitante

                            elif(v in item):
                                equipos[i][1] += 1
                                equipos[i][5] += marcadorvisitante
                                equipos[i][6] += marcadorlocal

                        for i,item in enumerate (equipos):
                            if(l in item):
                                if(marcadorlocal > marcadorvisitante):
                                    equipos[i][2] += 1
                                    equipos[i][7] += 3
                                elif(marcadorlocal == marcadorvisitante):
                                    equipos[i][4] += 1
                                    equipos[i][7] += 1
                                else:
                                    equipos[i][3] += 1
                            elif(v in item):
                                if(marcadorvisitante > marcadorlocal):
                                    equipos[i][2] += 1
                                    equipos[i][7] += 3
                                elif(marcadorlocal == marcadorvisitante):
                                    equipos[i][4] += 1
                                    equipos[i][7] += 1
                                else:
                                    equipos[i][3] += 1
    elif op == 3:
        tabla_de_puntajes = print("Reporte FCF")
        print(tabulate(equipos,headers=["Equipo","PJ","PG","PP","PE","GF","GC","TP"]))
        print("")

        maxgoles = max(equipos, key=lambda n:n[5])
        equipos_maxgoles = [equipo[0] for equipo in equipos if equipo[5] == maxgoles[5]]
        if len(equipos_maxgoles) > 1:
            print("Los equipos con mas goles:", equipos_maxgoles)
        else:
            print("El equipo que hizo mas goles: ", equipos_maxgoles[0])
            maxpuntos= max(equipos, key=lambda n:n[7])
            print("El equipo que hizo mas puntos: ",maxpuntos[0])
        print("")

        maxvictorias=max(equipos, key=lambda n:n[2])
        equipos_maxvictorias = [equipo[0] for equipo in equipos if equipo[2] == maxvictorias[2]]
        if len(equipos_maxvictorias) > 1:
            print("Los equipos con mas victorias:", equipos_maxvictorias)
        else:
            print("El equipo con mas victorias: ", equipos_maxvictorias[0])
        print("")

        print("Total de goles anotados en el torneo: ",tg)

        print("")
        print("Promedio de cantidad de goles:  ",float(tg/tp))
        print("")
        os.system("pause")

    elif op == 4:
        print("Gracias por utilizar nuestro sistema")
        break