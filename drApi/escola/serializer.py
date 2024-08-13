from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from escola.validators import *



class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg','cpf', 'data_nascimento', 'foto']

    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'Numero do CPF invalido'})
       
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome': 'Não pode haver caracteres numericos aqui'})
        
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg': 'O Rg deve ter 9 Digitos'})

        return data
    

class AlunoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg','cpf', 'data_nascimento', 'celular', 'foto']       
    

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'    


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula  
        fields = '__all__'   


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields= ['curso', 'periodo']


    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosEmUmCurso(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']
