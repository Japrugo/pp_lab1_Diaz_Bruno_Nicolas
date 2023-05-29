from funciones_pp1 import *


def correr_programa():
    """
    - Se encarga de correr el programa principal
    - No recibe nada
    - No retorna nada
    """
    flag_segundo_punto = False

    while True:
        print("Menú de opciones:")
        print("1. Mostrar la lista de todos los jugadores del Dream Team.")
        print("2. Ingresar un indice para ver estadisticas completas de ese jugador.")
        print("3. Guardar archivo con estadistias completas del jugador elegido en el punto 2.")
        print("4. Buscar un jugador por nombre para ver sus logros.")
        print("5. Ver el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.")
        print("6. Ingresar nombre para ver si ese jugador es miembro del Salón de la Fama del Baloncesto.")
        print("7. Ver el jugador con la mayor cantidad de rebotes totales.")
        print("8. Ver el jugador con el mayor porcentaje de tiros de campo.")
        print("9. Ver el jugador con la mayor cantidad de asistencias totales.")
        print("10. Ingresar un valor y ver los jugadores que han promediado más puntos por partido que ese valor.")
        print("11. Ingresar un valor y ver los jugadores que han promediado más rebotes por partido que ese valor.")
        print("12. Ingresar un valor y ver los jugadores que han promediado más asistencias por partido que ese valor.")
        print("13. Ver el jugador con la mayor cantidad de robos totales.")
        print("14. Ver el jugador con la mayor cantidad de bloqueos totales.")
        print("15. Ingresar un valor y ver los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
        print("16. Ver el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
        print("17. Ver el jugador con la mayor cantidad de logros obtenidos.")
        print("18. Ingresar un valor y ver los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.")
        print("19. Ver cual es el jugador con la mayor cantidad de temporadas jugadas.")
        print("20. Ingresar un valor y ver los jugadores, ordenados por posición en la cancha, que tengan un porcentaje de tiros de campo superior a ese valor.")
        print("0. Salir del programa")
        
        opcion = input("\nIngrese la opcion deseada\n")
        
        while validar_menu(opcion) == False:
            opcion = input("Opcion invalida. Ingrese la opcion deseada\n")
            
        match opcion:
            case 1:
                mostrar_jugadores(lista_jugadores)

            case 2: 
                indice_elegido = input("Ingrese un indice para elegir un jugador de la lista y ver sus estadisticas (1 - 12)\n")
                
                indice_elegido = validar_dato_ingresado(lista_jugadores, indice_elegido)

                while indice_elegido < 1 or indice_elegido > 12:
                    indice_elegido = input("Indice invalido. Ingrese un indice para elegir un jugador de la lista y ver sus estadisticas (1 - 12)\n")
                    indice_elegido = validar_dato_ingresado(lista_jugadores, indice_elegido)

                indice_elegido -= 1
                estadistica_jugador = estadisticas_completas_jugador(lista_jugadores, indice_elegido)

                print(lista_jugadores[indice_elegido]["nombre"])
                for estadistica in estadistica_jugador:
                    print("{}: {}".format(estadistica, estadistica_jugador[estadistica]))

                flag_segundo_punto = True

            case 3:
                if flag_segundo_punto == True:
                    guardar_estadisticas_csv(lista_jugadores, indice_elegido)
                    print("Archivo guardado!!")
                else:
                    print("No podes guardar un archivo con las estadisticas de un jugador, ya que no elegiste uno. Debes pasar por el punto 2")

            case "4":
                nombre_jugador = input("Ingrese el nombre del jugador cuyos logros quiere ver\n")

                lista_indice_nombres_elegidos = validacion_nombre(lista_jugadores, nombre_jugador) 

                lista_indice_nombres_elegidos = validar_dato_ingresado(lista_jugadores, lista_indice_nombres_elegidos)

                imprimir_logros_jugador(lista_jugadores, lista_indice_nombres_elegidos)

            case "5":
                print("El promedio de puntos por partido de todo el Dream Team junto es: {} puntos".format(promedio_equipo_por_llave(lista_jugadores, "promedio_puntos_por_partido")))
                print("Los jugadores ordenados alfabeticamente de forma ascendente, indicando su promedio puntos por partido")

                for jugador in quicksort(lista_jugadores, flag_asc=True, llave="nombre"):
                    print("- {} - {}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"]))

            case "6":
                nombre_jugador = input("Ingrese el nombre del jugador\n")

                lista_indice_nombres_elegidos = validacion_nombre(lista_jugadores, nombre_jugador)

                lista_indice_nombres_elegidos = validar_dato_ingresado(lista_jugadores, lista_indice_nombres_elegidos)

                imprimir_logros_jugador(lista_jugadores, lista_indice_nombres_elegidos, salon_de_la_fama=True)

            case "7":
                print("El jugador con mayor cantidad de rebotes es {} rebotes".format(calcular_max(lista_jugadores, llave="rebotes_totales")))

            case "8":
                print("El jugador con mayor porcentaje de tiros de campo es {} %".format(calcular_max(lista_jugadores, llave="porcentaje_tiros_de_campo")))

            case "9":
                print("El jugador con la mayor cantidad de asistencias totales es {} asistencias".format(calcular_max(lista_jugadores, llave="asistencias_totales")))

            case "10":
                lista_indices_mayores = ingresar_y_validar_valor(lista_jugadores, llave="promedio_puntos_por_partido")

                imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores, info="puntos por partido")

            case "11":
                lista_indices_mayores = ingresar_y_validar_valor(lista_jugadores, llave="promedio_rebotes_por_partido")
            
                imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores, info="rebotes por partido")

            case "12":
                lista_indices_mayores = ingresar_y_validar_valor(lista_jugadores, llave="promedio_asistencias_por_partido")

                imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores, info="asistencias por partido")

            case "13":
                print("El jugador con mayor cantidad de robos totales es {} robos".format(calcular_max(lista_jugadores, llave="robos_totales")))

            case "14":
                print("El jugador con mayor cantidad de bloqueos totales es {} bloqueos".format(calcular_max(lista_jugadores, llave="bloqueos_totales")))

            case "15":
                lista_indices_mayores = ingresar_y_validar_valor(lista_jugadores, llave="porcentaje_tiros_libres")
            
                imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores, info="porcentaje de tiros libres")

            case "16":
                print("El promedio de puntos por partido de todo el Dream Team excluyendo al jugador con la menor cantidad de puntos por partido es de {} puntos"
                    .format(promedio_equipo_por_llave(lista_jugadores, "promedio_puntos_por_partido", excluir_menor=True)))

            case "17":
                dict_jugador = jugador_mas_logros(lista_jugadores)

                print("El jugador con mas logros es {}, con los siguientes:".format(dict_jugador["nombre"]))
                for logro in dict_jugador["logros"]:
                    print(logro)

            case "18":
                lista_indices_mayores = ingresar_y_validar_valor(lista_jugadores, llave="porcentaje_tiros_triples")
            
                imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores, info="porcentaje de tiros triples")

            case "19":
                print("El jugador con mayor cantidad de temporadas jugadas es {} temporadas".format(calcular_max(lista_jugadores, llave="temporadas")))

            case "20":
                lista_indices_mayores = ingresar_y_validar_valor(lista_jugadores, llave="porcentaje_tiros_de_campo")            

                imprimir_nombre_jugador_por_indice(lista_jugadores, lista_indices_mayores, info="porcentaje de tiros de campo", flag_posicion=True)

            case "0":
                break

        input("\nPresione enter para continuar\n")


correr_programa()