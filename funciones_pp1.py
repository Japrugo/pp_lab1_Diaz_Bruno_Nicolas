import json
import re

def leer_archivo(nombre_archivo:str):
    """
    - Abre en modo lectura el archivo dado
    - Recibe un string
    - Retorna la lista
    """
    lista = []

    with open(nombre_archivo, "r", encoding="utf8") as archivo:
    
        return json.load(archivo)["jugadores"] 

lista_jugadores = leer_archivo("dreamteam.json")


def validar_menu(numero:int) -> bool:
    """
    - Esta función busca validar el numero ingresado para que sea apto para el menú.(1-20,23)
    - Un numero que se evaluará la validación.
    - True en caso que haya coincidido el re.match , False en caso que no haya coincidido.
    """
    coincidencia = re.match(r'^1?\d{1}$|20|23', numero)
    if coincidencia:
        return True
    else:
        return False
    

def validar_numero(dato:str):
    """
    - Valida si el dato pasado es numerico, y si lo es lo convierte a int o a float.
    - Recibe un str. 
    - Retorna un int o float en caso de ser numerico, si no lo es retorna False.
    """
    if re.match( r"^\d+(\.\d+)?$", dato):
        try:    
            return int(dato)
        except Exception as error:
            return float(dato)
    else: 
        return False


def validacion_nombre(lista_de_jugadores_original:list, nombre_jugador:str) -> list:
    """
    - Valida si el nombre del jugador ingresado existe.
    - Recibe el nombre del jugador ingresado y la lista de jugadores.
    - Retorna la lista de indices del/los jugadores elegidos o False si no existe.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    lista_indice_nombres_elegidos = []
    for jugador in lista_de_jugadores:
        coincidencia_nombre_jugador = re.match("{}+".format(nombre_jugador.lower()), jugador["nombre"].lower())
        if coincidencia_nombre_jugador:
            lista_indice_nombres_elegidos.append(lista_de_jugadores.index(jugador))
    
    if len(lista_indice_nombres_elegidos) > 0:
        return lista_indice_nombres_elegidos
    else:
        return False
    

def validar_dato_ingresado(lista_de_jugadores_original:list, valor_ingresado):
    """
    - Valida si el valor ingresado no sea incorrecto, si lo es, pregunta para ingresar otro.
    - Recibe la lista de jugadores y un valor.
    - Retorna ese valor.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    if type(valor_ingresado) == type(int()) or type(valor_ingresado) == type(float()) or type(valor_ingresado) == type(str()):
        valor_ingresado = validar_numero(valor_ingresado)

        while valor_ingresado == False:
            valor_ingresado = input("Valor invalido. Ingrese otro valor\n")
            valor_ingresado = validar_numero(valor_ingresado)
    
    elif type(valor_ingresado) == type(bool()):
        while valor_ingresado == False:
            valor_ingresado = input("Nombre inexistente. Ingrese el nombre del jugador cuyos logros quiere ver\n")
            valor_ingresado = validacion_nombre(lista_de_jugadores, nombre_jugador = valor_ingresado)
    
    return valor_ingresado


def ingresar_y_validar_valor(lista_de_jugadores_original:list, llave:str):
    """
    - Pide ingresar un valor, lo valida y calcula los mayores a ese valor ingresado.
    - Recibe la lista de jugadores y una llave(str).
    - Retorna la lista de los mayores al valor dado.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    valor_ingresado = input("Ingrese un valor\n")

    valor_ingresado = validar_dato_ingresado(lista_de_jugadores, valor_ingresado) 

    return mayor_al_valor_ingresado(lista_de_jugadores, llave, valor_ingresado)


def mostrar_jugadores(lista_de_jugadores_original:list):
    """
    - Muestra la lista de jugadores del Dream Team.
    - Recibe la lista de jugadores.
    - No retorna nada.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]
    cont = 1

    for jugador in lista_de_jugadores:
        print("{} - {} - {}".format(cont, jugador["nombre"], jugador["posicion"]))
        cont += 1   
    
def estadisticas_completas_jugador(lista_de_jugadores_original:list, indice:int) -> dict:
    """
    - Muestra las estadisticas completas de un jugador dado.
    - Recibe la lista de jugadores y un int que es un indice de la lista.
    - Retorna un dict.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    return lista_de_jugadores[indice]["estadisticas"] 

def guardar_estadisticas_csv(lista_de_jugadores_original:list, indice:int):
    """
    - Guarda en un CSV las estadisticas del jugador seleccionado en el punto 2.
    - Recibe la lista de jugadores y el indice elegido anteriormente.
    - No retorna nada.
    """
    
    lista_de_jugadores = lista_de_jugadores_original[:]

    with open(lista_de_jugadores[indice]["nombre"] + ".csv", "w") as archivo:
        for estadistica in lista_de_jugadores[indice]["estadisticas"]:         
            archivo.write("{},".format(estadistica))

        archivo.write("\n")  

        for estadistica in lista_de_jugadores[indice]["estadisticas"]: 
            archivo.write("{},".format(lista_de_jugadores[indice]["estadisticas"][estadistica]))  
            
def listar_logros_jugador(lista_de_jugadores_original:list, indice_jugador:int) -> list:
    """
    - Devuelve la lista de los logros de un jugador especificado por indice.
    - Recibe la lista de jugadores y un int con el indice de uno de ellos.
    - Retorna la lista de logros de dicho jugador.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    return lista_de_jugadores[indice_jugador]["logros"]
    

