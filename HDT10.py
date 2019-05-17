#Diana de Leon 18607
#Fatima Albeño 18060
#Luis Perez Aju
#Programa de consulta de doctores y receta de medicinas
#Base de datos en NEO4J

#Documentacion extraida de https://neo4j-rest-client.readthedocs.io/en/latest/

from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")

def addPaciente(nombre, genero, edad, peso ,estatura):
    paciente= gbd.nodes.create(Nombre=nombre, Genero=genero, Edad=edad, Peso=peso, Estatura=estatura)
    paciente.labels.add("Paciente")

def addDoctor (nombre, especialidad, telefono, correo, ubicacion):
    doctor= gbd.nodes.create(Nombre=nombre, Especialidad=especialidad, Telefono=telefono, Correo=correo, Ubicacion=ubicacion)
    doctor.labels.add("Doctor")

def addMedicina (nombre, dosis, vecesaldia, cantdias):
    medicina = gbd.nodes.create(Nombre=nombre, Dosis=dosis, Veces=vecesaldia, Dias=cantdias)
    medicina.labels.add("Medicina")

def addVisita (nomdoctor, nompaciente):
    pacientes= gbd.labels.get("Paciente")
    pacientes.all()
    doctores= gbd.labels.get("Doctor")
    doctores.all()
    pacientes.get(Nombre=nompaciente)[0].relationships.create("consulto",doctores.get(Nombre=nomdoctor)[0])

def prescripcion (nompaciente, nommedicina, nomdoctor):
    pacientes= gbd.labels.get("Paciente")
    pacientes.all()
    doctores= gbd.labels.get("Doctor")
    doctores.all()
    medicinas= gbd.labels.get("Medicina")
    medicinas.all()
    pacientes.get(Nombre=nompaciente)[0].relationships.create("toma",medicinas.get(Nombre=nommedicina)[0])
    doctores.get(Nombre0nomdoctor)[0].relationships.create("receta",medicinas.get(Nombre=nommedicina)[0])

def pacienteconoce (paciente1, paciente2):
    pacientes= gbd.labels.get("Paciente")
    pacientes.all()
    pacientes.get(Nombre=paciente1)[0].relationships.create("conoce",pacientes.get(Nombre=paciente2)[0])

def doctorconoce (doctor1, doctor2):
    doctores= gbd.labels.get("Doctor")
    doctores.all()
    doctores.get(Nombre=doctor1)[0].relationships.create("conocedoctor",doctores.get(Nombre=doctor2)[0])

def filtroespecialidad (tipo):
    buscar= "MATCH (n:Doctor {Especialidad: '"+tipo+"'}) RETURN n"
    resultados= gbd.query(buscar, data_contents=True)
    listado= resultados.rows
    return listados

def recomendacion(nompaciente, tipo):
    buscar = "MATCH (p:Paciente{Nombre:'"+nompaciente+"'})-[:conoce*1..2]->(amigos)-[:consulto]->(d:Doctor{Especialidad:'"+tipo+"'}) RETURN d"
    resultados = gbd.query(buscar, data_contents=True)
    listado = resultados.rows
    loficial = []
    for x in listado:
        if x not in loficial:
            loficial.append(x)
    return loficial

def recomendaciondoctor (nomdoctor, tipo):
    buscar = "MATCH (d:Doctor{Nombre:'"+nomdoctor+"'})-[:conocedoctor*1..2]->(a:Doctor{Especialidad:'"+tipo+"'}) RETURN a"
    resultados = gbd.query(query, data_contents=True)
    listado = resultados.rows
    loficial = []
    for x in listados:
        if x not in loficial:
            loficial.append(x)
    return loficial

opcion=0
while (opcion!=10):
    print("1. Agregar un paciente\n2. Agregar un doctor\n3. Paciente visita doctor\n4. Doctor receta medicina\n5. Consultar doctor segun especialidad\n6. Añadir conocido\n7. Añadir doctor conocido\n8. Recomendacion segun conocidos\n9. Doctor recomienda doctor\n10. Salir")
    opcion=int(input("Ingrese una opcion: "))
    if (opcion==1):
        nombre=input("Ingrese su nombre: ")
    elif (opcion==2):
    elif (opcion==3):
    elif (opcion==4):
    elif (opcion==5):
    elif (opcion==6):
    elif (opcion==7):
    elif (opcion==8):
    elif (opcion==9):
    

