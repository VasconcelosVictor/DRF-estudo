
from rest_framework import viewsets, generics, filters
from escola.models import Aluno, Curso, Matricula
from rest_framework import status
from escola.serializer import AlunoSerializer,AlunoSerializerV2 , CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosEmUmCurso
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    
    
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        return AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['location'] = request.build_absolute_uri() + id
            return response

class MatriculasViewSet(viewsets.ModelViewSet):
    '''Listando todas das matriculas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get','post']

    @method_decorator(cache_page(20))
    def dispatch(self,*args, **kwargs):
        return super(MatriculasViewSet, self).dispatch(*args, **kwargs)

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando Alunos e Alunas matriculados em um Curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosEmUmCurso

    


