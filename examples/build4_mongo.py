from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import time

# Conectar al cluster de Cassandra
cluster = Cluster(['127.0.0.1'])  # Reemplaza 'tu_direccion_ip_cassandra' por la dirección IP de tu cluster Cassandra
session = cluster.connect()

# Seleccionar el keyspace adecuado
keyspace = 'empleados'  # Reemplaza 'nombre_del_keyspace' por el nombre de tu keyspace
session.set_keyspace(keyspace)

# Revisar consultas 3, 5, 6, y 7.
# Revisar sobre todo la consulta 7.


# Primera consulta:

# INSERCION Q1
def insert_data_Q1():
    query = """
    INSERT INTO liderazgoFutbol (nombre, apellido, ciudad, pais, habilidad, deporte)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    nombre = input('Ingrese el nombre del empleado: ')
    apellido = input('Ingrese el apellido del empleado: ')
    ciudad = input('Ingrese la ciudad del empleado: ')
    pais = input('Ingrese el pais del empleado: ')
    habilidad = input('Ingrese la habilidad del empleado: ')
    deporte = input('Ingrese el deporte del empleado: ')

    session.execute(query, (nombre, apellido, ciudad, pais, habilidad, deporte))

# SELECT * FROM
def select_all_data_Q1():
    query = "SELECT * FROM liderazgoFutbol;"
    result = session.execute(query)
    for row in result:
        print(row)

# Consulta Q1
def select_data_Q1():
    query = """
    SELECT nombre, apellido, ciudad, pais, habilidad, deporte
    FROM liderazgoFutbol
    WHERE habilidad = 'Liderazgo' AND deporte = 'Futbol';
    """
    result = session.execute(query)
    for row in result:
        print(row)


# Segunda consulta:

# INSERCION Q2
def insert_data_Q2():
    query = """
    INSERT INTO trabajosPrevios (nombre, apellido, ciudad, pais, habilidad, trabajoPrevio)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    nombre = input('Ingrese el nombre del empleado: ')
    apellido = input('Ingrese el apellido del empleado: ')
    ciudad = input('Ingrese la ciudad del empleado: ')
    pais = input('Ingrese el pais del empleado: ')
    habilidad = input('Ingrese la habilidad del empleado: ')
    trabajoPrevio = input('Ingrese el trabajo previo del empleado: ')

    session.execute(query, (nombre, apellido, ciudad, pais, habilidad, trabajoPrevio))
'''
VALUES ('Jorge', 'Diaz', 'Buenos Aires', 'Argentina', 'Especialistas en Procesos', 'Atención al público');
VALUES ('Mariano', 'Perez', 'Buenos Aires', 'Argentina', 'Especialistas en Procesos', 'Programador');
VALUES ('Jorge', 'Gomez', 'Buenos Aires', 'Argentina', 'Especialista en Marketing', 'Mozo');
VALUES ('John', 'Smith', 'Seattle', 'Estados Unidos', 'Analista contable', 'Albañil');
VALUES ('Marcelo', 'Lopez', 'Buenos Aires', 'Argentina', 'Especialista en programación', 'Contador');
'''

# SELECT * FROM
def select_all_data_Q2():
    query = "SELECT * FROM trabajosPrevios;"
    result = session.execute(query)
    for row in result:
        print(row)

# Consulta Q2
def select_data_Q2():
    query = """
    SELECT nombre, apellido, ciudad, pais, habilidad, trabajoPrevio
    FROM trabajosPrevios
    WHERE habilidad = 'Especialistas en Procesos';
    """
    result = session.execute(query)
    for row in result:
        print(row)


# Tercera consulta:

# INSERCION Q3

