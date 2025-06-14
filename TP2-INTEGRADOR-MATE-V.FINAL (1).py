import datetime  # Para obtener el año actual
import itertools  # Para generar el producto cartesiano


# PARTE 1 – Conjuntos a partir de DNIs
# Para esto, armé una función que recibe los DNIs y genera conjuntos con dígitos únicos.
# Después, muestro por pantalla esos conjuntos.
# También programé las operaciones entre pares de conjuntos:
# - Unión
# - Intersección
# - Diferencia (entre pares)
# - Diferencia simétrica
# Por último, agregué una condición extra:
# “Si todos los conjuntos tienen al menos 5 elementos, mostrar ‘Alta diversidad numérica’”.

def conjuntos_desde_dnis(dnis):
    conjuntos = {}
    for nombre, dni in dnis.items():
        # Genero conjunto con dígitos únicos y ordenados
        conjuntos[nombre] = list(sorted(set(dni)))
    return conjuntos


def operaciones_entre_conjuntos(conjuntos):
    nombres = list(conjuntos.keys())
    n = len(nombres)
    print("\nOperaciones entre pares:\n")
    for i in range(n):
        for j in range(i+1, n):
            a = nombres[i]
            b = nombres[j]
            set_a = set(conjuntos[a])
            set_b = set(conjuntos[b])
            print(f"{a} y {b}")
            # Unión
            print("Unión:", sorted(set_a | set_b))
            # Intersección
            print("Intersección:", sorted(set_a & set_b))
            print(f"Diferencia ({a} - {b}):",
                  # Diferencia
                  sorted(set_a - set_b))
            # Diferencia simétrica
            print("Diferencia simétrica:", sorted(
                set_a ^ set_b))
            print()


def alta_diversidad_numérica(conjuntos):
    # Si todos los conjuntos tienen 5 o más elementos, muestro mensaje
    if all(len(c) >= 5 for c in conjuntos.values()):
        print("Alta diversidad numérica")
    else:
        print("No se cumple la alta diversidad numérica")

# -------------------------------------------------------------------------------------------------------------------------------------#


# PARTE 2 - Análisis de dígitos en los DNIs
# En esta sección, se analiza el contenido de los DNIs de forma numérica.
# Se cuenta la frecuencia de cada dígito, se calcula la suma total de los dígitos
# y se aplican algunas condiciones para obtener resultados adicionales.

def frecuencia_digitos(dnis):
    # Se crea un diccionario para almacenar las frecuencias de cada persona.
    frecuencias = {}

    # Se recorre el conjunto de DNIs, uno por cada persona.
    for nombre, dni in dnis.items():
        freq = {}

        # Se recorren los dígitos del DNI uno por uno.
        for digito in dni:
            # Se cuenta cuántas veces aparece cada dígito.
            # Si el dígito ya está, se suma 1. Si no, se inicia en 1.
            freq[digito] = freq.get(digito, 0) + 1

        # Se guarda la frecuencia en el diccionario principal.
        frecuencias[nombre] = freq

    return frecuencias


def suma_digitos(dnis):
    # Se crea un diccionario para guardar las sumas.
    sumas = {}

    # Se recorren los DNIs.
    for nombre, dni in dnis.items():
        # Se convierten los caracteres a enteros con int().
        # Luego, se suman todos los valores con la función sum().
        sumas[nombre] = sum(int(d) for d in dni)

    return sumas

# En esta parte se aplicaron algunas condiciones para obtener resultados adicionales.


def digito_compartido(conjuntos):
    # Se transforma cada conjunto de dígitos en un set para eliminar repeticiones.
    conjuntos_list = [set(c) for c in conjuntos.values()]

    # Se calcula la intersección de todos los conjuntos (dígitos compartidos).
    interseccion = set.intersection(*conjuntos_list)

    # Se imprime el resultado, dependiendo si hubo coincidencias o no.
    if interseccion:
        print(f"Dígito compartido: {sorted(interseccion)}")
    else:
        print("No hay dígito compartido en todos los conjuntos")


def diversidad_alta(conjuntos):
    # Se utiliza any() para verificar si existe al menos un conjunto con más de 6 elementos.
    # La función len() devuelve la cantidad de elementos en cada conjunto.
    if any(len(c) > 6 for c in conjuntos.values()):
        print("Diversidad numérica alta")
    else:
        print("Diversidad numérica no alta")


def grupo_par_impar(conjuntos):
    # Se calcula cuántos conjuntos tienen cantidad par de elementos.
    # El operador % (módulo) devuelve el resto de una división. Si da 0, es par.
    pares = sum(1 for c in conjuntos.values() if len(c) % 2 == 0)

    # Se calcula la cantidad de conjuntos impares restando al total los pares.
    impares = len(conjuntos) - pares

    # Se imprime un mensaje según cuál grupo sea mayor.
    if pares > impares:
        print("Grupo par")
    elif pares < impares:
        print("Grupo impar")
    else:
        print("Igual cantidad de conjuntos con cantidad par e impar de elementos")

# ------------------------------------------------------------------------------------------------------------------------------------#

# PARTE 3 – Años de nacimiento
# Para esto, se ingresan los años de nacimiento y se cuenta cuántos son pares y cuántos impares.

