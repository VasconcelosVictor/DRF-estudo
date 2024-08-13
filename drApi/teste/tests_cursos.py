from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CusosTesteCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('cursos-list')
        self.curso_1 = Curso.objects.create(codigo_curso='ctt1',descricao='Curso teste1', nivel='B')
        self.curso_2 = Curso.objects.create(codigo_curso='ctt1',descricao='Curso teste1', nivel='A')


    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisicao GET para listar os cusros"""  

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisicao POST para criar um curso"""
        data = {
            'codigo_curso':'CTT3',
            'descricao' : 'Curso teste 3',
            'nivel': 'A'
        }


        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar se curso é deletado """
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_requisicao_para_atualizar_curso(self):
        """Teste para verificar requisicao PUT para atualizar um curso"""
        data = {
            'codigo_curso': 'CTT1',
            'descricao' : 'Curso teste 1 atualizado',
            'nivel': 'A'
        }

        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    

