#Diana de Leon 18607
#Fatima Albeño 18060
#Luis Perez Aju 18212
#Programa de consulta de doctores y receta de medicinas
#Base de datos en NEO4J

#Documentacion extraida de https://neo4j-rest-client.readthedocs.io/en/latest/

from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")

def addPaciente(nombre, genero, edad, peso ,estatura):
    paciente= gdb.nodes.create(Nombre=nombre, Genero=genero, Edad=edad, Peso=peso, Estatura=estatura)
    paciente.labels.add("Paciente")

def addDoctor (nombre, especialidad, telefono, correo, ubicacion):
    doctor= gdb.nodes.create(Nombre=nombre, Especialidad=especialidad, Telefono=telefono, Correo=correo, Ubicacion=ubicacion)
    doctor.labels.add("Doctor")

def addMedicina (nombre, dosis, vecesaldia, cantdias):
    medicina = gdb.nodes.create(Nombre=nombre, Dosis=dosis, Veces=vecesaldia, Dias=cantdias)
    medicina.labels.add("Medicina")

def addVisita (nomdoctor, nompaciente):
    pacientes= gdb.labels.get("Paciente")
    pacientes.all()
    doctores= gdb.labels.get("Doctor")
    doctores.all()
    pacientes.get(Nombre=nompaciente)[0].relationships.create("consulto",doctores.get(Nombre=nomdoctor)[0])

def prescripcion (nompaciente, nommedicina, nomdoctor):
    pacientes= gdb.labels.get("Paciente")
    pacientes.all()
    doctores= gdb.labels.get("Doctor")
    doctores.all()
    medicinas= gdb.labels.get("Medicina")
    medicinas.all()
    pacientes.get(Nombre=nompaciente)[0].relationships.create("toma",medicinas.get(Nombre=nommedicina)[0])
    doctores.get(Nombre0nomdoctor)[0].relationships.create("receta",medicinas.get(Nombre=nommedicina)[0])

def pacienteconoce (paciente1, paciente2):
    pacientes= gdb.labels.get("Paciente")
    pacientes.all()
    pacientes.get(Nombre=paciente1)[0].relationships.create("conoce",pacientes.get(Nombre=paciente2)[0])

def doctorconoce (doctor1, doctor2):
    doctores= gdb.labels.get("Doctor")
    doctores.all()
    doctores.get(Nombre=doctor1)[0].relationships.create("conocedoctor",doctores.get(Nombre=doctor2)[0])

def filtroespecialidad (tipo):
    buscar= "MATCH (n:Doctor {Especialidad: '"+tipo+"'}) RETURN n"
    resultados= gdb.query(buscar, data_contents=True)
    listado= resultados.rows
    return listado

def recomendacion(nompaciente, tipo):
    buscar = "MATCH (p:Paciente{Nombre:'"+nompaciente+"'})-[:conoce*1..2]->(amigos)-[:consulto]->(d:Doctor{Especialidad:'"+tipo+"'}) RETURN d"
    resultados = gdb.query(buscar, data_contents=True)
    listado = resultados.rows
    loficial = []
    for x in listado:
        if x not in loficial:
            loficial.append(x)
    return loficial

def recomendaciondoctor (nomdoctor, tipo):
    buscar = "MATCH (d:Doctor{Nombre:'"+nomdoctor+"'})-[:conocedoctor*1..2]->(a:Doctor{Especialidad:'"+tipo+"'}) RETURN a"
    resultados = gdb.query(query, data_contents=True)
    listado = resultados.rows
    loficial = []
    for x in listados:
        if x not in loficial:
            loficial.append(x)
    return loficial

opcion=0
print("1. Agregar un paciente\n2. Agregar un doctor\n3. Agregar medicina\n4. Paciente visita doctor\n5. Doctor receta medicina\n6. Consultar doctor segun especialidad\n7. Añadir conocido\n8. Añadir doctor conocido\n9. Recomendacion segun conocidos\n10. Doctor recomienda doctor\n11. Salir")
opcion=int(input("Ingrese una opcion: "))