def insert_data_Q3():
    query = """
    INSERT INTO deportesEntre (nombre, apellido, ciudad, pais, trabajoPrevio, anioIni, anioFin, deportes)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    ciudad = input("Ingrese la ciudad del empleado: ")
    pais = input("Ingrese el país del empleado: ")
    trabajoPrevio = input("Ingrese el trabajo previo del empleado: ")
    anioIni = int(input("Ingrese el año de inicio del trabajo previo: "))
    anioFin = int(input("Ingrese el año de fin del trabajo previo: "))
    
    deportes = set()  # Creamos un conjunto vacío para almacenar los deportes

    # Solicitamos al usuario ingresar los deportes hasta que ingrese "salir"
    while True:
        deporte = input("Ingrese un deporte (o escriba 'salir' para terminar): ")
        if deporte.lower() == "salir":
            break
        deportes.add(deporte)
    
    session.execute(query, (nombre, apellido, ciudad, pais, trabajoPrevio, anioIni, anioFin, deportes))

'''
insert_data_query3('Jorge', 'Diaz', 'Buenos Aires', 'Argentina', 'Carpintero', 1999, 2009, {'hockey', 'rugby'})
insert_data_query3('Mariano', 'Perez', 'Buenos Aires', 'Argentina', 'Contador', 2011, 2019, {'futbol', 'handball'})
insert_data_query3('Jorge', 'Gomez', 'Buenos Aires', 'Argentina', 'Mozo', 2012, 2019, {'ping-pong', 'tenis'})
insert_data_query3('John', 'Smith', 'Seattle', 'Estados Unidos', 'Analista funcional', 2005, 2021, {'voley', 'basquet'})
insert_data_query3('Marcelo', 'Lopez', 'Buenos Aires', 'Argentina', 'Analista contable', 2013, 2018, {'futbol', 'tenis'})'''

# SELECT * FROM
def select_all_data_Q3():
    query = "SELECT * FROM deportesEntre;"
    result = session.execute(query)
    for row in result:
        print(row)

# Consulta Q3
def select_data_Q3():
    query = """
    SELECT nombre, apellido, deportes
    FROM deportesEntre
    WHERE anioIni >= 2010 AND anioFin <= 2020
    ALLOW FILTERING;
    """
    result = session.execute(query)
    for row in result:
        print(row)


# Cuarta consulta

# INSERCION Q4
def insert_data_Q4():
    query = """
    INSERT INTO deporteRiesgo (nombre, apellido, ciudad, pais, tipoDeporte, anioIni)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    nombre = input('Ingrese el nombre del empleado: ')
    apellido = input('Ingrese el apellido del empleado: ')
    ciudad = input('Ingrese la ciudad del empleado: ')
    pais = input('Ingrese el pais del empleado: ')
    tipoDeporte = input('Ingrese el tipo de deporte del empleado: ')
    anioIni = int(input('Ingrese el año de inicio del empleado: '))

    session.execute(query, (nombre, apellido, ciudad, pais, tipoDeporte, anioIni))

'''
VALUES ('Jorge', 'Diaz', 'Buenos Aires', 'Argentina', 'Federado', 1999);
VALUES ('Mariano', 'Perez', 'Buenos Aires', 'Argentina', 'Riesgo', 2011);
VALUES ('Jorge', 'Gomez', 'Buenos Aires', 'Argentina', 'Riesgo', 2021);
VALUES ('John', 'Smith', 'Seattle', 'Estados Unidos', 'Riesgo', 2021);
VALUES ('Marcelo', 'Lopez', 'Buenos Aires', 'Argentina', 'Federado', 2021);'''

# SELECT * FROM
def select_all_data_Q4():
    query = "SELECT * FROM deporteRiesgo;"
    result = session.execute(query)
    for row in result:
        print(row)

# Consulta Q4
def select_data_Q4():
    query = """
    SELECT nombre, apellido, ciudad, pais
    FROM deporteRiesgo
    WHERE tipoDeporte = 'Riesgo' AND anioIni >= 2021;
    """
    result = session.execute(query)
    for row in result:
        print(row)


# Quinta consulta

# INSERCION Q5
def insert_data_Q5():
    query = """
    INSERT INTO habilidadesPorEmpleado (nombre, apellido, ciudad, pais, habilidades)
    VALUES (%s, %s, %s, %s, %s);
    """
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    ciudad = input("Ingrese la ciudad del empleado: ")
    pais = input("Ingrese el país del empleado: ")
    
    habilidades = set()  # Creamos un conjunto vacío para almacenar las habilidades

    # Solicitamos al usuario ingresar las habilidades hasta que ingrese "salir"
    while True:
        habilidad = input("Ingrese una habilidad (o escriba 'salir' para terminar): ")
        if habilidad.lower() == "salir":
            break
        habilidades.add(habilidad)
    
    session.execute(query, (nombre, apellido, ciudad, pais, habilidades))

