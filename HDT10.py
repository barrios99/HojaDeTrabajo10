#Diana de Leon 18607
#Fatima Albeño 18060
#Luis Perez Aju
#Programa de consulta de doctores y receta de medicinas
#Base de datos en NEO4J

#Documentacion extraida de https://neo4j-rest-client.readthedocs.io/en/latest/

from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474/db/data/")

def addPaciente(nombre, genero, edad, peso estatura):
    paciente= gbd.nodes.create(Nombre:nombre, Genero:genero, Edad:edad, Peso:peso, Estatura:estatura)
    paciente.labels.add("Paciente")


def addDoctor (nombre, especialidad, telefono, correo, ubicacion):
    doctor= gbd.nodes.create(Nombre:nombre, Especialidad:especialidad, Telefono:telefono, Correo:correo, Ubicacion:ubicacion)
    doctor.labels.add("Doctor")

