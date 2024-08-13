from rest_framework.test import APITestCase
from escola.models import Curso
from escola.serializer import CursoSerializer

class CursoSerializerTesteCase(APITestCase):
    
    def setUp(self):
        self.curso = Curso(
            codigo_curso = '123',
            descricao = 'Curso de Teste',
            nivel = 'I'
        )
        self.serializer = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estao sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id','codigo_curso', 'descricao', 'nivel']))    

    def test_verificacao_de_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['id'], self.curso.id)
        self.assertEqual(data['codigo_curso'], self.curso.codigo_curso)
        self.assertEqual(data['descricao'], self.curso.descricao)
        self.assertEqual(data['nivel'], self.curso.nivel)