'''
insert_data_query5('Jorge', 'Diaz', 'Buenos Aires', 'Argentina', {'Innovación', 'Creatividad'})
insert_data_query5('Mariano', 'Perez', 'Buenos Aires', 'Argentina', {'Proactividad', 'Inteligencia'})
insert_data_query5('Jorge', 'Gomez', 'Buenos Aires', 'Argentina', {'Paciencia', 'Empatía'})
insert_data_query5('John', 'Smith', 'Seattle', 'Estados Unidos', {'Carisma', 'Creatividad', 'Innovación'})
insert_data_query5('Marcelo', 'Lopez', 'Buenos Aires', 'Argentina', {'Tolerancia', 'Compromiso'})'''

# SELECT * FROM
def select_all_data_Q5():
    query = "SELECT * FROM habilidadesPorEmpleado;"
    result = session.execute(query)
    for row in result:
        print(row)

# Consulta Q5
def select_data_Q5():
    query = """
    SELECT nombre, apellido, ciudad, pais, habilidades
    FROM habilidadesPorEmpleado
    WHERE nombre = 'John' AND apellido = 'Smith';
    """
    result = session.execute(query)
    for row in result:
        print(row)


# Sexta consulta

# INSERCION Q6
def insert_data_Q6():
    query = """
    INSERT INTO programadoresDeportes (nombre, apellido, ciudad, pais, habilidad, deportes)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    ciudad = input("Ingrese la ciudad del empleado: ")
    pais = input("Ingrese el país del empleado: ")
    habilidad = input("Ingrese la habilidad del empleado: ")
    deportes = set()

    while True:
        deporte = input("Ingrese un deporte (o escriba 'salir' para terminar): ")
        if deporte.lower() == 'salir':
            break;
        deportes.add(deporte)

    session.execute(query, (nombre, apellido, ciudad, pais, habilidad, deportes))

'''
insert_data_query6('Jorge', 'Diaz', 'Buenos Aires', 'Argentina', 'Experto Programador', {'voley', 'tenis'})
insert_data_query6('Mariano', 'Perez', 'Buenos Aires', 'Argentina', 'Experto en Marketing', {'basquet', 'tenis'})
insert_data_query6('Jorge', 'Gomez', 'Buenos Aires', 'Argentina', 'Experto en finanzas', {'futbol', 'voley'})
insert_data_query6('John', 'Smith', 'Seattle', 'Estados Unidos', 'Experto Programador', {'basquet', 'baseball'})
insert_data_query6('Marcelo', 'Lopez', 'Buenos Aires', 'Argentina', 'Experto en contaduría', {'hockey', 'futbol'})'''

# SELECT * FROM
def select_all_data_Q6():
    query = "SELECT * FROM programadoresDeportes;"
    result = session.execute(query)
    for row in result:
        print(row)

# Consulta Q6
def select_data_Q6():
    query = """
    SELECT nombre, apellido, deportes
    FROM programadoresDeportes
    WHERE habilidad = 'Experto Programador';
    """
    result = session.execute(query)
    for row in result:
        print(row)


# Septima consulta

# INSERCION Q7
def insert_data_Q7():
    query = """
    INSERT INTO contaduriaDeportes (nombre, apellido, ciudad, pais, habilidad, tipoDeportes)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    nombre = input('Ingrese el nombre del empleado: ')
    apellido = input('Ingrese el apellido del empleado: ')
    ciudad = input('Ingrese la ciudad del empleado: ')
    pais = input('Ingrese el pais del empleado: ')
    habilidad = input('Ingrese la habilidad del empleado: ')
    tipo_deportes = []

    while True:
        deporte = input("Ingrese un deporte (o escriba 'salir' para terminar): ")
        if deporte.lower() == 'salir':
            break;
        tipo_deportes.append(deporte)

    session.execute(query, (nombre, apellido, ciudad, pais, habilidad, tipo_deportes))

'''
VALUES ('Jorge', 'Gomez', 'Buenos Aires', 'Argentina', 'Experto Programador', ['federado', 'riesgo']);
VALUES ('Mariano', 'Perez', 'Buenos Aires', 'Argentina', 'Experto en contaduria', ['federado', 'federado']);
VALUES ('Jorge', 'Gomez', 'Buenos Aires', 'Argentina', 'Experto en finanzas', ['riesgo', 'federado']);
VALUES ('John', 'Smith', 'Seattle', 'Estados Unidos', 'Experto Programador', ['federado', 'federado']);
VALUES ('Marcelo', 'Lopez', 'Buenos Aires', 'Argentina', 'Experto en contaduria', ['riesgo', 'riesgo']);
'''

