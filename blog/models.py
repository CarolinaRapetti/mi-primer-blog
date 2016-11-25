from django.db import models
from django.utils import timezone


class Post(models.Model): #esta línea define nuestro modelo, es un objeto. Post es el nombre del modelo. models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #Es justo el método publish que mencionábamos antes. def significa que es una función/método y publish es el nombre del método
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title