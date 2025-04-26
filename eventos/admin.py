from django.contrib import admin
from .models import Evento, Sponsor
from django.utils.html import format_html

# Register your models here.

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'cantidad_sponsors')
    search_fields = ('titulo',)
    list_filter = ('fecha',)

    def cantidad_sponsors(self, obj):
        return obj.sponsors.count()
    cantidad_sponsors.short_description = 'Sponsors'
    

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'mostrar_logo', 'link')
    readonly_fields = ('mostrar_logo',)

    def mostrar_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" height="50"/>', obj.logo.url)
        return "(Sin imagen)"
    mostrar_logo.short_description = 'Logo'


#admin.site.register(Evento, EventoAdmin)
#admin.site.register(Sponsor)