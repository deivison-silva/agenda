from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    rep_senha = request.POST.get('repetir_senha')

    if not nome or not sobrenome or not email or not usuario or not senha or not rep_senha:
        messages.error(request, 'Preencha todos os campos!')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido!')
        return render(request, 'accounts/register.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuário deve conter no mínimo 6 caracteres!')
        return render(request, 'accounts/register.html')

    if len(senha) < 8:
        messages.error(request, 'A senha deve ter no mínimo 8 caracteres!')
        return render(request, 'accounts/register.html')

    if senha != rep_senha:
        messages.error(request, 'As senhas não conferem!')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe!')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe!')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Usuário cadastrado com sucesso! Faça login para continuar.')

    user = User.objects.create_user(
        username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome)
    user.save()

    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
