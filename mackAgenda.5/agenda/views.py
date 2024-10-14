from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.

# Home do Projeto
def home(request):
    return render(request, 'usuarios/home.html')

def cadastro_view(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tarefas')
            except:
                return render(request, 'usuarios/cadastro.html', {
                    'form': UserCreationForm,
                    "error": 'Usuário já existe'
                })

        return render(request, 'usuarios/cadastro.html', {
            'form': UserCreationForm,
            "error": 'As senhas são diferentes'
        })

def login_view(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html', {
            'form': AuthenticationForm
        })

    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'usuarios/login.html', {
                'form': AuthenticationForm,
                'error': 'Usuário ou senha estão incorretos'
            })
        else:
            login(request, user)
            return redirect('tarefas')
        
def listar_tarefas(request):
    # Verifica se o usuário está autenticado
    if request.user.is_authenticated:
        # Filtra as tarefas do usuário logado
        tarefas = Tarefa.objects.filter(user=request.user)
    else:
        # Se o usuário não estiver autenticado, pode retornar uma lista vazia ou redirecionar
        tarefas = []  # Ou você pode redirecionar para a página de login

    # Renderiza o template com as tarefas
    return render(request, 'usuarios/tarefas.html', {'tarefas': tarefas})


@login_required
def sair(request):
    logout(request)
    return redirect('home')

@login_required
def tarefas_view(request):
    tarefas = Tarefa.objects.filter(user=request.user) #Filtra as tarefas do usuário 
    return render(request, 'usuarios/tarefas.html')

"""def Cadastro_View(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html', {  # Caminho atualizado
            'form': UserCreationForm()
        })   

    else: 
        if request.POST['password1'] == request.POST['password2']:
            try: 
                user = User.objects.create_user(
                    username=request.POST.get['username'], 
                    password=request.POST.get['password1']
                )
                user.save()
                login(request, user)
                return redirect('tarefas')  # Redireciona para a página de tarefas
                
            except:
                return render(request, 'usuarios/cadastro.html', {  # Caminho atualizado
                    'form': UserCreationForm(),
                    "error": 'Usuário já existe'
                }) 
           
        return render(request, 'usuarios/cadastro.html', {  # Caminho atualizado
            'form': UserCreationForm(),
            "error": 'Senhas são diferentes'
        }) 

def Login_View(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html', {  # Caminho atualizado
            'form': AuthenticationForm()
        })

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'usuarios/login.html', {  # Caminho atualizado
                'form': AuthenticationForm(),
                'error': 'Usuário ou senha estão incorretos'
            })

        else:
            login(request, user)
            return redirect('tarefas')  # Redireciona para a página de tarefas
        """

#@login_required       
def sair(request):
    logout(request)
    return redirect('home')

####################################################################

#@login_required       
def Tarefas(request):
    tarefas = Tarefa.objects.filter(user=request.user)
    #tarefas = Tarefa.objects.all()
    return render(request, 'usuarios/tarefas.html')  # Certifique-se de que a rota está correta

def criar_tarefa(request):
    if request.method == 'GET':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.user = request.user  # Associa a tarefa ao usuário logado
            tarefa.save()
            return redirect('tarefas')
    else:
        form = TarefaForm()

    return render(request, 'usuarios/tarefas.html', {'form': form})



"""def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)  # Cria a tarefa mas não salva ainda
            tarefa.user = request.user  # Associa a tarefa ao usuário logado
            tarefa.save()  # Salva a tarefa no banco de dados
            return redirect('tarefas')
    else:
        form = TarefaForm()
    
    return render(request, 'usuarios/tarefas.html', {'form': form})"""


"""def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)  # Cria a tarefa mas não salva ainda
            #tarefa.user = request.user  # Associa a tarefa ao usuário logado
            tarefa.save()  # Salva a tarefa no banco de dados
            return redirect('tarefas')  # Redireciona para a lista de tarefas
    else:
        form = TarefaForm()
    
    return render(request, 'usuarios/tarefas.html', {'form': form})"""

"""def criar_tarefa(request):
    if request.method == 'GET':
        return render(request, 'usuarios/tarefa.html', {
            'form' : TarefaForm
        })
    else:
        try:
            form = TarefaForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tarefas')
        except ValueError:
            return render(request,'usuarios/tarefa.html', {
                'form' : TarefaForm,
                'error' : 'Favor inserir dados validos'
            })      """


"""def criar_tarefa(request):
    if request.method == 'GET':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)  # Cria a tarefa mas não salva ainda
            tarefa.user = request.user  # Associa a tarefa ao usuário logado
            tarefa.save()  # Salva a tarefa no banco de dados
            return redirect('tarefas')  # Redireciona para a lista de tarefas
    else:
        form = TarefaForm()
    
    return render(request, 'usuarios/tarefas.html', {'form': form})"""


def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, user=request.user)
    
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)  # Verifique se o form está sendo usado corretamente
        if form.is_valid():
            form.save()
            return redirect('tarefas')
    else:
        form = TarefaForm(instance=tarefa)  # Para o método GET, preenche o formulário com a tarefa existente

    return render(request, 'usuarios/tarefas.html', {'form': form, 'tarefa': tarefa})  # Certifique-se de passar a tarefa


def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, user=request.user)

    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas')


"""def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(tarefa, id=tarefa_id, user=request.user)

    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas')"""


"""def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id, user=request.user)  # Garante que a tarefa pertence ao usuário
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas')
    return render(request, '.usuarios/tarefas.html', {'tarefa': tarefa})"""

defexibirTarefas
