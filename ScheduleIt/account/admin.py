from django.contrib import admin
from .models import Evaluacion

# Register your models here.
@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'materia', 'fecha', 'hora', 'lugar', 'creado', 'actualizado', 'usuario']
    list_filter = ['creado', 'actualizado']
    search_fields = ['nombre', 'materia', 'fecha', 'hora', 'lugar', 'creado', 'actualizado', 'usuario']
    date_hierarchy = 'creado'
    ordering = ['creado', 'actualizado']
    prepopulated_fields = {'nombre': ('materia',)}
    raw_id_fields = ['usuario']
    readonly_fields = ['creado', 'actualizado']
    fieldsets = (
        (None, {
            'fields': ('nombre', 'materia', 'fecha', 'hora', 'lugar', 'descripcion')
        }),
        ('Información adicional', {
            'classes': ('collapse',),
            'fields': ('creado', 'actualizado', 'usuario')
        })
    )