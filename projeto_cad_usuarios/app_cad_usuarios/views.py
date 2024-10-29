from urllib import request
from django.shortcuts import render # type: ignore
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.Nome = request.POST.get('nome')
        novo_usuario.Sobrenome = request.POST.get('sobrenome')
        novo_usuario.Email = request.POST.get('email')
        novo_usuario.save()

    # Obter todos os usuários para enviar para o template
    todos_usuarios = Usuario.objects.all()
    
    return render(request, 'usuarios/usuarios.html', {'usuarios': todos_usuarios})
