from django.db import models
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID

# Create your models here.

class Destaque(models.Model):
	titulo = models.CharField(max_length=50)
	texto = models.CharField(max_length=50)
	imagem = StdImageField(null=True,blank=True, upload_to=UploadToUUID(path='images/'), variations={'normal': (1900, 550, True)})

	def __str__(self):
		return self.titulo
