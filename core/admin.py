from django.contrib import admin

from .models import *

# Register your models here.

class DestaqueAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'descricao',)

class ServicoAdmin(admin.ModelAdmin):
	list_display = ('nome',)

class PortfolioAdmin(admin.ModelAdmin):
	list_display = ('nome',)

class AlunoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cargo',)

class Docente_taAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cargo',)

class PostagemAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'autor',)

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('post_comentado','nome', 'comentario',)

admin.site.register(Destaque, DestaqueAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Texto_modal)
admin.site.register(Img_texto)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Docente_ta, Docente_taAdmin)
admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Comentario, ComentarioAdmin)