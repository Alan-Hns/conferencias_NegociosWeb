from django.contrib import admin
from app_registro.models import Conferencia, Conferencista

# Register your models here.

class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'hora', 'conferencista')
    list_editable = ('nombre', 'conferencista')

admin.site.register(Conferencia, ConferenciaAdmin)


admin.site.register(Conferencista)