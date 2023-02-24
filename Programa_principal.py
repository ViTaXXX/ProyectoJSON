import json
from Funciones import *


with open("Inventario.json") as f:
        inventario = json.load(f)

opcion = 0

while opcion != 6:
        print("")
        print("Menu de consultas de objetos:")
        print("1. Listar todos los objetos del inventario.")
        print("2. Contar todos los objetos del inventario.")
        print("3. Filtrar los objetos mostrando solamente los que tengan poder divino.")
        print("4. Mostrar los tipos de ataque de un objeto específico.")
        print("5. Calcular el poder máximo de un objeto.")
        print("6. Salir.")
        print("")

        opcion = int(input("Introduzca una opción(1-6): "))

        if opcion == 1:
            listar_objetos(inventario)
        elif opcion == 2:
            contar_objetos(inventario)
        elif opcion == 3:
            filtrar_objetos(inventario)
        elif opcion == 4:
            buscar_info_objeto(inventario)
        elif opcion == 5:
            calcular_poder_max(inventario)
        elif opcion == 6:
            print("Hasta luego.")
        else:
            print("Error: opción inválida. (1-6)")