while (opcion!=11):
    
    if (opcion==1):
        print("----------Añadir paciente----------")
        nombre=input("Ingrese su nombre: ")
        genero=input("Ingrese su genero: ")
        edad=input("Ingrese su edad: ")
        peso=input("Ingrese su peso: ")
        estatura=input("Ingrese su estatura: ")
        addPaciente(nombre, genero, edad, peso, estatura)
        print("Se ha añadido exitosamente el paciente. \n")
        
    elif (opcion==2):
        print("-----------Añadir doctor-----------")
        nombre=input("Ingrese su nombre: ")
        espec=input("Ingrese su especialidad: ")
        tel=input("Ingrese su numero telefonico: ")
        correo=input("Ingrese su correo: ")
        ubic=input("Ingrese la ubicacion de su clinica: ")
        addDoctor(nombre,espec,tel,correo,ubic)
        print("Se ha añadido existosamente el doctor. \n")

    elif (opcion==3):
        print("----------Añadir medicina----------")
        nombre=input("Ingrese el nombre de la medicina: ")
        dosis=input("Ingrese la dosis de medicina: ")
        veces=input("Ingrese el intervalo de tiempo de consumo: ")
        dias=input("Ingrese la cantidad de dias que se tomara la medicina: ")
        addMedicina(nombre,dosis,veces,dias)
        print("Se ha añadido exitosamente la medicina. \n")

    elif (opcion==4):
        print("----------Crear consulta----------")
        nombre = input("Ingrese su nombre: ")
        doctor = input("Ingrese el nombre del doctor al que visitó: ")
        try:
            addVisita(nombre,doctor)
            print("Se agregó su visita con éxito. \n")
        except IndexError:
                print("\nLos nombres ingresados no están en la base de datos. \n")

    elif (opcion==5):
        print("----------Recetar medicina----------")
        paciente = input("Ingrese el nombre del paciente: ")
        medicina = input("Ingrese la medicina recomendada: ")
        doctor = input("Ingrese el nombre del doctor: ")
        try:
            prescripcion(paciente, medicina, doctor)
        except IndexError:
                print("\nLos datos ingresados no están en la base de datos. \n")
            
    elif (opcion==6):
        print("----------Buscar doctor por especialidad----------")
        especialidad = input("Ingrese la especialidad del doctor: ")
        try:
            es = filtroespecialidad(especialidad)
            a=""
            if es is not None:
                for i in es:
                    for x in i:
                        a+="-"
                        for c in x:
                            a+=str(c)+" : "+str(x[c])+"\t"
                    a+="\n"
                print(a)
            else:
                print("\nNo hay ningun doctor con esa especialidad en la base de datos. \n")
        except IndexError:
                print("\nNo hay ningun doctor con esa especialidad en la base de datos. \n")
        
    elif (opcion==7):
        print("----------Añadir a alguien a mis conocidos----------")
        conocido=input("Ingrese su nombre: ")
        conocido2=input("Ingrese el nombre de su conocido: ")
        try:
            pacienteconoce(conocido, conocido2)
            print("Se ha añadido a la persona conocida con exito. \n")
        except IndexError:
                print("\nLos nombres ingresados no están en la base de datos. \n")

    elif (opcion==8):
        print("----------Doctor añade colega----------")
        conocido=input("Ingrese su nombre: ")
        conocido2=input("Ingrese el nombre de su conocido: ")
        try:
            doctorconoce(conocido, conocido2)
            print("Se ha añadido a la persona conocida con exito. \n")
        except IndexError:
                print("\nLos nombres ingresados no están en la base de datos. \n")

    elif (opcion==9):
        print("----------Recomendar doctor de un conocido----------")
        nombre=input("Ingrese su nombre: ")
        es=input("Ingrese la especialidad del doctor que necesita: ")
        try:
            lista=recomendacion(nombre,es)
            a=""
            if lista is not None:
                for i in lista:
                    for x in i:
                        a+="-"
                        for c in x:
                            a+=str(c)+" : "+str(x[c])+"\t"
                    a+="\n"
                print(a)
            else:
                print("\nNo hay ningun doctor con esa especialidad en la base de datos. \n")
        except IndexError:
            print("\nLos datos ingresados no están en la base de datos. \n")
            
    elif (opcion==10):
        print("----------Doctor recomienda otro doctor----------")
        nombre=input("Ingrese el nombre de su doctor: ")
        es=input("Ingrese la especialidad del doctor que necesita: ")
        try:
            lista=recomendaciondoctor(nombre,es)
            a=""
            if lista is not None:
                for i in lista:
                    for x in i:
                        a+="-"
                        for c in x:
                            a+=str(c)+" : "+str(x[c])+"\t"
                    a+="\n"
                print(a)
            else:
                print("\nNo hay ningun doctor con esa especialidad en la base de datos. \n")
        except IndexError:
            print("\nLos datos ingresados no están en la base de datos. \n")

    else:
        print("La opcion no es valida. \n")

    print("\n*****************************************************************\n")
    print("1. Agregar un paciente\n2. Agregar un doctor\n3. Agregar medicina\n4. Paciente visita doctor\n5. Doctor receta medicina\n6. Consultar doctor segun especialidad\n7. Añadir conocido\n8. Añadir doctor conocido\n9. Recomendacion segun conocidos\n10. Doctor recomienda doctor\n11. Salir")
    opcion=int(input("Ingrese una opcion: "))


print("********Gracias por usar nuestro sistema de recomendacion********\n")

