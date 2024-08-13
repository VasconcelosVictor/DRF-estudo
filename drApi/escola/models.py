from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=10)
    cpf = models.CharField(max_length=12, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=11, default="")
    foto = models.ImageField(blank=True)
    

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    Nivel = (('B', 'Básico'),
             ('I', 'Intermediário'),
             ('A', 'Avaçado'),
             )
    codigo_curso =  models.CharField(max_length=50)
    descricao =  models.CharField(max_length=50)
    nivel =  models.CharField(max_length=2, choices=Nivel, blank=False, null=False, default='B')
    
    def __str__(self):
        return self.descricao
    

class Matricula(models.Model):
    PERIODO = (('M', 'Matitino'),
               ('V', 'Vespertino'),
               ('N', 'Noturno')
               )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')
    

    

