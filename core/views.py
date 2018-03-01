from django.shortcuts import render
from django.contrib import messages
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.template import Context, loader

from .models import *

from .forms import Contato

# Create your views here.

def error404(request):
    template = loader.get_template('core/404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('core/500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

def index(request):
	context = {
		'destaques': Destaque.objects.order_by('titulo')
	}
	return render(request, 'core/index.html', context=context)

def contato(request):
	form = Contato(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			nome = form.cleaned_data['nome']
			email = form.cleaned_data['email']
			assunto = form.cleaned_data['assunto']
			mensagem = form.cleaned_data['mensagem']

			mensagem = 'Nome: {0}\nE-mail: {1}\nAssunto: {2}\n{3}'.format(nome, email, assunto, mensagem)
			email = EmailMessage(subject='E-mail enviado pelo site [Emakers]',
								 body=mensagem, 
								 from_email=settings.DEFAULT_FROM_EMAIL,
								 to=[settings.DEFAULT_FROM_EMAIL, ], 
								 headers={'Reply-To': email})			
			email.send()

			messages.success(request, 'Enviado com sucesso!')
			form = Contato() # limpa formulario apos mandar
		else:
			messages.error(request, 'Erro ao enviar e-mail.')

	return render(request, 'core/contato.html', {'form': form })

def equipe(request):
	context = {
		'alunos': Aluno.objects.order_by('pos_cargo'),
		'docentes_ta': Docente_ta.objects.order_by('pos_cargo')
	}
	return render(request, 'core/equipe.html', context=context)
