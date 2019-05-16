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

