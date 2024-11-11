from django.db import models

def file_location(instance, filename, **kwargs):
    file_path = f"article/{instance.title}-{filename}"
    return file_path

# Create your models here.
class Piso(models.Model):
    title = models.CharField(max_length=60, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to=file_location, null=False, blank=True)
    ubicacion = models.CharField(max_length=255, null=False, blank=False)