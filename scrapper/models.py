from django.db import models

class  Noticia(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
