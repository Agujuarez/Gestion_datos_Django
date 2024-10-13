from django.contrib import admin
from .models import *
import csv
from django.http import HttpResponse

# Register your models here.

def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)
    
    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])
    
    return response

export_as_csv.short_description = "Exportar seleccionados a CSV"

class LibroInline(admin.TabularInline):
    model = Libro
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    fields = ('name', 'birthdate', 'deathdate', 'profession', 'nationality')
    list_display = ('name', 'birthdate', 'deathdate', 'profession', 'nationality')
    inlines = [LibroInline]
    actions = [export_as_csv]

admin.site.register(Autor, AutorAdmin)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'autor')
    list_display = ('name', 'description', 'autor')
    actions = [export_as_csv]
