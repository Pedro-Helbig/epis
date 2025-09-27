def listar_equipamentos(request):
	nome = request.GET.get('nome', '')
	equipamentos = Equipamento.objects.filter(nome__icontains=nome) if nome else Equipamento.objects.all()
	return render(request, 'home/listar_equipamentos.html', {'equipamentos': equipamentos, 'nome': nome})
from .forms import ColaboradorForm, EquipamentoForm, EmprestimoForm
def controle_epi(request, pk=None):
	if pk:
		instance = get_object_or_404(Emprestimo, pk=pk)
	else:
		instance = None
	if request.method == 'POST':
		form = EmprestimoForm(request.POST, instance=instance)
		if form.is_valid():
			# Validação: data prevista > data atual
			from django.utils import timezone
			data_prevista = form.cleaned_data['data_prevista_devolucao']
			if data_prevista <= timezone.now().date():
				messages.error(request, 'A data prevista de devolução deve ser posterior à data atual.')
			else:
				form.save()
				if pk:
					messages.success(request, 'Controle de EPI atualizado com sucesso!')
				else:
					messages.success(request, 'Controle de EPI cadastrado com sucesso!')
				return redirect('controle_epi')
		else:
			messages.error(request, 'Erro ao cadastrar/atualizar controle de EPI.')
	else:
		form = EmprestimoForm(instance=instance)
	return render(request, 'home/controle_epi.html', {'form': form, 'is_edit': pk is not None})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Colaborador, Emprestimo, Equipamento
from .forms import ColaboradorForm, EquipamentoForm

def cadastrar_equipamento(request):
	if request.method == 'POST':
		form = EquipamentoForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Equipamento cadastrado com sucesso!')
			return redirect('cadastrar_equipamento')
		else:
			messages.error(request, 'Erro ao cadastrar equipamento. Verifique os dados.')
	else:
		form = EquipamentoForm()
	return render(request, 'home/cadastrar_equipamento.html', {'form': form})

def editar_equipamento(request, pk):
	equipamento = get_object_or_404(Equipamento, pk=pk)
	if request.method == 'POST':
		form = EquipamentoForm(request.POST, instance=equipamento)
		if form.is_valid():
			form.save()
			messages.success(request, 'Equipamento atualizado com sucesso!')
			return redirect('editar_equipamento', pk=pk)
		else:
			messages.error(request, 'Erro ao atualizar equipamento.')
	else:
		form = EquipamentoForm(instance=equipamento)
	return render(request, 'home/editar_equipamento.html', {'form': form, 'equipamento': equipamento})

def excluir_equipamento(request, pk):
	equipamento = get_object_or_404(Equipamento, pk=pk)
	if request.method == 'POST':
		equipamento.delete()
		messages.success(request, 'Equipamento excluído com sucesso!')
		return redirect('cadastrar_equipamento')
	return render(request, 'home/excluir_equipamento.html', {'equipamento': equipamento})

def home(request):
	return render(request, 'home/home.html')

def cadastrar_colaborador(request):
	if request.method == 'POST':
		form = ColaboradorForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Colaborador cadastrado com sucesso!')
			return redirect('cadastrar_colaborador')
		else:
			messages.error(request, 'Erro ao cadastrar colaborador. Verifique os dados.')
	else:
		form = ColaboradorForm()
	return render(request, 'home/cadastrar_colaborador.html', {'form': form})

def editar_colaborador(request, pk):
	colaborador = get_object_or_404(Colaborador, pk=pk)
	if request.method == 'POST':
		form = ColaboradorForm(request.POST, instance=colaborador)
		if form.is_valid():
			form.save()
			messages.success(request, 'Colaborador atualizado com sucesso!')
			return redirect('editar_colaborador', pk=pk)
		else:
			messages.error(request, 'Erro ao atualizar colaborador.')
	else:
		form = ColaboradorForm(instance=colaborador)
	return render(request, 'home/editar_colaborador.html', {'form': form, 'colaborador': colaborador})

def excluir_colaborador(request, pk):
	colaborador = get_object_or_404(Colaborador, pk=pk)
	if request.method == 'POST':
		colaborador.delete()
		messages.success(request, 'Colaborador excluído com sucesso!')
		return redirect('cadastrar_colaborador')
	return render(request, 'home/excluir_colaborador.html', {'colaborador': colaborador})

def relatorio(request):
	nome = request.GET.get('nome', '')
	colaboradores = Colaborador.objects.filter(nome__icontains=nome) if nome else Colaborador.objects.all()
	emprestimos = Emprestimo.objects.filter(colaborador__in=colaboradores)
	return render(request, 'home/relatorio.html', {
		'colaboradores': colaboradores,
		'emprestimos': emprestimos,
		'nome': nome
	})
