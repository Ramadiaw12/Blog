from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    titre = models.CharField(max_length=150)
    resume = models.CharField(max_length=250)
    contenu = models.TextField(blank=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)

    def __str__(self):
        return f"{self.titre}"
