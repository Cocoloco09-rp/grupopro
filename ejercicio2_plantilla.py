# SECCIÓN A: clasificación y visualización

def clasificar_existencia(cantidad):
    # TODO A1: retornar la clasificación correspondiente.
    return "Clasificación pendiente"


def mostrar_inventario(existencias):
    print("\n--- INVENTARIO ---")

    # TODO A2:
    # Mostrar número de producto, cantidad y clasificación.

    print(existencias)


# SECCIÓN B: validación de entradas

def pedir_entero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: debes escribir un número entero.")
            continue

        if minimo <= valor <= maximo:
            return valor

        print(f"Error: el valor debe estar entre {minimo} y {maximo}.")


# SECCIÓN C: operaciones de inventario

def retirar_unidades(disponible, cantidad):
    # TODO C1:
    # Si no hay unidades suficientes, informar y retornar disponible.
    # Si hay suficientes, retornar disponible - cantidad.
    return disponible


def reponer_unidades(disponible, cantidad):
    # TODO C2: retornar disponible + cantidad.
    return disponible


# SECCIÓN D: programa principal

existencias = [8, 0, 4]

while True:
    # TODO D1: mostrar el menú de opciones.

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            mostrar_inventario(existencias)

        case "2" | "3":
            numero_producto = pedir_entero_en_rango(
                f"Número de producto (1 a {len(existencias)}): ",
                1,
                len(existencias)
            )

            cantidad = pedir_entero_en_rango(
                "Cantidad de unidades (1 a 20): ",
                1,
                20
            )

            indice = numero_producto - 1

            if opcion == "2":
                existencias[indice] = retirar_unidades(
                    existencias[indice],
                    cantidad
                )
            else:
                existencias[indice] = reponer_unidades(
                    existencias[indice],
                    cantidad
                )

            print(f"Existencia actual: {existencias[indice]}")

        case "4":
            print("Programa finalizado.")
            break

        case _:
            print("Error: selecciona una opción entre 1 y 4.")