def imprimir_logros_jugador(lista_de_jugadores_original:list, lista_indice_nombres_elegidos:list, salon_de_la_fama:bool=False):
    """
    - Imprime los logros de los jugadores por nombre dado, o indica si estan en el salon de la fama.
    - Recibe la lista de jugadores, la lista de indices de nombres elegidos y un bool indicando si se quiere saber si ingreso al salon de la fama o no.
    - No retorna nada.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    for indice_jugador in lista_indice_nombres_elegidos:
        lista_logros_del_jugador = listar_logros_jugador(lista_de_jugadores, indice_jugador)
        
        if salon_de_la_fama == False:
            print("- Logros de {}:".format(lista_de_jugadores[indice_jugador]["nombre"]))

            for logro in lista_logros_del_jugador:
                print("{}".format(logro))
        else:
            if "Miembro del Salon de la Fama del Baloncesto" in lista_logros_del_jugador:
                print("{} es miembro del salon de la fama".format(lista_de_jugadores[indice_jugador]["nombre"]))



def promedio_equipo_por_llave(lista_de_jugadores_original:list, llave:str, excluir_menor:bool=False) -> int: 
    """
    - Se encarga de hallar el promedio del equipo de la llave dada.
    - Recibe una lista de jugadores y una llave del dict estadisticas.
    - Retorna el promedio (int).
    """
    lista_de_jugadores = lista_de_jugadores_original[:]
    acumulador = 0
    contador = 0

    if excluir_menor == True:
        lista_de_jugadores.pop(calcular_min(lista_de_jugadores, llave)) # pop() toma como parametro un indice para luego borrarlo de la lista
    
    for jugador in lista_de_jugadores:
        if type(jugador["estadisticas"][llave]) == type(int()) or type(jugador["estadisticas"][llave]) == type(float()):
            acumulador += jugador["estadisticas"][llave]
            contador += 1
            
    return acumulador / contador


def quicksort(lista_de_jugadores_original:list, flag_asc:bool, llave:str, llave_estadisticas:str = None) -> list:
    """
    - Se encarga de ordenar de manera ascendente o descendente los elementos dados. 
    - Recibe una lista de jugadores, una flag indicando si es asc o desc, una llave del dict de la lista y 
      una llave del dict 'estadisticas' en caso de ser necesaria.
    - Retorna la lista ordenada.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]
    mayores_pivot = []
    menores_pivot = []

    if len(lista_de_jugadores) <= 1:
        return lista_de_jugadores
    else:
        pivot = lista_de_jugadores[0]
        for jugador in lista_de_jugadores[1:]:
            if flag_asc == True:
                if llave.lower() == "estadisticas":  # Esta modificacion esta hecha para el 23
                    if jugador[llave][llave_estadisticas] > pivot[llave][llave_estadisticas]:
                        mayores_pivot.append(jugador)
                    else:
                        menores_pivot.append(jugador)
                else: 
                    if jugador[llave] > pivot[llave]:
                        mayores_pivot.append(jugador)
                    else:
                        menores_pivot.append(jugador)
            elif flag_asc == False:
                if llave.lower() == "estadisticas":  # Esta modificacion esta hecha para el 23
                    if jugador[llave][llave_estadisticas] < pivot[llave][llave_estadisticas]:
                        mayores_pivot.append(jugador)
                    else:
                        menores_pivot.append(jugador)
                else: 
                    if jugador[llave] < pivot[llave]:
                        mayores_pivot.append(jugador)
                    else:
                        menores_pivot.append(jugador)

    menores_pivot = quicksort(menores_pivot, flag_asc, llave, llave_estadisticas)
    menores_pivot.append(pivot)

    mayores_pivot = quicksort(mayores_pivot, flag_asc, llave, llave_estadisticas)
    menores_pivot.extend(mayores_pivot)

    return menores_pivot


def calcular_min(lista_de_jugadores_original:list, llave:str) -> int:
    """
    - Calcula cual es el minimo de la llave dada.
    - Recibe la lista de heroes y una llave del dict.
    - Retorna el indice del minimo.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    for indice in range(len(lista_de_jugadores)):
        if indice == 0 or float(lista_de_jugadores[minimo_indice]["estadisticas"][llave]) > float(lista_de_jugadores[indice]["estadisticas"][llave]):
            minimo_indice = indice

    return minimo_indice


def calcular_max(lista_de_jugadores_original:list, llave:str) -> str:
    """
    - Calcula cual es el maximo de la llave dada.
    - Recibe la lista de heroes y una llave del dict.
    - Retorna el nombre del maximo.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    for indice in range(len(lista_de_jugadores)):
        if indice == 0 or float(lista_de_jugadores[maximo_indice]["estadisticas"][llave]) < float(lista_de_jugadores[indice]["estadisticas"][llave]):
            maximo_indice = indice

    return "{} - {}".format(lista_de_jugadores[maximo_indice]["nombre"], lista_de_jugadores[maximo_indice]["estadisticas"][llave])
    
