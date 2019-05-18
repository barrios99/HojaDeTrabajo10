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

def prescripcion (nompaciente, nomdoctor,nommedicina):
    pacientes= gdb.labels.get("Paciente")
    pacientes.all()
    doctores= gdb.labels.get("Doctor")
    doctores.all()
    medicinas= gdb.labels.get("Medicina")
    medicinas.all()
    pacientes.get(Nombre=nompaciente)[0].relationships.create("toma",medicinas.get(Nombre=nommedicina)[0])
    doctores.get(Nombre=nomdoctor)[0].relationships.create("receta",medicinas.get(Nombre=nommedicina)[0])

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
    if listado is not None:
        for x in listado:
            if x not in loficial:
                loficial.append(x)
    return loficial

def recomendaciondoctor (nomdoctor, tipo):
    buscar = "MATCH (d:Doctor{Nombre:'"+nomdoctor+"'})-[:conocedoctor*1..2]->(a:Doctor{Especialidad:'"+tipo+"'}) RETURN a"
    resultados = gdb.query(buscar, data_contents=True)
    listado = resultados.rows
    loficial = []
    if listado is not None:
        for x in listado:
            if x not in loficial:
                loficial.append(x)
    return loficial

#-------------------------------------------------------------------------------------------------------------------------------------------

#Datos para la base
addPaciente("Fernando","Hombre","20","140","1.72")
addPaciente("Mario","Hombre","30","160","1.61")
addPaciente("Roberto","Hombre","22","154","1.83")
addPaciente("Juan","Hombre","28","145","1.64")
addPaciente("Antonio","Hombre","63","122","1.41")
addPaciente("Fernanda","Mujer","19","112","1.43")
addPaciente("Sofia","Mujer","46","132","1.52")
addPaciente("Maria","Mujer","15","120","1.30")
addPaciente("Diana","Mujer","24","123","1.47")
addPaciente("Ana","Mujer","33","141","1.58")

addDoctor("Saul", "Pediatra", "22334499","saul@gmail.com","Zona 1 de Guatemala")
addDoctor("Manuel", "Cirujano","1239641","manuel@gmail.com","Fraijanes")
addDoctor("Estuardo", "Dermatologo", "63109862","estuardo@gmail.com","San Jose Pinula")
addDoctor("Daniel", "Pediatra", "43006901","daniel@gmail.com","Zona 1 de Mixco")
addDoctor("Alejandro", "Dentista", "36094881","alejandro@gmail.com","Villa Nueva")
addDoctor("Jazmin", "Oftalmologo", "48930132","jazmin@gmail.com","Zona 1 de Guatemala")
addDoctor("Susana", "Ginecologa", "66930128","susana@gmail.com","San Lucas")
addDoctor("Camila", "Traumatologa", "75755326","camila@gmail.com","San Cristobal")
addDoctor("Izabel", "Fisioterapeuta", "86910751","izabel@gmail.com","Cienaga Grande")
addDoctor("Joseline", "Cardiologa", "40755697","joseline@gmail.com","Sumpango")

addMedicina("Diclofenaco","500","3","12")
addMedicina("Vitaflenaco","1000","2","16")
addMedicina("Tabcin","250","4","4")
addMedicina("Hibuprofeno","500","2","20")
addMedicina("Loratadina","300","3","6")
addMedicina("Panadol","1000","4","4")
addMedicina("Cardiovital","1000","3","10")
addMedicina("Aspirina","500","2","15")
addMedicina("Parecetamol","30","4","8")
addMedicina("Atarax","25","1","9")

#addVisita("Saul","Fernanda")
addVisita("Manuel","Mario")
addVisita("Estuardo","Roberto")
addVisita("Daniel","Juan")
#addVisita("Alejandro","Antonio")
addVisita("Jazmin","Fernando")
addVisita("Susana","Sofia")
addVisita("Camila","Maria")
#addVisita("Izabel","Diana")
addVisita("Joseline","Ana")

#prescripcion("Fernanda","Saul","Diclofenaco")
prescripcion("Mario","Manuel","Vitaflenaco")
prescripcion("Roberto","Estuardo","Tabcin")
prescripcion("Juan","Daniel","Hibuprofeno")
#prescripcion("Antonio","Alejandro","Loratadina")
prescripcion("Fernando","Jazmin","Panadol")
prescripcion("Sofia","Susana","Cardiovital")
prescripcion("Maria","Camila","Aspirina")
#prescripcion("Diana","Izabel","Parecetamol")
prescripcion("Ana","Joseline","Atarax")

pacienteconoce("Fernanda", "Mario")
pacienteconoce("Mario", "Juan")
pacienteconoce("Roberto", "Sofia")
pacienteconoce("Juan", "Sofia")
pacienteconoce("Antonio", "Diana")
pacienteconoce("Fernando", "Ana")
pacienteconoce("Sofia", "Roberto")
pacienteconoce("Maria", "Fernanda")
pacienteconoce("Diana", "Mario")
pacienteconoce("Ana", "Juan")

doctorconoce("Saul","Joseline")
doctorconoce("Manuel","Izabel")
doctorconoce("Estuardo","Jazmin")
doctorconoce("Daniel","Jazmin")
doctorconoce("Alejandro","Saul")
doctorconoce("Jazmin","Saul")
doctorconoce("Susana","Manuel")
doctorconoce("Camila","Jazmin")
doctorconoce("Izabel","Daniel")
doctorconoce("Joseline","Susana")
doctorconoce("Joseline","Daniel")
doctorconoce("Joseline","Saul")

#---------------------------------------------------------------------------------------------------------------------------------------------

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
            addVisita(doctor,nombre)
            print("Se agregó su visita con éxito. \n")
        except IndexError:
                print("\nLos nombres ingresados no están en la base de datos. \n")

    elif (opcion==5):
        print("----------Recetar medicina----------")
        paciente = input("Ingrese el nombre del paciente: ")
        medicina = input("Ingrese la medicina recomendada: ")
        doctor = input("Ingrese el nombre del doctor: ")
        try:
            prescripcion(paciente, doctor, medicina)
            print("Receta preescrita. \n")
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