# SELECT * FROM
def select_all_data_Q7():
    query = "SELECT * FROM contaduriaDeportes;"
    result = session.execute(query)
    for row in result:
        print(row)

# Consulta Q7
def select_data_Q7():
    query = """
    SELECT nombre, apellido, ciudad, pais
    FROM contaduriaDeportes
    WHERE habilidad = 'Experto en contaduria' AND tipoDeportes CONTAINS 'federado'
    ALLOW FILTERING;
    """
    result = session.execute(query)
    for row in result:
        print(row)


# Octava consulta

# INSERCION Q8
def insert_data_Q8():
    query = """
    INSERT INTO expertoProgramador (nombre, apellido, ciudad, pais, habilidad, trabajoPrevio, anioIni, anioFin)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    nombre = input('Ingrese el nombre del empleado: ')
    apellido = input('Ingrese el apellido del empleado: ')
    ciudad = input('Ingrese la ciudad del empleado: ')
    pais = input('Ingrese el pais del empleado: ')
    habilidad = input('Ingrese la habilidad del empleado: ')
    trabajoPrevio = input('Ingrese el trabajo previo del empleado: ')
    anioIni = int(input('Ingrese el año de inicio del empleado: '))
    anioFin = int(input('Ingrese el año de fin del empleado: '))

    session.execute(query, (nombre, apellido, ciudad, pais, habilidad, trabajoPrevio, anioIni, anioFin))

'''
VALUES ('Jorge', 'Gomez', 'Buenos Aires', 'Argentina', 'Experto Programador', 'Comunicaciones', 2004, 2009);
VALUES ('Mariano', 'Perez', 'Buenos Aires', 'Argentina', 'Experto en Contaduría', 'Contabilidad', 2012, 2019);
VALUES ('Jorge', 'Gomez', 'Buenos Aires', 'Argentina', 'Experto en Finanzas', 'Contabilidad', 2009, 2014);
VALUES ('John', 'Smith', 'Seattle', 'Estados Unidos', 'Experto en Finanzas', 'Programación', 2011, 2017);
VALUES ('Marcelo', 'Lopez', 'Buenos Aires', 'Argentina', 'Experto Programador', 'Comunicaciones', 2014, 2019);'''

# SELECT * FROM
def select_all_data_Q8():
    query = "SELECT * FROM expertoProgramador;"
    result = session.execute(query)
    for row in result:
        print(row)

# Consulta Q8
def select_data_Q8():
    query = """
    SELECT nombre, apellido, ciudad, pais, habilidad, trabajoPrevio
    FROM expertoProgramador
    WHERE habilidad = 'Experto Programador' AND trabajoPrevio = 'Comunicaciones' AND anioIni >= 2010 AND anioFin <= 2020
    ALLOW FILTERING;
    """
    result = session.execute(query)
    for row in result:
        print(row)

def menu():

    print('Bienvenido, elija una query')
    print('--------------------------------------')
    print('1. liderazgoFutbol')
    print('2. trabajosPrevios')
    print('3. deportesEntre')
    print('4. deporteRiesgo')
    print('5. habilidadesPorEmpleado')
    print('6. programadoresDeportes')
    print('7. contaduriaDeportes')
    print('8. expertoProgramador')
    print('--------------------------------------')
    print()

    opcion = input('Opción: ')
    if opcion == '1' :

        print("Elija la operación")
        print('--------------------------------------')
        print('1. Cargar datos')
        print('2. Mostrar datos')
        print('3. Ejecutar Query')
        print('--------------------------------------')
        print()

        opcion = input('Opción: ')

        if opcion == '1' :
            insert_data_Q1()
            print('Carga realizada')
            time.sleep(5)
            menu()

        elif opcion == '2' :
            select_all_data_Q1()
            time.sleep(5)
            menu()

        elif opcion == '3' :
            select_data_Q1()
            time.sleep(5)
            menu()

        else:
            print("Opción incorrecta")
            time.sleep(5)
            menu()

    elif opcion == '2' :
        print("Elija la operación")
        print('--------------------------------------')
        print('1. Cargar datos')
        print('2. Mostrar datos')
        print('3. Ejecutar Query')
        print('--------------------------------------')
        print()

        opcion = input('Opción: ')
    
        if opcion == '1' :
            insert_data_Q2()
            print('Carga realizada')
            time.sleep(5)
            menu()
    
        elif opcion == '2' :
            select_all_data_Q2()
            time.sleep(5)
            menu()
    
        elif opcion == '3' :
            select_data_Q2()
            time.sleep(5)
            menu()
    
        else:
            print("Opción incorrecta")
            time.sleep(5)
            menu()
    
    elif opcion == '3' :
        print("Elija la operación")
        print('--------------------------------------')
        print('1. Cargar datos')
        print('2. Mostrar datos')
        print('3. Ejecutar Query')
        print('--------------------------------------')
        print()

        opcion = input('opcion: ')
    
        if opcion == '1' :
            insert_data_Q3()
            print('Carga realizada')
            time.sleep(5)
            menu()
    
        elif opcion == '2' :
            select_all_data_Q3()
            time.sleep(5)
            menu()
    
        elif opcion == '3' :
            select_data_Q3()
            time.sleep(5)
            menu()
    
        else:
            print("Opción incorrecta")
            time.sleep(5)
            menu()
    
    elif opcion == '4' :
        print("Elija la operación")
        print('--------------------------------------')
        print('1. Cargar datos')
        print('2. Mostrar datos')
        print('3. Ejecutar Query')
        print('--------------------------------------')
        print()

        opcion = input('Opción: ')
    
        if opcion == '1' :
            insert_data_Q4()
            print('Carga realizada')
            time.sleep(5)
            menu()
    
        elif opcion == '2' :
            select_all_data_Q4()
            time.sleep(5)
            menu()
    
        elif opcion == '3' :
            select_data_Q4()
            time.sleep(5)
            menu()
    
        else:
            print("Opción incorrecta")
            time.sleep(5)
            menu()
    
    elif opcion == '5' :
        print("Elija la operación")
        print('--------------------------------------')
        print('1. Cargar datos')
        print('2. Mostrar datos')
        print('3. Ejecutar Query')
        print('--------------------------------------')
        print()

        opcion = input('Opción: ')
    
        if opcion == '1' :
            insert_data_Q5()
            print('Carga realizada')
            time.sleep(3)
            menu()
    
        elif opcion == '2' :
            select_all_data_Q5()
            time.sleep(3)
            menu()
    
        elif opcion == '3' :
            select_data_Q5()
            time.sleep(3)
            menu()
    
        else:
            print("Opción incorrecta")
            time.sleep(3)
            menu()

    elif opcion == '6' :
        print("Elija la operación")
        print('--------------------------------------')
        print('1. Cargar datos')
        print('2. Mostrar datos')
        print('3. Ejecutar Query')
        print('--------------------------------------')
        print()

        opcion = input('opcion: ')
    
        if opcion == '1' :
            insert_data_Q6()
            print('Carga realizada')
            time.sleep(2)
            menu()
    
        elif opcion == '2' :
            select_all_data_Q6()
            time.sleep(2)
            menu()
    
        elif opcion == '3' :
            select_data_Q6()
            time.sleep(2)
            menu()
    
        else:
            print("Opción incorrecta")
            time.sleep(2)
            menu()
    
    elif opcion == '7' :
        print("Elija la operación")
        print('--------------------------------------')
        print('1. Cargar datos')
        print('2. Mostrar datos')
        print('3. Ejecutar Query')
        print('--------------------------------------')
        print()

        opcion = input('opcion: ')
    
        if opcion == '1' :
            insert_data_Q7()
            print('Carga realizada')
            time.sleep(2)
            menu()
    
        elif opcion == '2' :
            select_all_data_Q7()
            time.sleep(2)
            menu()
    
        elif opcion == '3' :
            select_data_Q7()
            time.sleep(2)
            menu()
    
        else:
            print("Opción incorrecta")
            time.sleep(2)
            menu()
    
    elif opcion == '8' :
        print("Elija la opearación")
        print('--------------------------------------')
        print('1. Cargar datos')
        print('2. Mostrar datos')
        print('3. Ejecutar Query')
        print('--------------------------------------')
        print()

        opcion = input('Opción: ')
    
        if opcion == '1' :
            insert_data_Q8()
            print('Carga realizada')
            time.sleep(2)
            menu()
    
        elif opcion == '2' :
            select_all_data_Q8()
            time.sleep(2)
            menu()
    
        elif opcion == '3' :
            select_data_Q8()
            time.sleep(2)
            menu()
    
        else:
            print("Opción incorrecta")
            time.sleep(2)
            menu()

# Run program
menu()
