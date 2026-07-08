lista_canciones = []


def mostar_menu():
    print("======MENU PRINCIPAL======")
    print("1. Agregar cancion")
    print("2. Buscar cancion")
    print("3. Eliminar cancion")
    print("4. Actualizar estados")
    print("5. Mostrar canciones")
    print("6. Salir")
    print("==========================")

def pedir_opcion():
    while True:
        opcion = input("Elige una opcion 1 - 6: ")
        try:
            opcion_numero = int(opcion)
            if 1<= opcion_numero <= 6:
                return opcion_numero
        except ValueError:
            print("Opcion invalida debe ser un numero entero")
            continue
        print("Opcion invalida debe estar entre el 1 y el 6")    
          