def mayor_al_valor_ingresado(lista_de_jugadores_original:list, llave:str, valor_ingresado:int) -> list:
    """
    - Busca en la lista dada, si el valor ingresado es mayor o menor a la llave dada.
    - Recibe una lista de jugadores, una llave del dict 'estadisticas' y un valor ingresado(int).
    - Retorna una lista con los indices de los jugadores mayores al valor ingresado.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]
    indices_mayores_pivot = []

    pivot = valor_ingresado
    for jugador in lista_de_jugadores:
        if jugador["estadisticas"][llave] > pivot:
            indices_mayores_pivot.append(lista_de_jugadores.index(jugador))

    return indices_mayores_pivot
    

def imprimir_nombre_jugador_por_indice(lista_de_jugadores_original:list, lista_indices:list, info:str, flag_posicion:bool=False):
    """
    - Imprime los nombres de los jugadores segun la lista de indice/s pasado/s.
    - Recibe la lista de jugadores, una lista de indices, un str que hace referencia a lo que se calculo anteriormente y 
      un bool que indica si se toma la posicion en la cancha o no.
    - No retorna nada.
    """
    lista_de_jugadores = lista_de_jugadores_original[:]
    lista_jugadores_mayores_a_valor = []

    if len(lista_indices) == 0:
        print("No hay ningun jugador que promedie mas {}".format(info))
    else:
        if "porcentaje" in info and flag_posicion == False:
            print("Los jugadores con un mayor {} que el valor ingresado son:".format(info))
            for indice in lista_indices:
                print("- " + lista_de_jugadores[indice]["nombre"])

        elif flag_posicion == True:
            print("Los jugadores con un mayor {} que el valor ingresado son:".format(info))

            for indice in lista_indices:
                lista_jugadores_mayores_a_valor.append(lista_de_jugadores[indice]) # Agregamos a una nueva lista, los jugadores que sean mayores al valor ingresado.

            for indice in range(len(lista_jugadores_mayores_a_valor)):  # Ordena los mayores al valor por posicion.  
                lista_ordenada_por_posicion = quicksort(lista_jugadores_mayores_a_valor, flag_asc=True, llave="posicion")

                print("- {} - {}".format(lista_ordenada_por_posicion[indice]["nombre"],
                                         lista_ordenada_por_posicion[indice]["posicion"]))
        else:
            print("Los jugadores que han promediado mas {} que el valor ingresado son:".format(info))
            for indice in lista_indices:
                print("- " + lista_de_jugadores[indice]["nombre"])



def jugador_mas_logros(lista_de_jugadores_original:list) -> dict:
    """
    - Calcula el jugador con mas logros en su carrera.
    - Recibe la lista de jugadores.
    - Retorna el jugador con mas logros obtenidos(dict).
    """
    lista_de_jugadores = lista_de_jugadores_original[:]

    acumulador_logros = 0
    logros_jugadores = []
    logros_jugadores_sin_indices = []

    for jugador in lista_de_jugadores:
        for logro in jugador["logros"]:
            patron_cuatro_digitos = r"\d{4}"
            if re.search(patron_cuatro_digitos, logro): # Si hay un año en el logro entra.
                acumulador_logros += len(re.findall(patron_cuatro_digitos, logro)) # Busca esos años, y el len va a indicar cuantos son y se suman al acumulador.
            elif "Miembro" in logro:
                acumulador_logros += 1
            else:
                patron = r"\d{1,3}"
                if re.match(patron, logro): # Si el logro empieza con un 1 o 2 digitos entra.
                    acumulador_logros += int(re.findall(patron, logro)[0]) # Trae el numero de cada logro, lo parsea y lo suma al acumulador.
        
        logros_jugadores.append(lista_de_jugadores.index(jugador)) # Agrego el indice del jugador de la lista real.
        logros_jugadores.append(acumulador_logros) # Agrego la cantidad de logros que tenga ese jugadoor. 
        logros_jugadores_sin_indices.append(acumulador_logros) # Lista aparte solo con logros.

        acumulador_logros = 0

    for indice in range(len(logros_jugadores_sin_indices)): # Recorro segun el largo de la lista de solo logros.
        if indice == 0 or float(logros_jugadores_sin_indices[maximo_indice]) < float(logros_jugadores_sin_indices[indice]):
            maximo_indice = indice
            numero_maximo = logros_jugadores_sin_indices[maximo_indice]

    indice_jugador_mas_logros = logros_jugadores[logros_jugadores.index(numero_maximo) - 1] # Dentro del [] obtiene el indice anterior del numero_maximo, 
                                                                                            # que seria el indice del jugador en la lista original. Al ser Jordan da 0.
                                # Y logros_jugadores[x] te da la posicion real del json, del jugador con mas logros.
    return lista_de_jugadores[indice_jugador_mas_logros]
