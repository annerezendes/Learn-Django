from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


# Register your models here.
# montar o crud


class Alunos(admin.ModelAdmin):
    # alterar e editar
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    # buscar por nome
    search_fields = ('nome',)
    list_per_page = 20 # quantidade de alunos por página

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    
admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
        list_display = ('id', 'aluno', 'curso', 'periodo')
        list_display_links = ('id', )
        
admin.site.register(Matricula, Matriculas)