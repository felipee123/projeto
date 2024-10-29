from django.db import models # type: ignore

class Usuario(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    sobrenome = models.TextField(max_length=255)
    email = models.TextField(max_length=255) 




    
