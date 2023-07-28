// Iniciar mongo

sudo systemctl start mongod // correr mongo

mongosh // entrar a consola mongo

show dbs // mostrar dbs

use viajes // usar o crear esa db


// creacion de coleccion:

db.createCollection('final')

// inserts que dió el profe:

db.final.insertOne({
  nombre: 'Carlos',
  apellido: 'Santana',
  modo: 'Solista',
  ciudad: 'Los Ángeles',
  país: 'USA',
  habilidades: [{ descripción: 'guitarrista', tipo: 'rockero', nivel: 'superlativo' }]
});

db.final.insertOne({
  nombre: 'David',
  apellido: 'Lebon',
  modo: 'Parte de un grupo',
  habilidades: [{ descripción: 'bajista', tipo: 'blusero', nivel: 'muy bueno' }]
});

db.final.insertOne({
  nombre: 'Juana',
  apellido: 'Molina',
  modo: 'Banda propia',
  ciudad: 'Montevideo',
  país: 'Uruguay',
  habilidades: [{descripción:'voz', nivel:'superlativa'}]
});

db.final.insertOne({
  nombre: 'Angus',
  apellido: 'Young',
  ciudad: 'Glasgow',
  país: 'Escocia',
  modo: 'Showman',
  habilidades: [{ descripción: 'guitarrista', nivel: 'increíble' }]
});

db.final.insertOne({
  nombre: 'Ghost',
  ciudad: 'Linköping',
  país: 'Suecia',
  modo: 'Banda',
  habilidades: [{ descripción:'show', nivel: 'Increíble'}],
  inicio: 2006
});

db.final.insertOne({
  nombre: 'Rammstein',
  ciudad: 'Berlin',
  país: 'Alemania',
  musicos: ['Christoph Schneider', 'Oliver Riedel'],
  inicio: '1990',
  modo: 'Banda'
});

// 1) Querys:-----------------------------------------------------------

// 1. Obtener todos los documentos

db.final.find()

// 2. Obtener documentos con habilidad guitarrista.

db.final.find({"habilidades.descripción":'guitarrista'})

// 3. Obtener documentos con habilidad blusero

db.final.find({"habilidades.tipo":'blusero'})

// 4. Obtener los discos entre el año 2000 y 2010.

db.final.find({"discos.año":{$gte:2000, $lte:2010}},
{_id:0,"discos.nombre.$":1})

// El $ muestra el primer resultado que cumpla con eso.

// 2) Actualizar Documentos:--------------------------------------------

// 1. Agregar habilidades a un musico.

db.final.updateOne(
  { nombre:'David',apellido:'Lebon' },
  { $push: {habilidades: [{descripción:'voz',nivel:'superlativa'}]} } );

// 2. Agregar una ciudad a un musico.

db.final.updateOne(
  { nombre:'David',apellido:'Lebon' },
  { $set: {ciudad: 'Buenos Aires'} } );

// 3. Agregar los discos a una banda.

db.final.updateOne(
{nombre:'Rammstein'},
{$set: {discos:[{nombre:'Mutter',año:2001},{nombre:'Sehnsucht',año: 1997}]}})

// 4. Agregar los músicos a una banda.

db.final.updateOne({
nombre:'Rammstein'},
{$push: {musicos:'Christian Lorenz'}})

// 5. Cambiar el país de nacimiento de un intérprete.

db.final.updateOne({
nombre:'David',apellido:'Lebon'},
{$set:{país:'Argentina'}})

// 6. Eliminar el disco de una banda.

db.final.updateOne(
{nombre: 'Rammstein'},
{$pull: {discos: {nombre: 'Mutter' }}})

// 7. Cambiar el nivel de una habilidad.

db.fina.updateOne(
{nombre:'David', apellido:'Lebon',"habilidades.descripción":'bajista'},
{$set: {habilidades.$.nivel:'increible'}}})

// 8. Agregar comentarios a una banda (podrían ser más de uno).

db.final.updateOne(
{nombre:'Rammstein'},
{$push:{cometarios:'Son unos Cracks'}})
