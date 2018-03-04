from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.template import Context, loader
from django.db.models import Q	

from .models import *

from .forms import *

# Create your views here.

def error404(request):
    template = loader.get_template('core/404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('core/500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

def index(request):
	context = {
		'destaques': Destaque.objects.order_by('titulo'),
		'servicos': Texto_modal.objects.order_by('pk'),
		'portfolio': Portfolio.objects.order_by('nome'),
	}
	return render(request, 'core/index.html', context=context)

def contato(request):
	form = ContatoForm(request.POST or None)
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
			return redirect('contato') # retorna a mesma pagina de contato
		else:
			messages.error(request, 'Erro ao enviar e-mail.')

	return render(request, 'core/contato.html', {'form': form })

def equipe(request):
	context = {
		'alunos': Aluno.objects.order_by('pos_cargo'),
		'docentes_ta': Docente_ta.objects.order_by('pos_cargo'),
	}	
	return render(request, 'core/equipe.html', context=context)

def blog(request):
	context = {
		'postagens': Postagem.objects.order_by('data_publicacao')
	}
	return render(request, 'core/blog.html', context=context)

                       # refente a url
def blog_post(request, titulo):
	form = ComentarioForm(request.POST or None)
	postagem = Postagem.objects.get(titulo=titulo) # pega a postagem da url
	if request.method == 'POST':
		if form.is_valid():
			nome = form.cleaned_data['nome']
			comentario = form.cleaned_data['comentario']
			comentario_post = Comentario(post_comentado=postagem, 
										nome=nome, 
										comentario=comentario) # salva no bd comentario, com a postagem clicada
			comentario_post.save()
		context = {
			'postagem': postagem,
			'form': form,
		}
		return redirect('blog_post', titulo=titulo) # redireciona para a mesma pag att com o novo comentario
	else:
		comentarios = Comentario.objects.filter(post_comentado=postagem.pk)
		context = {
			'postagem': postagem,
			'comentarios': comentarios,
			'form': form,
		}
	return render(request, 'core/blog_post.html', context=context)

def pesquisa_blog(request):
	query = request.GET.get('q') # pega o value do html
	erro = ''
	if query:
		resultado = Postagem.objects.filter(Q(titulo__icontains=query) |
									    Q(texto__icontains=query) |
									    Q(autor__icontains=query))
	else:
		resultado = Postagem.objects.order_by('data_publicacao')

	if not resultado:
		erro = "Sua pesquisa '" + query + "' não foi encontrada."

	context ={
		'resultado': resultado,
		'erro': erro,
	}							
	return render(request, 'core/pesquisa.html', context=context)