import pymongo
import os
import time

# Funciones
def insertar(documento, coleccion):
    collection = db[coleccion]
    sentencia = collection.insert_one(documento)
    if sentencia.acknowledged:
        print(f"El documento 'id:{sentencia.inserted_id}' se inserto correctamente.")
    else:
        print(f"El documento 'id:{sentencia.inserted_id}' no se pudo insertar.")


# Actualización 1
def actualizacion_1(collection):
    nombre_musico = input("Ingrese el nombre del músico: ")
    apellido_musico = input("Ingrese el apellido del músico: ")

    descripcion = input("Ingrese la descripción de la habilidad: ")
    tipo = input("Ingrese el tipo de habilidad: ")
    nivel = input("Ingrese el nivel de habilidad: ")

    habilidad = {"descripción": descripcion, "tipo": tipo, "nivel": nivel}

    collection.update_one({"nombre": nombre_musico, "apellido": apellido_musico},
                          {"$addToSet": {"habilidades": habilidad}})

# Actualización 2
def actualizacion_2(collection):
    nombre_musico = input("Ingrese el nombre del músico: ")
    apellido_musico = input("Ingrese el apellido del músico: ")
    ciudad = input("Ingrese el nombre de la ciudad que desea agregar: ")

    collection.update_one({"nombre": nombre_musico, "apellido": apellido_musico},
                            {"$set": {"ciudad": ciudad}})

# Actualización 3
def actualizcion_3(collection):
    nombre_banda = input("Ingrese el nombre de la banda: ")
    nombre_disco = input("Ingrese el nombre del disco: ")
    año_disco = int(input("Ingrese el año del disco: "))
    disco = {"nombre": nombre_disco, "año": año_disco}

    collection.update_one({"nombre": nombre_banda},
                          {"$addToSet": {"discos": disco}})

# Actualización 4
def actualizacion_4(collection):
    nombre_banda = input("Ingrese el nombre de la banda: ")
    nombre_musico = input("Ingrese el nombre del músico: ")

    musico = {"nombre": nombre_musico}

    collection.update_one({"nombre": nombre_banda},
                          {"$addToSet": {"musicos": musico}})
    

# Actualización 5
def actualizacion_5(collection):
    nombre_musico = input("Ingrese el nombre del músico: ")
    apellido_musico = input("Ingrese el apellido del músico: ")
    pais = input("Ingrese el nombre del país que reemplazará al anterior: ")

    collection.update_one({"nombre": nombre_musico, "apellido": apellido_musico},
                          {"$set": {"país": pais}})

# Actualización 6
def actualizacion_6(collection):
    nombre_banda = input("Ingrese el nombre de la banda: ")
    nombre_disco = input("Ingrese el nombre del disco: ")

    collection.update_one({"nombre": nombre_banda},
                          {"$pull": {"discos": {"nombre": nombre_disco}}})

# Actualización 7
def actualizacion_7(collection):
    nombre_musico = input("Ingrese el nombre del músico: ")
    apellido_musico = input("Ingrese el apellido del músico: ")
    descripcion = input("Ingrese la descripción de la habilidad: ")
    nivel = input("Ingrese el nuevo nivel de habilidad: ")

    collection.update_one({"nombre": nombre_musico, "apellido": apellido_musico, "habilidades.descripción": descripcion},
                          {"$set": {"habilidades.$.nivel": nivel}})

# Actualización 8
def actualizacion_8(collection):
    nombre_banda = input("Ingrese el nombre de la banda: ")

    comentarios_nuevos = []
    while True:
        comentario = input("Ingrese el comentario (o escriba 'salir' para terminar): ")
        if comentario.lower() == "salir":
            break
        else:
            comentarios_nuevos.append(comentario)

    if comentarios_nuevos:
        collection.update_one({"nombre": nombre_banda},
                              {"$addToSet": {"comentarios": {"$each": comentarios_nuevos}}})


# Consulta 1
def query_1(collection):
    for documento in collection.find():
        print(documento)

# Consulta 2
def query_2(collection):
    for documento in collection.find({"habilidades.descripción": "guitarrista"}):
        print(documento)

# Consulta 3
def query_3(collection):
    for documento in collection.find({"habilidades.tipo": "blusero"}):
        print(documento)

# Consulta 4
def query_4(collection):
    for documento in collection.find({"discos.año": {"$gte": 2000, "$lte": 2010}}):
        nombre_banda = documento.get("nombre")
        discos = documento.get("discos", [])

        for disco in discos:
            nombre_disco = disco.get("nombre")
            print(f"Banda: {nombre_banda}, Disco: {nombre_disco}")

# Eliminación 1
def eliminacion_1_solista(collection):
    nombre_musico = input("Ingrese el nombre del músico solista: ")
    apellido_musico = input("Ingrese el apellido del músico solista: ")
    nombre_disco = input("Ingrese el nombre del disco a eliminar: ")

    collection.update_one(
        {"nombre": nombre_musico, "apellido": apellido_musico},
        {"$pull": {"discos": {"nombre": nombre_disco}}}
    )

