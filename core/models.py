from django.db import models
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID

# Create your models here.

class Destaque(models.Model):
	titulo = models.CharField(max_length=50)
	texto = models.CharField(max_length=50)
	imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='destaques/'), variations={'normal': (1900, 550, True)})

	def __str__(self):
		return self.titulo

# Servicos
class Servico(models.Model):
	nome = models.CharField(max_length=20)
	exemplos = models.CharField(max_length=50)
	imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='servicos/'), variations={'normal': (1900, 550, True)})
	descricao = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

class Texto_modal(models.Model):
	servico_id = models.ForeignKey(Servico, on_delete=models.DO_NOTHING)
	texto = models.CharField(max_length=200)

	def __str__(self):
		return self.servico_id

class Img_texto(models.Model):
	texto_id = models.ForeignKey(Texto_modal, on_delete=models.DO_NOTHING)
	img = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='servicos/texto-img'), variations={'normal': (1900, 550, True)})

	def __str__(self):
		return self.texto_id

# Equipe
class Aluno(models.Model):
	nome = models.CharField(max_length=20)
	cargo = models.CharField(max_length=20)
	pos_cargo = models.IntegerField(default=0)
	imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='equipe/aluno'), variations={'normal': (1900, 550, True)})
	linkedin = models.CharField(max_length=20)
	github = models.CharField(max_length=20)

	def __str__(self):
		return self.nome

class Docente_ta(models.Model):
	nome = models.CharField(max_length=20)
	cargo = models.CharField(max_length=20)
	pos_cargo = models.IntegerField(default=0)
	imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='equipe/docente_ta'), variations={'normal': (1900, 550, True)})
	linkedin = models.CharField(max_length=20)
	github = models.CharField(max_length=20)

	def __str__(self):
		return self.nome