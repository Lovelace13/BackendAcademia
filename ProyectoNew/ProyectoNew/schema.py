import graphene
from graphene_django import DjangoObjectType
from Academia.models import Materia, Profesor, Aula


class MateriaType(DjangoObjectType):
    class Meta:
        model = Materia
        fields = ("idmateria","nombre", "codigo","descripcion")


class createMateriaMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        code = graphene.String(required=True)
        description = graphene.String(required=True)

    asignatura = graphene.Field(MateriaType)

    def mutate(self, info, name, code, description):
        asignatura = Materia(nombre=name, codigo=code, descripcion=description)
        asignatura.save()
        return createMateriaMutation(asignatura=asignatura)
    
class deleteMateriaMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required =True)

    message = graphene.String()

    def mutate(self, info, id):
        asignatura = Materia.objects.get(pk=id)
        asignatura.delete()
        return deleteMateriaMutation(message="Libro eliminado")

class updateMateriaMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        code = graphene.String()
        description = graphene.String()

    asignaturaEditada = graphene.Field(MateriaType)

    def mutate(self, info, id, name, code, description):
        asignatura = Materia.objects.get(pk=id)
        asignatura.nombre = name
        asignatura.codigo = code
        asignatura.descripcion = description
        asignatura.save()
        return updateMateriaMutation(asignaturaEditada = asignatura)



class Mutation(graphene.ObjectType):
    create_materia = createMateriaMutation.Field()
    delete_materia = deleteMateriaMutation.Field()
    update_materia = updateMateriaMutation.Field()

    

class AulaType(DjangoObjectType):
    class Meta:
        model = Aula
        fields = ("codigo", "tema", "fecha", "hora")

class ProfesorType(DjangoObjectType):
    class Meta:
        model = Profesor
        fields = ("nombre", "cedula")

class Query(graphene.ObjectType):
    asignaturas = graphene.List(MateriaType)
    asignatura = graphene.Field(MateriaType, id=graphene.ID())
    Aulas = graphene.List(AulaType)
    Aula = graphene.Field(AulaType, id=graphene.ID())
    Educadores = graphene.List(ProfesorType)
    Educador = graphene.Field(ProfesorType, id=graphene.ID())

    def resolve_asignaturas(self, info):
        return Materia.objects.all()

    def resolve_asignatura(self, info, id):
        return Materia.objects.get(pk=id)
    
    def resolve_Aulas(self, info):
        return Aula.objects.all()

    def resolve_Aula(self, info, id):
        return Aula.objects.get(pk=id)
    
    def resolve_Educadores(self, info):
        return Profesor.objects.all()

    def resolve_Educador(self, info, id):
        return Profesor.objects.get(pk=id)
    

esquema = graphene.Schema(query=Query, mutation = Mutation)