def eliminacion_1_banda(collection):
    nombre_banda = input("Ingrese el nombre de la banda: ")
    nombre_disco = input("Ingrese el nombre del disco a eliminar: ")

    collection.update_one(
        {"nombre": nombre_banda},
        {"$pull": {"discos": {"nombre": nombre_disco}}}
    )

# Eliminación 2
def eliminacion_2(collection):
    collection.delete_many({"modo": "Banda"})


# Establecer la conexión a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["final"]
collection = db["musicos"]

documento1 = {
    "nombre": "Carlos",
    "apellido": "Santana",
    "modo": "Solista",
    "ciudad": "Los Angeles",
    "país": "USA",
    "habilidades": [
        {
            "descripción": "guitarrista",
            "tipo": "rockero",
            "nivel": "superlativo"
        }
    ]
}
documento2 = {
    "nombre": "David",
    "apellido": "Lebon",
    "modo": "Solista",
    "habilidades": [
        {
            "descripción": "bajista",
            "tipo": "blusero",
            "nivel": "muy bueno"
        }
    ]
}
documento3 = {
    "nombre": "Juana",
    "apellido": "Molina",
    "modo": "Solista",
    "ciudad": "Montevideo",
    "país": "Uruguay"
}
documento4 = {
    "nombre": "Angus",
    "apellido": "Young",
    "modo": "Solista",
    "ciudad": "Glasgow",
    "país": "Escocia",
    "habilidades": [
        {
            "descripción": "guitarrista",
            "nivel": "increible"
        }
    ]
}
documento5 = {
    "nombre": "Ghost",
    "modo": "Banda",
    "ciudad": "Linköping",
    "país": "Suecia",
    "habilidades": [{"nombre": "Frontman"}],
    "inicio": 2006
}
documento6 = {
    "nombre": "Rammstein",
    "ciudad": "Berlín",
    "país": "Alemania",
    "modo": "Banda",
    "musicos": [
        {"nombre": "Christoph Schneider"}, {"nombre": "Oliver Riedel"}
    ],
    "inicio": 1990
}


def menu():
    print("-----------------------------------")
    print("Bienvenido al menu de la aplicación")
    print("Opciones: ")
    print("Opción 1: Actualizar documentos")
    print("Opción 2: Realizar consultas")
    print("Opción 3: Eliminar documentos")
    print("-----------------------------------")
    collection = db["musicos"]
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        print("--------------------------------------------------------------")
        print("Elija una actualización a realizar: ")
        print("1. Agregar habilidades a un musico.")
        print("2. Agregar una ciudad a un musico.")
        print("3. Agregar los discos a una banda.")
        print("4. Agregar los músicos a una banda.")
        print("5. Cambiar el país de nacimiento de un intérprete.")
        print("6. Eliminar el disco de una banda.")
        print("7. Cambiar el nivel de una habilidad.")
        print("8. Agregar comentarios a una banda (podrían ser más de uno).")
        print("--------------------------------------------------------------")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            actualizacion_1(collection)
            time.sleep(2)
            menu()
        
        elif opcion == "2":
            actualizacion_2(collection)
            time.sleep(2)
            menu()
        
        elif opcion == "3":
            actualizcion_3(collection)
            time.sleep(2)
            menu()
        
        elif opcion == "4":
            actualizacion_4(collection)
            time.sleep(2)
            menu()
        
        elif opcion == "5":
            actualizacion_5(collection)
            time.sleep(2)
            menu()
        
        elif opcion == "6":
            actualizacion_6(collection)
            time.sleep(2)
            menu()
        
        elif opcion == "7":
            actualizacion_7(collection)
            time.sleep(2)
            menu()
        
        elif opcion == "8":
            actualizacion_8(collection)
            time.sleep(2)
            menu()
    
    elif opcion == "2":
        print("--------------------------------------------------------------")
        print("Elija una consulta a realizar: ")
        print("1. Obtener todos los documentos")
        print("2. Obtener documentos con habilidad guitarrista.")
        print("3. Obtener documentos con habilidad blusero")
        print("4. Obtener los discos entre el año 2000 y 2010.")
        print("--------------------------------------------------------------")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            query_1(collection)
            time.sleep(2)
            menu()
        
        elif opcion == "2":
            query_2(collection)
            time.sleep(2)
            menu()

        elif opcion == "3":
            query_3(collection)
            time.sleep(2)
            menu()
        
        elif opcion == "4":
            query_4(collection)
            time.sleep(2)
            menu()
        
        else:
            print("Opción inválida")
            time.sleep(2)
            menu()

    elif opcion == "3":
        print("--------------------------------------------------------------")
        print("Elija una eliminación a realizar: ")
        print("1. Eliminar el disco Abraxas de Santana")
        print("2. Eliminar a las bandas de la colección")
        print("--------------------------------------------------------------")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            modo = input("Ingrese el modo del musico (solista o banda): ")
            if modo == "solista":
                eliminacion_1_solista(collection)
                time.sleep(2)
                menu()

            elif modo == "banda":
                eliminacion_1_banda(collection)
                time.sleep(2)
                menu()

        elif opcion == "2":
            eliminacion_2(collection)
            time.sleep(2)
            menu()

    else:
        print("Opción inválida")
        time.sleep(2)
        menu()

menu()
