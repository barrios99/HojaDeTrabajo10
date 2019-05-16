#Diana de Leon 18607
#Fatima Albeño 18060
#Luis Perez Aju
#Programa de consulta de doctores y receta de medicinas
#Base de datos en NEO4J

#Documentacion extraida de https://neo4j-rest-client.readthedocs.io/en/latest/

from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="12345")

def addPaciente(nombre, genero, edad, peso estatura):
    paciente= gbd.nodes.create(Nombre:nombre, Genero:genero, Edad:edad, Peso:peso, Estatura:estatura)
    paciente.labels.add("Paciente")

def addDoctor (nombre, especialidad, telefono, correo, ubicacion):
    doctor= gbd.nodes.create(Nombre:nombre, Especialidad:especialidad, Telefono:telefono, Correo:correo, Ubicacion:ubicacion)
    doctor.labels.add("Doctor")

def addMedicina (nombre, dosis, vecesaldia, cantdias):
    medicina = gbd.nodes.create(Nombre:nombre, Dosis:dosis, Veces:vecesaldia, Dias:cantdias)
    medicina.labels.add("Medicina")

def addVisita (nomdoctor, nompaciente):
    pacientes= gbd.labels.get("Paciente")
    pacientes.all()
    doctores= gbd.labels.get("Doctor")
    doctores.all()
    pacientes.get(Nombre:nompaciente)[0].relationships.create("consulto",doctores.get(Nombre:nomdoctor)[0])

def prescripcion (nompaciente, nommedicina, nomdoctor):
    pacientes= gbd.labels.get("Paciente")
    pacientes.all()
    doctores= gbd.labels.get("Doctor")
    doctores.all()
    medicinas= gbd.labels.get("Medicina")
    medicinas.all()
    pacientes.get(Nombre:nompaciente)[0].relationships.create("toma",medicinas.get(Nombre:nommedicina)[0])
    doctores.get(Nombre:nomdoctor)[0].relationships.create("receta",medicinas.get(Nombre:nommedicina)[0])

def pacienteconoce (paciente1, paciente2):
    pacientes= gbd.labels.get("Paciente")
    pacientes.all()
    pacientes.get(Nombre:paciente1)[0].relationships.create("conoce",pacientes.get(Nombre:paciente2)[0])

def doctorconoce (doctor1, doctor2):
    doctores= gbd.labels.get("Doctor")
    doctores.all()
    doctores.get(Nombre:doctor1)[0].relationships.create("conocedoctor",doctores.get(Nombre:doctor2)[0])

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


    

