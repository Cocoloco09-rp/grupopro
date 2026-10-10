def calcular_subtotal(total_paginas, precio_pagina):
    # TODO 1: retornar el subtotal correcto.
    return 0


paquetes = ["Apuntes", "Guía de ejercicios", "Material de consulta"]

PRECIO_PAGINA = 2
PORCENTAJE_DESCUENTO = 0.10

total_paginas = 0
cantidad_paquetes_aceptados = 0

for indice in range(len(paquetes)):
    # TODO : Imprimir el nombre del paquete actual.

    try:
        paginas = int(input("Cantidad de páginas (1 a 50): "))
    except ValueError:
        print("Error: debes escribir un número entero. Paquete omitido.")
        continue

    # TODO 2:
    # Si paginas está fuera del rango 1 a 50,
    # mostrar un mensaje y omitir este paquete con continue.

    # TODO 3:
    # Acumular las páginas y aumentar los paquetes aceptados.


subtotal = calcular_subtotal(total_paginas, PRECIO_PAGINA)
descuento = 0

# TODO 4:
# Aplicar 10% de descuento solo si total_paginas supera 100.


print("\n--- RESUMEN DEL PEDIDO ---")
"""
 TODO 5: Mostrar un mensaje si no se aceptó ningún paquete. 
 E imprimir el resumen del pedido con la cantidad de paquetes aceptados, 
 total de páginas, subtotal, descuento y total a pagar.
"""