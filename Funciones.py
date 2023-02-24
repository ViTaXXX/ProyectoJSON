import json

def leer_json(nombre_archivo):
    with open(nombre_archivo) as archivo:
        datos = json.load(archivo)
    return datos

def listar_objetos(inventario):
    for objeto in inventario:
        print(objeto['name'])

def contar_objetos(inventario):
    print(f"Hay {len(inventario)} objetos en el inventario.")

def filtrar_objetos(inventario):
    objetos_poder_divino = []
    for objeto in inventario:
        if objeto['effects']['divine'] is not None:
            objetos_poder_divino.append(objeto['name'])
    print("Los objetos con poder divino son:")
    print("")
    for objeto in objetos_poder_divino:
        print(objeto)

    

def buscar_info_objeto(inventario):
    nombre_objeto = input("Ingresa el nombre del objeto: ")
    print("")
    for objeto in inventario:
        if objeto['name'].lower() == nombre_objeto.lower():
            print(f"Los tipos de ataque de {nombre_objeto} son:")
            print("")
            for tipo_ataque in objeto['attackTypes']:
                print(tipo_ataque)

def calcular_poder_max(inventario):
    nombre_objeto = input("Ingresa el nombre del objeto: ")
    for objeto in inventario:
        if objeto['name'].lower() == nombre_objeto.lower():
            ataque_fisico = objeto['atk']['physical']
            ataque_magico = objeto['atk']['magic']
            ataque_luz = objeto['atk']['lightning']
            ataque_fuego = objeto['atk']['fire']
            suma_ataque_fisico_magico = ataque_fisico + ataque_magico
            print(f"El objeto {nombre_objeto} tiene:")
            print(f"Ataque físico: {ataque_fisico}")
            print(f"Ataque mágico: {ataque_magico}")
            print(f"Ataque de luz: {ataque_luz}")
            print(f"Ataque de fuego: {ataque_fuego}")
            print(f"La suma de ataque físico y mágico es: {suma_ataque_fisico_magico}")

