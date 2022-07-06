from django.contrib import admin

# Register your models here.

from .models import Chassi, Carro, Montadora

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero',)

@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'preco', 'chassi', 'montadora', 'get_motoristas')

    def get_motoristas(self, obj):
        return ", ".join(m.username for m in obj.motoristas.all())

    get_motoristas.short_description = 'Motoristas'