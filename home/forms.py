from django import forms
from .models import Colaborador, Equipamento, Emprestimo

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'email', 'foto', 'cargo', 'telefone']


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'descricao']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['colaborador', 'equipamento', 'data_emprestimo', 'data_prevista_devolucao', 'status', 'data_devolucao', 'observacao_devolucao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # No cadastro, ocultar status devolvido, danificado, perdido
        if not self.instance.pk:
            self.fields['status'].choices = [
                ('emprestado', 'Emprestado'),
                ('em_uso', 'Em Uso'),
                ('fornecido', 'Fornecido'),
            ]
            self.fields['data_devolucao'].widget = forms.HiddenInput()
            self.fields['observacao_devolucao'].widget = forms.HiddenInput()
        else:
            # No editar, mostrar todos os status
            self.fields['status'].choices = Emprestimo.STATUS_CHOICES
