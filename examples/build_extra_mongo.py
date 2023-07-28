// Iniciar mongo

sudo systemctl start mongod // correr mongo

mongosh // entrar a consola mongo

show dbs // mostrar dbs

use viajes // usar o crear esa db


// Modelado --------------------
// crear colleccion o insertar datos en collection
db.viajes.insertOne(
	{
			numero: 1,
	    usario: {
				nombre: "Bunny",
				nacimiento: 2003
			},
	    lugarOrigen: "Berlin",
			fechaorigen: new Date('2019-01-15T11:25'),
			lugarDestino: "Paris",
			fechaDestino: new Date('2023-04-12T09:28')
	}
);


// Inserts --------------------

db.viajes.insertOne({numero: 1, usario: { nombre: "Bunny", nacimiento: 2003 }, lugarOrigen: "Berlin", fechaorigen: new Date('2020-04-12T09:28'), lugarDestino: "Paris", fechaDestino: new Date('2020-04-13T11:25')});
db.viajes.insertOne({numero: 2, usario: { nombre: "Bunny", nacimiento: 2006 }, lugarOrigen: "Buenos Aires", fechaorigen: new Date('2021-04-12T09:28'), lugarDestino: "Paris", fechaDestino: new Date('2021-06-30T11:25')});

db.viajes.insertOne({numero: 3, usario: { nombre: "Alice", nacimiento: 1992 }, lugarOrigen: "San Francisco", fechaorigen: new Date('2022-08-15T10:00'), lugarDestino: "Tokyo", fechaDestino: new Date('2022-08-16T16:30')});
db.viajes.insertOne({numero: 4, usario: { nombre: "Bob", nacimiento: 1980 }, lugarOrigen: "London", fechaorigen: new Date('2021-12-20T09:45'), lugarDestino: "New York", fechaDestino: new Date('2021-12-21T14:15')});
db.viajes.insertOne({numero: 5, usario: { nombre: "Emily", nacimiento: 2001 }, lugarOrigen: "Sydney", fechaorigen: new Date('2023-02-05T08:30'), lugarDestino: "Paris", fechaDestino: new Date('2023-02-06T12:00')});
db.viajes.insertOne({numero: 6, usario: { nombre: "Michael", nacimiento: 1975 }, lugarOrigen: "Berlin", fechaorigen: new Date('2022-05-10T13:20'), lugarDestino: "Cape Town", fechaDestino: new Date('2022-05-15T09:55')});
db.viajes.insertOne({numero: 7, usario: { nombre: "Sophia", nacimiento: 1998 }, lugarOrigen: "Los Angeles", fechaorigen: new Date('2023-06-20T11:00'), lugarDestino: "Tokyo", fechaDestino: new Date('2023-06-21T17:30')});


// Modificar documentos --------------------

// No es necesario el user y nac, con el id del viaje alcanza, cambio el viaje redondo
db.viajes.updateOne(
	{numero: 3, "usuario.nombre":"Alice", "usuario.nacimineto": 1992}, {$set: {lugarDestino: "San Francisco"}}
);

// cambio el viaje mas largo
db.viajes.updateOne(
	{numero: 3, "usuario.nombre":"Bob", "usuario.nacimineto": 1980}, {$set: {fechaDestino: new Date('2060-05-23T10:10')}}
);

// updetea todos los bunnys a nacimiento 2000
db.viajes.updateMany(
	{"usuario.nombre":"Bunny"}, {$set: {"usuario.nacimineto": 2000}}
);



// Ejecutar Queries --------------------

//1.	¿Cuántos viajes hizo el usuario Bunny?
db.viajes.count({"usuario.nombre":"Bunny", "usuario.nacimiento": 2003});

// Otra forma con aggregate
db.viajes.aggregate(
	[
		{
			$match: {
				"usuario.nombre":"Bunny",
				nacimiento: 2003
			}
		},
		{
			$count: "cantidadDeViajes"
		}
	]
);


// 2.	¿Quiénes hicieron un viaje redondo (es decir salieron y llegaron al mismo destino)?
db.viajes.find({ $expr: { $eq: ["$lugarOrigen", "$lugarDestino"] }});


// 3.	¿Cuál fue el usuario con más viajes (puede ser más de uno)?
db.viajes.aggregate( [ { $group: { _id: {"usuario.nombre":"$usuario.nombre", "usuario.nacimiento":"$usuario.nacimiento" }, viajes: { $count: "$numero" } } },] );

// para que quede perfecto deberia agrupar por id de user no por nombre solo
db.viajes.aggregate( [ { $group: { _id: "$usuario.idCuenta", viajes: { $count: "$numero" } } },] );


// 4.	¿Cuál fue el origen y destino del viaje más largo (en tiempo)?
db.viajes.aggregate( [ { $group: { _id: "$numero", largo: { $substract: ["fechaDestino","fechaOrigen"] } } }, { $project: { numero: 1, fechaOrigen: 1, fechaDestino: 1} }, { $sort: { largo: -1 } }, { $limit: 1 } ] );


// 5.	¿Qué orígenes y destinos son los más populares?
// Origen mas popular
db.viajes.aggregate([ { $group: { _id: "$lugarOrigen", cant: { $count: "$lugarOrigen"} } }, { $project: {lugarOrigen: 1} }, { $sort: { cant: -1 } }, { $limit: 1 } ]);

// Destino mas popular
db.viajes.aggregate([ { $group: { _id: "$lugarDestino", cant: { $count: "$lugarDestino"} } }, { $project: {lugarDestino: 1} }, { $sort: { cant: -1 } }, { $limit: 1 } ]);


// 6.	¿En qué días de la semana se realizan la mayoría de los viajes?
db.viajes.aggregate([ { $group: { dayOfWeek: { $dayOfWeek: "$fechaOrigen"}, cant: { $count: "$numero"} } }, { $project: {dayOfWeek: 1} }, { $sort: { cant: -1 } }, { $limit: 3 } ]);
