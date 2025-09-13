from django.db import models

class Colaborador(models.Model):
	nome = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	foto = models.URLField(blank=True)
	cargo = models.CharField(max_length=50, blank=True)
	telefone = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return self.nome

class Equipamento(models.Model):
	nome = models.CharField(max_length=100)
	descricao = models.TextField(blank=True)

	def __str__(self):
		return self.nome

class Emprestimo(models.Model):
	STATUS_CHOICES = [
		('emprestado', 'Emprestado'),
		('em_uso', 'Em Uso'),
		('fornecido', 'Fornecido'),
		('devolvido', 'Devolvido'),
		('danificado', 'Danificado'),
		('perdido', 'Perdido'),
	]
	colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
	equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
	data_emprestimo = models.DateField()
	data_prevista_devolucao = models.DateField()
	data_devolucao = models.DateField(null=True, blank=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='emprestado')
	observacao_devolucao = models.TextField(blank=True)

	def __str__(self):
		return f"{self.colaborador.nome} - {self.equipamento.nome}"
