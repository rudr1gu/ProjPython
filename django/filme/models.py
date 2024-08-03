from django.db import models
from django.utils import timezone

# Create your models here.

LISTA_CATEGORIAS = (
    ("a","selecione uma categoria"),
    ("acao", "Ação"),
    ("comedia", "Comédia"),
    ("drama", "Drama"),
    ("romance", "Romance"),
    ("suspense", "Suspense"),
    ("terror", "Terror"),
    ("ficcao", "Ficção Científica"),
)

#criar urls de filmes
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to="thumbs_filmes/")
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS, default="drama")
    descricao = models.TextField(max_length=1000)
    data_criacao = models.DateTimeField(default=timezone.now)
    visualizacoes = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo