from django.contrib import admin
from .models import Categoria, Contato

# Register your models here.


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email',
                    'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('telefone', 'mostrar')
    list_per_page = 10


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
