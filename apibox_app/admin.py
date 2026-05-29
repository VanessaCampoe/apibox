from django.contrib import admin
# registrar  o modelo BOx para que ele apareça na interface da adm do django 
from.models import Box 
class BoxAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero')
    search_fields=('numero',)
admin.site.register(Box, BoxAdmin)


# aqui bbi geral da o migrate de todas as tabelas do django no admim e geraa tudo para voce , 
# Register your models here.