# Esta función recibe un año como dato de entrada y evalúa si es bisiesto.
# Un año es bisiesto si cumple estas condiciones:
# - Es divisible por 4,
# - No es divisible por 100, salvo que también sea divisible por 400.


def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


# Esta función toma una lista de años y analiza:
# - cuántos son pares e impares,
# - si todos son posteriores al 2000,
# - y si hay algún año bisiesto.
def analizar_anios(anios):
    # Cuenta cuántos años de la lista son pares
    pares = sum(1 for a in anios if a % 2 == 0)

    # El resto es considerado impar
    impares = len(anios) - pares

    # Muestra la cantidad de años pares e impares
    print(f"Números pares: {pares}, Números impares: {impares}")

    # Verifica si todos los años son posteriores al 2000
    # La función all() devuelve True si todos los elementos cumplen la condición
    if all(a > 2000 for a in anios):
        print("Grupo Z")
    else:
        print("No todos nacieron después del 2000")

    # Verifica si alguno de los años es bisiesto
    # La función any() devuelve True si al menos uno cumple la condición
    if any(es_bisiesto(a) for a in anios):
        print("Tenemos un año especial")
    else:
        print("No hay año bisiesto en el grupo")

#Producto Cartesiano

anios = [1993, 1991, 1986, 1987]

analizar_anios(anios)

edades = [2025 - a for a in anios]
print ("Edades calculadas: ", edades)

producto_cartesiano = [(a, e) for a in anios for e in edades]

print ("\nProductos cartesianos: ")
for par in producto_cartesiano:
    print(par)


# ----------------------------------------------------------------------------------------------------------------------------------------#

# PARTE 4 – Producto cartesiano y control general con menú
# Este bloque calcula la edad de cada integrante según su año de nacimiento.

# Esta función recibe una lista de años y calcula la edad actual de cada persona


def calcular_edades(anios):
    anio_actual = datetime.datetime.now().year  # Obtiene el año actual
    # Calcula edad restando el año de nacimiento al actual
    edades = [anio_actual - a for a in anios]
    print(f"Edades calculadas: {edades}")
    return edades

# Esta función recibe una lista de edades y crea un conjunto con valores únicos


def crear_conjunto_edades(edades):
    conjunto = set(edades)  # El conjunto elimina duplicados automáticamente
    print(f"Conjunto de edades únicas: {conjunto}")
    return conjunto

# Esta función recibe las listas de años y edades y muestra todas las combinaciones posibles


def producto_cartesiano(anios, edades):
    print("\nProducto cartesiano (Año de nacimiento, Edad):")
    for par in itertools.product(anios, edades):
        print(par)

# Función para mostrar el menú y controlar la ejecución del programa


def menu_principal():
    anios = [1993, 1991, 1986, 1987]  # Lista fija de años de nacimiento
    while True:
        print("\n--- PARTE 4 ---")
        print("\n--- Menú ---")
        print("1. Calcular edades")
        print("2. Crear conjunto de edades")
        print("3. Mostrar producto cartesiano")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            edades = calcular_edades(anios)

        elif opcion == "2":
            try:
                edades
            except NameError:
                print("Primero debe calcular las edades (opción 1).")
            else:
                crear_conjunto_edades(edades)

        elif opcion == "3":
            try:
                edades
            except NameError:
                print("Primero debe calcular las edades (opción 1).")
            else:
                producto_cartesiano(anios, edades)

        elif opcion == "4":
            print("Saliendo del menú...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecución principal –


if __name__ == "__main__":
    dnis = {
        "Antonela": "37023953",
        "Sandra": "32464594",
        "Yanina": "36162919",
        "Laura": "34507750"
    }
    anios = [1993, 1991, 1986, 1987]

    # Mensaje PARTE 1
    print("\n--- PARTE 1 - Conjuntos a partir de DNIs ---")
    conjuntos = conjuntos_desde_dnis(dnis)
    print("Conjuntos generados (con dígitos únicos y ordenados):")
    for nombre, conjunto in conjuntos.items():
        print(f"{nombre}: {conjunto}")
    operaciones_entre_conjuntos(conjuntos)
    alta_diversidad_numérica(conjuntos)

    # Mensaje PARTE 2
    print("\n--- PARTE 2 - Análisis de dígitos en DNIs ---\n")
    frecuencias = frecuencia_digitos(dnis)
    print("Frecuencia de dígitos en cada DNI:")
    for nombre, freq in frecuencias.items():
        print(f"{nombre}: {freq}")
    sumas = suma_digitos(dnis)
    print("\nSuma total de los dígitos de cada DNI:")
    for nombre, suma in sumas.items():
        print(f"{nombre}: {suma}")

    # Separador visual
    print("\n" + "-"*40 + "\n")

    digito_compartido(conjuntos)
    diversidad_alta(conjuntos)
    grupo_par_impar(conjuntos)

    # Otra línea para separar antes de la siguiente parte
    print("\n" + "="*50 + "\n")

    # Mensaje PARTE 3
    print("\n--- PARTE 3 - Años de nacimiento ---")
    print(f"Años de nacimiento: {anios}")
    analizar_anios(anios)

    # Mensaje PARTE 4
    menu_principal()
