from django.db import models

# Create your models here.
class Autor(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)
    birthdate = models.DateField(verbose_name='Fecha de nacimiento', null=False, blank=False)
    deathdate = models.DateField(verbose_name='Fecha de fallecimiento', null=True, blank=True)
    profession = models.CharField(verbose_name='Profesión', max_length=50)
    nationality = models.CharField(verbose_name='Nacionalidad', max_length=50)

    class Meta:
        db_table = 'Autores'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.name

class Libro(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)
    description = models.TextField(verbose_name='Descripciónn', null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)