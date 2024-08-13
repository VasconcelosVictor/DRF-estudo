from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user('vvv', password='123456')
        self.list_url = reverse('cursos-list') # basename + list tras todas

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticacao de um user com as credenciais corretas"""
        user = authenticate(username='vvv', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica uma requisicao GET sem Autenticar"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  

    def test_autenticacao_username_incorreto(self):
        user = authenticate(username='vv', password='123456')
        self.assetFalse((user is not None) and user.is_authenticated)     

    def test_requisicao_get_com_user_autenticado(self):
        """Teste que verifica uma requisição GET de um user autenticado"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

          