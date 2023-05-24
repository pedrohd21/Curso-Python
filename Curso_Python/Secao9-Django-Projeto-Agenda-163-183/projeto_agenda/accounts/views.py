from django.shortcuts import render, redirect           # Importar o redirect pra enviar o formulario para o login
from django.contrib import messages, auth               # As mensagem é pra mostrar as mensagem de erro sucesso etc
from django.core.validators import validate_email       # é um pacote de validção de emails
from django.contrib.auth.models import User             # Enviar os dados do usuario no admin so um exemplo
from django.contrib.auth.decorators import login_required
from .models import FormContato


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login Sucesso!')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('dashboard')


def cadastro(request):      ## Aq que acontece a magia
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    
    nome = request.POST.get('nome')             ## validar os campo de resgistros
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:  # Vai verificar se nenhum campo ta vazio
        messages.error(request, 'Nenhum campo pode ficar vazio.')
        return render(request, 'accounts/cadastro.html')        ## caso tiver algum campo vazio vai ficar reclamando

    try:        # Usar para validar o email
        validate_email(email)
    except:
        messages.error(request, 'Email Invalido.')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:          # Senha tem que ter no minimo 6 caracteres
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senha não conferem.')
        return render(request, 'accounts/cadastro.html')
    
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuario já existe.')
        return render(request, 'accounts/cadastro.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já existe.')
        return render(request, 'accounts/cadastro.html')
    
    messages.success(request, 'Registrado com sucesso! Faça o login.')
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome, last_name=sobrenome) # captura os dados na variavel user

    user.save()  # vai salvar na base de dados
    return redirect('login') # vai redirecionar para o login


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})
    
    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})
    
    descricao = request.POST.get('descricao')

    if len(descricao) < 5:
        messages.error(request, 'Descrição precisa ter mais de 5 caracteres.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso.')
    return redirect('dashboard')