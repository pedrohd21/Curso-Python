from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)              # SEMPRE FAZER ISSSOOOOO
admin.site.register(Contato, ContatoAdmin)  # Registra os dados para nn parecer nomes aleatorios de Poo