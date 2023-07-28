from pymongo import MongoClient
def get_database():

   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://127.0.0.1:27017"

   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)

   # Create the database for our example (we will use the same database throughout the tutorial
   return client['mongoBD']

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

   # Get the database
   mongobd = get_database()

# 1) Creacion de estructuras e inserts:

mongobd.drop_collection('final')

mongobd.create_collection('final')

final = mongobd["final"]


final.insert_one({
  "nombre": 'Carlos',
  "apellido": 'Santana',
  "modo": 'Solista',
  "ciudad": 'Los Ángeles',
  "país": 'USA',
  "habilidades": [{ "descripción": 'guitarrista', "tipo": 'rockero', "nivel": 'superlativo' }]
})

final.insert_one({
  "nombre": 'David',
  "apellido": 'Lebon',
  "modo": 'Parte de un grupo',
  "habilidades": [{"descripción": 'bajista', "tipo": 'blusero', "nivel": 'muy bueno'}]
})

final.insert_one({
  "nombre": 'Juana',
  "apellido": 'Molina',
  "modo": 'Banda propia',
  "ciudad": 'Montevideo',
  "país": 'Uruguay',
  "habilidades": [{"descripción": 'voz', "nivel": 'superlativa'}]
})

final.insert_one({
  "nombre": 'Angus',
  "apellido": 'Young',
  "ciudad": 'Glasgow',
  "país": 'Escocia',
  "modo": 'Showman',
  "habilidades": [{"descripción": 'guitarrista', "nivel": 'increíble'}]
})

final.insert_one({
  "nombre": 'Ghost',
  "ciudad": 'Linköping',
  "país": 'Suecia',
  "modo": 'Banda',
  "habilidades": [{"descripción": 'show', "nivel": 'Increíble'}],
  "inicio": 2006
})

final.insert_one({
  "nombre": 'Rammstein',
  "ciudad": 'Berlin',
  "país": 'Alemania',
  "musicos": ['Christoph Schneider', 'Oliver Riedel'],
  "inicio": 1990,
  "modo": 'Banda'
})


# Querys

#1. Obtener todos los documentos
def query1():
   documentos = final.find()
   for i in documentos:
      print(i)

#2. Obtener documentos con habilidad guitarrista.

def query2():
   documentos = final.find({"habilidades.descripción":'guitarrista'})
   for i in documentos:
      print(i)

#3. Obtener documentos con habilidad blusero

def query3():
   documentos = final.find({"habilidades.tipo":'blusero'})
   for i in documentos:
      print(i)

#4. Obtener los discos entre el año 2000 y 2010.

def query4():
   discos = final.find({"discos.año":{"$gte":2000, "$lte":2010}},{"_id":0,"discos.nombre.$":1})
   for i in discos:
      print(i['discos'][0]['nombre'])

# 2) Actualizar Documentos:

def update1():
   # 1. Agregar habilidades a un músico.
   final.update_one(
      {"nombre": "David", "apellido": "Lebon"},
      {"$push": {"habilidades": {"descripción": "voz", "nivel": "superlativa"}}}
   )

def update2():
   # 2. Agregar una ciudad a un músico.
   final.update_one(
      {"nombre": "David", "apellido": "Lebon"},
      {"$set": {"ciudad": "Buenos Aires"}}
   )

def update3():
   # 3. Agregar los discos a una banda.
   final.update_one(
      {"nombre": "Rammstein"},
      {"$set": {"discos": [{"nombre": "Mutter", "año": 2001}, {"nombre": "Sehnsucht", "año": 1997}]}}
   )

def update4():
   # 4. Agregar los músicos a una banda.
   final.update_one(
      {"nombre": "Rammstein"},
      {"$push": {"musicos": "Christian Lorenz"}}
   )

def update5():
   # 5. Cambiar el país de nacimiento de un intérprete.
   final.update_one(
      {"nombre": "David", "apellido": "Lebon"},
      {"$set": {"país": "Argentina"}}
   )

def update6():
   # 6. Eliminar el disco de una banda.
   final.update_one(
      {"nombre": "Rammstein"},
      {"$pull": {"discos": {"nombre": "Sehnsucht"}}}
   )

def update7():
   # 7. Cambiar el nivel de una habilidad.
   final.update_one(
      {"nombre": "David", "apellido": "Lebon", "habilidades.descripción": "bajista"},
      {"$set": {"habilidades.$.nivel": "increíble"}}
   )

def update8():
   # 8. Agregar comentarios a una banda (podrían ser más de uno).
   final.update_one(
      {"nombre": "Rammstein"},
      {"$push": {"comentarios": "Son unos Cracks"}}
   )

update1()
update2()
update3()
update4()
update5()
update6()
update7()
update8()
