from models import *


def crear_curso(codigo, nombre, version, profesor_id):
    profesor = Profesor.objects.get(rut=profesor_id)
    nuevo_curso = Curso.objects.create(codigo=codigo, nombre=nombre, version=version, profesor=profesor)
    return nuevo_curso

def crear_profesor(rut, nombre, apellido, activo=False, creado_por=None):
    nuevo_profesor = Profesor.objects.create(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por)
    return nuevo_profesor

def crear_estudiante(rut, nombre, apellido, fecha_nacimiento, activo=False, creado_por=None):
    nuevo_estudiante = Estudiante.objects.create(rut=rut, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, activo=activo, creado_por=creado_por)
    return nuevo_estudiante

def crear_direccion(calle, numero, dpto, comuna, ciudad, region, estudiante_id):
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    nueva_direccion = Direccion.objects.create(calle=calle, numero=numero, dpto=dpto, comuna=comuna, ciudad=ciudad, region=region, estudiante=estudiante)
    return nueva_direccion

def obtiene_estudiante(estudiante_id):
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    return estudiante

def obtiene_profesor(profesor_id):
    profesor = Profesor.objects.get(rut=profesor_id)
    return profesor

def obtiene_curso(curso_codigo):
    curso = Curso.objects.get(codigo=curso_codigo)
    return curso

def agrega_profesor_a_curso(profesor_id, curso_codigo):
    curso = Curso.objects.get(codigo=curso_codigo)
    profesor = Profesor.objects.get(rut=profesor_id)
    curso.profesor = profesor
    curso.save()

def agrega_cursos_a_estudiante(estudiante_id, cursos_codigos):
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    cursos = Curso.objects.filter(codigo__in=cursos_codigos)
    estudiante.curso_set.add(*cursos)

def imprime_estudiante_cursos(estudiante_id):
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    cursos = estudiante.curso_set.all()
    for curso in cursos:
        print(curso)
